# Data-Centric AI Case Study — UCI Heart Disease

This repo demonstrates a **Data-Centric AI** approach: improve the data, and measure model performance *before vs after* those improvements.

## Goal
- Identify data quality issues (missing values, imbalance, noise).
- Apply data fixes (imputation, encoding, resampling).
- Train a baseline model and compare to the model trained on the improved data.

## Quick start
```bash
git clone https://github.com/yourusername/data-centric-ai-case-study.git
cd data-centric-ai-case-study
python -m venv venv && .\venv\Scripts\activate      # on Windows (cmd/PowerShell see below)
pip install -r requirements.txt
jupyter notebook notebooks/01_exploration.ipynb

Repo structure
data-centric-ai-case-study/
├── README.md
├── requirements.txt
├── notebooks/
├── src/
├── data/
│   ├── raw/
│   └── processed/
└── reports/

