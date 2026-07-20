import streamlit as st
import pandas as pd
import plotly.express as px


# 1. Problem Setup Module
def load_data():
    """Load the job displacement risk dataset."""
    data = {
        'Role': [
            'Data Entry',
            'Customer Support',
            'Junior Legal',
            'Skilled Trades',
            'Healthcare',
            'Strategy/Leadership',
        ],
        'Risk_Score': [9, 8, 7, 2, 1, 2],
        'Type': [
            'High Risk',
            'High Risk',
            'High Risk',
            'Resilient',
            'Resilient',
            'Resilient',
        ],
    }
    return pd.DataFrame(data)


# 2. Core Logic Module
def run_model(role_name, dataset):
    """Filter dataset to return the row matching the selected role."""
    result = dataset[dataset['Role'] == role_name]
    return result


# 3. Explainability Module
def generate_explanation(risk_score):
    """Explain why a role received its risk score."""
    if risk_score >= 7:
        return (
            "High Risk: This role involves routine tasks (data/text) highly susceptible "
            "to cognitive automation. AI systems can replicate these workflows with high "
            "accuracy and at scale, making human incumbents vulnerable to displacement."
        )
    return (
        "Resilient: This role requires human-centric skills like empathy, physical "
        "dexterity, or complex judgment that AI cannot reliably replicate today. "
        "Workers in this category are better positioned against near-term automation."
    )


# 4. Visual UI Module
def render_ui():
    """Main Streamlit UI entry point."""
    st.title("Job Displacement Risk Analyzer")
    st.write(
        "Assess how vulnerable a job role is to AI-driven automation using a "
        "risk scoring model grounded in task-based displacement theory."
    )

    df = load_data()

    st.sidebar.header("Controls")
    selected_role = st.sidebar.selectbox("Select a Job Role to Analyze:", df['Role'])

    analyze = st.sidebar.button("Analyze Risk", use_container_width=True)

    # Overview chart always visible
    st.subheader("Risk Landscape — All Roles")
    fig_overview = px.bar(
        df,
        x='Role',
        y='Risk_Score',
        color='Type',
        color_discrete_map={'High Risk': '#EF4444', 'Resilient': '#22C55E'},
        title="AI Displacement Risk Score by Job Role (0 = Safe, 10 = High Risk)",
        labels={'Risk_Score': 'Risk Score (0–10)', 'Role': 'Job Role'},
        text='Risk_Score',
    )
    fig_overview.update_traces(textposition='outside')
    fig_overview.update_layout(yaxis_range=[0, 11], legend_title_text='Risk Category')
    st.plotly_chart(fig_overview, use_container_width=True)

    # Analysis panel
    if analyze:
        st.divider()
        result = run_model(selected_role, df)
        risk = int(result['Risk_Score'].values[0])
        role_type = result['Type'].values[0]

        st.subheader(f"Analysis Results — {selected_role}")

        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                label="Risk Score",
                value=f"{risk} / 10",
                delta=f"{risk - 5:+d} vs. midpoint",
                delta_color="inverse",
            )
        with col2:
            st.metric(label="Category", value=role_type)

        # Explainability panel
        st.subheader("Explainability")
        if risk >= 7:
            st.error(generate_explanation(risk))
        else:
            st.success(generate_explanation(risk))

        # Focused comparison chart
        st.subheader("Performance Evaluation — Role Comparison")
        fig_detail = px.bar(
            df,
            x='Role',
            y='Risk_Score',
            color='Type',
            color_discrete_map={'High Risk': '#EF4444', 'Resilient': '#22C55E'},
            title=f"Risk Score Comparison (Selected: {selected_role})",
            labels={'Risk_Score': 'Risk Score (0–10)', 'Role': 'Job Role'},
        )
        # Highlight selected role
        fig_detail.add_hline(
            y=risk,
            line_dash="dot",
            line_color="orange",
            annotation_text=f"{selected_role}: {risk}",
            annotation_position="top left",
        )
        fig_detail.update_layout(yaxis_range=[0, 11])
        st.plotly_chart(fig_detail, use_container_width=True)

        st.subheader("Evaluation Metric")
        st.write("**Metric:** Risk Level — Lower scores indicate greater job security.")
        st.write(
            f"The selected role **{selected_role}** scored **{risk}/10**. "
            + (
                "Roles with scores ≥ 7 are considered high-risk for displacement. "
                "Consider upskilling toward human-centric competencies."
                if risk >= 7
                else "Roles with scores < 7 are considered resilient. "
                "Continue developing domain expertise and interpersonal skills."
            )
        )


if __name__ == "__main__":
    render_ui()
