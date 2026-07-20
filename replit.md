# Job Displacement Risk Analyzer

An interactive Streamlit web app that scores job roles by AI-driven automation risk, explains the reasoning, and visualizes the full risk landscape with Plotly charts.

## Run & Operate

- `streamlit run app.py --server.port 5000` — run the Streamlit app (port 5000)
- `pip install -r requirements.txt` — install Python dependencies

## Stack

- Python 3.11
- Streamlit — interactive web UI
- Pandas — data manipulation
- Plotly Express — interactive bar charts

## Where things live

- `app.py` — main application entry point (all four modules)
- `requirements.txt` — Python dependencies
- `data/` — dataset folder (extendable with CSV files)
- `.streamlit/config.toml` — Streamlit server configuration (port 5000, headless)

## Architecture decisions

- All four modules (`load_data`, `run_model`, `generate_explanation`, `render_ui`) live in `app.py` as top-level functions per the lab rubric.
- Risk threshold of ≥ 7 separates High Risk from Resilient, matching the assignment dataset.
- Sidebar controls keep the main content area focused on results and charts.

## Product

A tool for assessing job displacement risk across six representative roles. Users pick a role, click Analyze, and get a risk score, an explanation of why that score was assigned, an overview bar chart, and a performance evaluation metric vs. the midpoint baseline.

## User preferences

_Populate as you build._

## Gotchas

- Always use `streamlit run app.py --server.port 5000` — the `.streamlit/config.toml` is set for port 5000.
- Python packages install to `.pythonlibs/` in this environment (NixOS). Use the package-management skill, not bare `pip install`.

## Pointers

- See the `streamlit` skill for UI and configuration guidelines.
