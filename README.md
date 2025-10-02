# Data-Centric AI Case Study — Heart Disease Dataset

This repo demonstrates a **Data-Centric AI** workflow: focusing on improving data quality first, rather than just tweaking models.  
It is structured as a reproducible case study with **exploration, cleaning, and modeling** steps.
 For demonstration, this repo uses a **small 30-row sample dataset** (`data/raw/heart.csv`) to keep it lightweight.  
> With the full dataset (303 rows from UCI/OPENML), improvements in accuracy after cleaning are more evident.


## Goal
-  Explore dataset → detect missing values, imbalance, correlations.
- Apply data cleaning (imputation, encoding).
- Train baseline vs improved models.
- Compare performance and document findings.

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/jean-granger/data-centric-ai-case-study.git
cd data-centric-ai-case-study
2. Set up environment
bash
Copy code
python -m venv venv
venv\Scripts\activate   # Windows
# OR source venv/bin/activate  # macOS/Linux
pip install -r requirements.txt
3. Run the notebooks
bash
Copy code
jupyter notebook
Open notebooks in order:

01_exploration.ipynb
02_cleaning.ipynb
03_modeling.ipynb
```

## Results summary
- Baseline accuracy: ~0.33
- Processed accuracy: ~0.33
- Because this is a small clean dataset, accuracy did not improve after cleaning.
- In larger datasets with missing values or categorical variables, data-centric fixes lead to measurable gains

## Next Improvements
- Replace sample dataset with full UCI Heart Disease dataset (303 rows).
- Add imbalanced data handling (SMOTE/undersampling).
- Compare multiple models (Logistic Regression, Random Forest, XGBoost).
- Add visual reports (confusion matrix, ROC curve).

## Author
Jean Granger - AI and ML Enthusiast | Aspiring MSc in AI
[LinkedIn](https://linkedin.com/in/ange-granger-jean-365b94320) — jeannange001@gmail.com - aeagsjean@st.knust.edu.gh

## License
This project is released under the MIT License.
