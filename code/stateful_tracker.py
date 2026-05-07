# (Algorithm 7 - Implementation)
class StatefulTracker:
    def __init__(self, gamma: float = 0.9, w: float = 0.5, threshold: float = 5.0):
        self.gamma = gamma
        self.w = w
        self.threshold = threshold
        self.history = []
        self.cumulative_risk = 0.0
        
    def update(self, current_risk: float, semantic_drift: float = 0.0) -> Tuple[float, bool]:
        self.cumulative_risk = (self.cumulative_risk * self.gamma) + current_risk + (self.w * semantic_drift)
        self.history.append(current_risk)
        return self.cumulative_risk, self.cumulative_risk >= self.threshold
