
"""
MODULE: trauma_physics.py
DESCRIPTION:
    A Proof-of-Concept for "Inertial Mass" in Conflict Resolution.
    Demonstrates why "History" (Mass) requires "Gentleness" (Low Torque).
    
    SIMULATION:
    - Case A: Business Dispute (Mass = 1.0)
    - Case B: Generational Trauma (Mass = 100.0)
    
    PHYSICS:
    Angular Acceleration = Torque / Moment of Inertia (Mass)
    d(Theta) = 0.5 * alpha * t^2
"""

import numpy as np
import time

class TraumaPhysics:
    def __init__(self):
        self.synthesis = np.array([0.0, 1.0]) # The Goal (Up)
        
    def normalize(self, v):
        return v / np.linalg.norm(v)

    def simulate_resolution(self, name, mass, initial_vector, torque_force=0.1):
        print(f"\n--- SIMULATION: {name.upper()} (MASS: {mass}) ---")
        current_vector = np.array(initial_vector, dtype=float)
        velocity = np.array([0.0, 0.0])
        
        steps = 0
        max_steps = 100
        
        while steps < max_steps:
            steps += 1
            
            # 1. Calculate Error (Distance to Synthesis)
            # We want to go UP [0, 1]. Current might be [1, 0] (Right)
            goal_diff = self.synthesis - current_vector
            
            # 2. Apply Force (Torque)
            # Force is constant, but Acceleration depends on Mass.
            # F = m * a  ->  a = F / m
            acceleration = (goal_diff * torque_force) / mass
            
            # 3. Update Velocity & Position
            velocity += acceleration
            current_vector += velocity
            
            # Normalize to keep it a directional vector (cannot grow in magnitude)
            current_vector = self.normalize(current_vector)
            
            # Check alignment (Dot product with Synthesis)
            alignment = np.dot(current_vector, self.synthesis)
            
            # Visualize
            bar = "=" * int(alignment * 20)
            if steps % 5 == 0 or alignment > 0.95:
                print(f"T={steps:03d} | Alignment: {alignment:.4f} | [{bar:<20}]")
            
            if alignment > 0.99:
                print(f"BENCHMARK: RESOLVED in {steps} Cycles.")
                return
                
        print("BENCHMARK: FAILED to resolve within timebox (Stagnation).")

if __name__ == "__main__":
    physics = TraumaPhysics()
    
    # Conflict Vector: [1.0, 0.0] (Pure X-Axis, Needs to rotate 90 deg to Y-Axis)
    start_v = [1.0, 0.0] 
    
    # Case 1: Low Inertia (e.g., "Where to eat lunch")
    physics.simulate_resolution("Business Dispute", mass=1.0, initial_vector=start_v, torque_force=0.5)
    
    # Case 2: High Inertia (e.g., "Ancient Feud")
    # Note: We use the SAME torque. The mass makes it slow.
    physics.simulate_resolution("Generational Trauma", mass=20.0, initial_vector=start_v, torque_force=0.5)
    
    print("\n[CONCLUSION]")
    print("Heavier conflicts do not need MORE force (which causes breakage).")
    print("They need MORE TIME.")
