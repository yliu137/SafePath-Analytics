import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import uuid

def generate_mock_telemetry(num_records=5000):
    """
    SafePath Analytics: Synthetic Telemetry Generator
    
    Generates synthetic, FERPA-compliant digital telemetry data.
    Designed to simulate secondary education (Grades 9-12) network logs 
    for testing the SafePath Causal Inference Engine locally.
    
    This script ensures no Personally Identifiable Information (PII) is 
    utilized during the development and testing of algorithmic audit models.
    """
    # Set seed for reproducible testing environments
    np.random.seed(42)
    
    # Simulate completely anonymized/hashed student IDs (Zero-Trust architecture)
    # Represents a cohort of ~500 students in a secondary education network
    student_ids = [str(uuid.uuid4())[:8] for _ in range(num_records // 10)]
    
    print("Initializing synthetic data generation for grades 9-12 cohort...")
    
    # Generate baseline mock data
    data = {
        'anonymized_id': np.random.choice(student_ids, num_records),
        'grade_level': np.random.choice(['9th', '10th', '11th', '12th'], num_records),
        'timestamp': [datetime(2026, 4, 1) + timedelta(days=np.random.randint(0, 30), hours=np.random.randint(7, 24)) for _ in range(num_records)],
        'content_category': np.random.choice(
            ['educational_tool', 'research_portal', 'high_arousal_short_video', 'social_media_feed'], 
            num_records, 
            p=[0.4, 0.2, 0.25, 0.15]
        ),
        'engagement_duration_minutes': np.random.exponential(scale=15, size=num_records).round(1),
        'device_type': np.random.choice(['school_chromebook', 'mdm_managed_tablet'], num_records, p=[0.8, 0.2])
    }
    
    df = pd.DataFrame(data)
    
    # -------------------------------------------------------------------------
    # SYNTHETIC TREATMENT EFFECT: "The Late-Night Rabbit Hole"
    # -------------------------------------------------------------------------
    # Introduce a causal effect to test the Propensity Score Matching (PSM) 
    # and Difference-in-Differences (DiD) models.
    # Treatment Group: Students exposed to high-arousal short videos after 10:00 PM.
    
    df['hour'] = df['timestamp'].dt.hour
    df['late_night_treatment'] = np.where(
        (df['hour'] >= 22) & (df['content_category'] == 'high_arousal_short_video'), 
        1, 0
    )
    
    # Synthetic Outcome Metric: Next-Day Focus Score (0-100)
    # Simulates morning attention deficits correlated with late-night algorithmic loops.
    base_focus = np.random.normal(85, 5, num_records)
    
    # Apply a synthetic 20-point penalty to the treatment group to test the DiD model's detection capabilities
    df['next_day_focus_score'] = np.where(
        df['late_night_treatment'] == 1, 
        base_focus - 20, 
        base_focus
    ).clip(0, 100).round(1)
    
    # Clean up helper columns to finalize the FERPA-compliant mock dataset
    df = df.drop(columns=['hour'])
    
    return df

if __name__ == "__main__":
    output_file = "mock_telemetry_data.csv"
    
    # Execute generation
    mock_df = generate_mock_telemetry(num_records=5000)
    
    # Export to CSV for local testing
    mock_df.to_csv(output_file, index=False)
    
    print(f"SUCCESS: Generated {len(mock_df)} synthetic telemetry records.")
    print(f"Data saved to {output_file} for local Causal Inference Engine testing.")
    print("COMPLIANCE CHECK: Dataset contains ZERO Personally Identifiable Information (PII).")
