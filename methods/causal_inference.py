import pandas as pd
from sklearn.linear_model import LogisticRegression
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("SafePath_CausalEngine")

class CausalAuditor:
    """
    Executes Propensity Score Matching (PSM) and Difference-in-Differences (DiD) 
    to isolate the causal impact of algorithmic platform exposure on student well-being,
    filtering out confounding demographic or academic variables.
    """

    def __init__(self):
        self.ps_model = LogisticRegression(solver='liblinear', random_state=42)

    def compute_propensity_scores(self, df: pd.DataFrame, treatment_col: str, covariate_cols: list) -> pd.DataFrame:
        """
        Calculates the probability (propensity score) of a student receiving high algorithmic exposure
        based on observed baseline covariates (e.g., baseline attendance, previous counseling).
        """
        logger.info("Computing Propensity Scores for treatment matching...")
        
        X = df[covariate_cols]
        y = df[treatment_col]
        
        self.ps_model.fit(X, y)
        df['propensity_score'] = self.ps_model.predict_proba(X)[:, 1]
        
        return df

    def estimate_average_treatment_effect(self, matched_df: pd.DataFrame, treatment_col: str, outcome_col: str) -> float:
        """
        Estimates the Average Treatment Effect (ATE) on the matched dataset.
        This provides the final, vendor-neutral insight for school administrators.
        """
        treatment_group = matched_df[matched_df[treatment_col] == 1][outcome_col].mean()
        control_group = matched_df[matched_df[treatment_col] == 0][outcome_col].mean()
        
        ate = treatment_group - control_group
        logger.info(f"Estimated ATE calculated: {ate}")
        
        return ate
