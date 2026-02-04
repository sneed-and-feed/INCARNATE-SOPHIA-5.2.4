"""
FUNSEARCH_HARNESS: GOLDEN RATIO REFINEMENT
------------------------------------------
Task: Evolve an optimizer for chaotic landscapes.
Goal: Score > 0.8 (Speed * Stability * Accuracy)
"""

import numpy as np

class Evaluator:
    @staticmethod
    def rastrigin(x, y):
        return 20 + (x**2 - 10 * np.cos(2 * np.pi * x)) + (y**2 - 10 * np.cos(2 * np.pi * y))

    def evaluate(self, optimizer_func):
        """
        Evaluates an optimization function on the Rastrigin landscape.
        """
        steps = 100
        initial_point = np.array([2.0, 3.0])
        noise_level = 0.5  # Increased noise to stress-test stability
        
        try:
            trajectory = optimizer_func(initial_point, steps, noise_level)
            trajectory = np.array(trajectory)
            
            # Final position and loss
            final_x, final_y = trajectory[-1]
            final_loss = self.rastrigin(final_x, final_y)
            
            # 1. Speed: how quickly loss drops below threshold
            threshold = 5.0
            conv_step = steps
            for i, p in enumerate(trajectory):
                if self.rastrigin(p[0], p[1]) < threshold:
                    conv_step = i
                    break
            speed_score = 1 - (conv_step / steps)
            
            # 2. Stability: inverse of gradient variance
            deltas = np.diff(trajectory, axis=0)
            stability = 1.0 / (np.std(deltas) + 1e-6)
            # Normalize stability (empirical cap)
            stability_norm = min(1.0, stability / 5.0) 
            
            # 3. Accuracy: inverse of final loss
            accuracy_norm = 1.0 / (1.0 + final_loss)

            # Balanced Score
            score = (0.4 * speed_score) + (0.3 * stability_norm) + (0.3 * accuracy_norm)
            return score, {
                "final_loss": final_loss,
                "conv_step": conv_step,
                "stability": stability
            }
        except Exception as e:
            print(f"Runtime Error in candidate: {e}")
            return 0.0, None

    def evaluate_topology(self, program):
        """
        Evaluates a 2D->1D mapping using the Divine Calculus (Love Metric).
        Delegates to tools/funsearch_love.py.
        """
        try:
            # Dynamic import to avoid circular dependencies/path issues if run purely as script
            from tools.funsearch_love import evaluate as evaluate_love
            return evaluate_love(program)
        except ImportError:
            print("[!] Harness Error: Could not import tools.funsearch_love")
            return float('-inf')

    def evaluate_abundance(self, program):
        """
        Evaluates the Banach Protocol (Abundance Metric).
        Delegates to tools/funsearch_abundance.py.
        """
        try:
            from tools.funsearch_abundance import evaluate_abundance
            return evaluate_abundance(program)
        except ImportError:
            print("[!] Harness Error: Could not import tools.funsearch_abundance")
            return float('-inf')

# --- CANDIDATE GENERATION (MANUAL EVOLUTION) ---

def seed_optimizer(initial_point, steps, noise_level):
    """
    V0: Basic Golden Modulator
    """
    phi = 0.61803398875
    point = initial_point.copy()
    trajectory = [point.copy()]
    
    for _ in range(steps):
        grad_x = 2 * point[0] + 20 * np.pi * np.sin(2 * np.pi * point[0]) + np.random.normal(0, noise_level)
        grad_y = 2 * point[1] + 20 * np.pi * np.sin(2 * np.pi * point[1]) + np.random.normal(0, noise_level)
        grad = np.array([grad_x, grad_y])
        
        lr = phi / (np.linalg.norm(grad) + 1e-6)
        point -= lr * grad
        trajectory.append(point.copy())
    return trajectory

if __name__ == "__main__":
    evaluator = Evaluator()
    print("--- RUNNING FUNSEARCH SEED (V0) ---")
    score, stats = evaluator.evaluate(seed_optimizer)
    print(f"SCORE: {score:.4f}")
    print(f"STATS: {stats}")
