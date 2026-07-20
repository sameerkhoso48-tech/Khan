# Job Displacement Risk Analyzer

A Streamlit web application that assesses how vulnerable a job role is to AI-driven automation using a risk-scoring model grounded in task-based displacement theory.

## Project Goal

This tool helps users understand the relative risk of AI/automation displacement across six representative job roles. It provides:

- A **risk score (0–10)** per role, where higher scores indicate greater exposure to automation
- An **explainability panel** describing *why* a role received its score
- An **interactive bar chart** showing the full risk landscape
- **Performance evaluation metrics** for the selected role vs. the midpoint baseline

## Installation

1. **Clone or download this repository.**

2. **Install dependencies** from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```

## Running the App

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501` by default, or at port `5000` if using the included `.streamlit/config.toml`.

## Project Structure

```
.
├── app.py               # Main application entry point
├── requirements.txt     # Python dependencies
├── README.md            # This file
├── data/                # Folder for datasets (extendable)
└── .streamlit/
    └── config.toml      # Streamlit server configuration
```

## Application Modules

| Function | Role |
|---|---|
| `load_data()` | Problem Setup — creates the job role risk dataset |
| `run_model(role, df)` | Core Logic — filters the dataset for the selected role |
| `generate_explanation(score)` | Explainability — returns a human-readable reason for the score |
| `render_ui()` | Visual UI — assembles all Streamlit/Plotly components |

## Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Interactive web UI framework |
| `pandas` | Data manipulation and filtering |
| `plotly` | Interactive chart visualizations |
