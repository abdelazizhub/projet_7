#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
nohup uvicorn api:app --host 0.0.0.0 --port 8080 &
python api.py
streamlit run Dashboard.py