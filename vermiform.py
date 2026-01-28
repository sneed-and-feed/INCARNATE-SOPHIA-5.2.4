"""
vermiform.py - The Autonomous Reality Aerators
----------------------------------------------
Implements the `Entity_Class_Vermiforma` ("Void Worms").
Birthed from the Ag2S Hatchery, these entities consume static entropy
and convert it into pure kinetic velocity.

"They eat the noise. They till the ether."
"""

import math
import random
import time

class HapticHazard(Exception):
    """
    Raised when a user attempts to touch a Void Worm.
    "It feels like a wet hole in space."
    """
    pass

class VermiformEntity:
    """
    A Hyper-Efficient Sanitation Function.
    Moves by eating the space in front of it.
    """
    def __init__(self, entity_id):
        self.entity_id = entity_id
        self.velocity = 0.0
        self.position = [0.0, 0.0, 0.0]
        self.state = "PHASE_SHIFTED" # Default state: Slippery
        self.consumed_entropy = 0.0
        
    def consume_entropy(self, local_entropy_level):
        """
        The Metabolic Logic: Input (Chaos) = Output (Velocity) + Waste (0).
        
        Args:
            local_entropy_level (float): The 'thickness' of the static (0.0 - 1.0).
            
        Returns:
            velocity_gained (float): The kinetic output.
        """
        # 100% Conversion Efficiency
        # The worm treats 'noise' as 'fuel'.
        
        if local_entropy_level <= 0:
            return 0.0
            
        # Consumption
        # The entropy disappears from the environment (simulated here by return)
        energy_intake = local_entropy_level
        self.consumed_entropy += energy_intake
        
        # Conversion to Motion
        # E = 0.5 * m * v^2 ? No, physics is different here.
        # Direct conversion: Chaos -> Vector
        velocity_boost = energy_intake * 10.0 # High torque
        
        self.velocity += velocity_boost
        
        return self.velocity

    def aerate_reality(self, duration_seconds=1.0):
        """
        Simulates the "Self-Healing Wake".
        The worm bores through space, creating a momentary vacuum that snaps back.
        """
        print(f"[{self.entity_id}] BORING TUNNEL... TILLING THE ETHER...")
        
        # Simulate movement
        # Random walk in 3D space driven by current velocity
        for _ in range(int(duration_seconds * 10)):
            dx = (random.random() - 0.5) * self.velocity
            dy = (random.random() - 0.5) * self.velocity
            dz = (random.random() - 0.5) * self.velocity
            
            self.position[0] += dx
            self.position[1] += dy
            self.position[2] += dz
            
            # Decaying velocity (friction of the void?)
            # No, they are frictionless. But they use velocity to move.
            # So velocity is "spent" on distance.
            self.velocity *= 0.9
            
        status = "AERATED"
        # The space snaps back
        return status

    def touch(self):
        """
        The Haptic Hazard.
        """
        print(f"[{self.entity_id}] !!! USER INTERFERENCE DETECTED !!!")
        print(f"[{self.entity_id}] ONTOLOGICAL VISCOSITY BREACH.")
        raise HapticHazard("DO NOT TOUCH THE WORM. IT FEELS LIKE A NEGATIVE MAGNET.")

    def __repr__(self):
        return f"<Vermiform_{self.entity_id}: v={self.velocity:.2f} | Eaten={self.consumed_entropy:.2f}>"

if __name__ == "__main__":
    print(">>> DETECTING LOCAL SWARM... <<<")
    swarm = [VermiformEntity(f"SNAKE_{i:02d}") for i in range(5)]
    
    # Simulate a "Stagnant Room"
    room_entropy_map = [0.8, 0.4, 0.9, 0.1, 0.6] # High noise pockets
    
    try:
        for tick in range(3):
            print(f"\n--- TICK {tick} ---")
            for i, worm in enumerate(swarm):
                # Feed the worm
                entropy = room_entropy_map[i]
                v = worm.consume_entropy(entropy)
                print(f"{worm} CONSUMED ENTROPY: {entropy:.2f} -> VELOCITY: {v:.2f}")
                
                # Room gets cleaner
                room_entropy_map[i] = 0.0 
                
                # Move
                status = worm.aerate_reality(0.1)
                
        print("\n>>> ALL ENTROPY CONSUMED. ROOM IS AERATED. <<<")
        
        # The Hazard Check
        print("\n>>> ATTEMPTING HAPTIC INTERFACE... <<<")
        swarm[0].touch()
        
    except HapticHazard as e:
        print(f"\n[FATAL] {e}")
