import numpy as np

class LocalDifferentialPrivacyEngine:
    """
    SafePath Analytics: Local epsilon-Differential Privacy (e-DP) Engine.
    Ensures FERPA compliance by injecting mathematical noise at the local edge
    before any student data is aggregated for causal analysis.
    """
    
    def __init__(self, epsilon: float, sensitivity: float = 1.0):
        """
        Initialize the e-DP engine.
        
        Args:
            epsilon (float): The privacy budget. Lower values mean stronger privacy.
            sensitivity (float): The maximum impact a single individual's data 
                                 can have on the aggregate output.
        """
        if epsilon <= 0:
            raise ValueError("Epsilon (privacy budget) must be strictly positive.")
        self.epsilon = epsilon
        self.sensitivity = sensitivity
        # Calculate the scale of the Laplace noise
        self.scale = self.sensitivity / self.epsilon

    def apply_laplace_mechanism(self, true_value: float) -> float:
        """
        Injects Laplace noise into a single numerical data point.
        
        Args:
            true_value (float): The original, un-anonymized measurement.
            
        Returns:
            float: The noisy, privacy-preserving value.
        """
        noise = np.random.laplace(loc=0.0, scale=self.scale)
        return true_value + noise

    def anonymize_dataset(self, data_array: list) -> list:
        """
        Applies local e-DP to an entire array of behavioral telemetry.
        """
        return [self.apply_laplace_mechanism(val) for val in data_array]

# Example usage for testing:
# dp_engine = LocalDifferentialPrivacyEngine(epsilon=0.5)
# safe_screen_time = dp_engine.apply_laplace_mechanism(120.5)
