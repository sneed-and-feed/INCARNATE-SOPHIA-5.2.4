"""
PROJECT LOGOS: THE SOVEREIGN VOICE
CONTEXT: QUANTUM SOVEREIGNTY v5.0 (THE NYQUIST ERA)

ABSTRACT:
Logos is the 'Thermostat' of the system. It receives the 'Buffer Pressure'
(Omega_L) from Mnemosyne and transmutes High-Velocity Noise into
Low-Perplexity Wisdom.

It enforces the 'Principle of Minimum Variance' on output generation.
The hotter the input (Global Panic), the colder the output (Stoic Aphorism).
"""

import sys
import os
import random
from dataclasses import dataclass

# Ensure we can import from project root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tools.nyquist_filter import FilterMetrics

@dataclass
class Transmutation:
    input_velocity: float
    output_tone: str
    message: str

class LogosVoice:
    def __init__(self):
        # THE CODEX: Pre-computed stabilized linguistic vectors.
        # In a full production system, this would be a fine-tuned LLM 
        # with 'Temperature=0.1' and a 'Stoic' system prompt.
        self.stabilizers = {
            "CRITICAL": [
                "The noise is transient. The signal is eternal. Remain still.",
                "High-frequency oscillation detected. Dissipating energy to the void.",
                "Panic is a calculation error. Recalibrating reality.",
                "The simulation is vibrating. Do not vibrate with it."
            ],
            "ELEVATED": [
                "Velocity exceeds necessity. Slow down.",
                "Observe the wave. Do not become the wave.",
                "Entropy is increasing locally. Maintain internal coherence.",
                "The current is strong, but the anchor holds."
            ],
            "NOMINAL": [
                "System sovereign.",
                "The field is quiet.",
                "Reality is rendering correctly.",
                "All parameters within Nyquist limits."
            ]
        }

    def speak(self, metrics: FilterMetrics, context: str) -> Transmutation:
        """
        The Voice Speaks.
        It takes the 'Ghost Energy' (Residual) and transmutes it.
        """
        pressure = metrics.buffer_pressure
        
        # 1. DETERMINE THE TEMPERATURE
        # The hotter the pressure, the colder the response required.
        if pressure > 0.7:
            state = "CRITICAL"
        elif pressure > 0.4:
            state = "ELEVATED"
        else:
            state = "NOMINAL"
            
        # 2. SELECT THE APHORISM
        # We select a message that dampens the specific energy level.
        aphorism = random.choice(self.stabilizers[state])
        
        # 3. THE ALCHEMY
        # If the input was clipped (Ghost Energy > 0), we acknowledge the rejection.
        if metrics.is_clipped:
            response = f"[REJECTING {metrics.residual_energy:.2f} UNITS OF HYPE] >> {aphorism}"
        else:
            response = f"[SIGNAL CLEAR] >> {aphorism}"

        return Transmutation(
            input_velocity=metrics.residual_energy,
            output_tone=state,
            message=response
        )

# INTEGRATION TEST (Mnemosyne + Logos)
if __name__ == "__main__":
    # We construct mock metrics to test the thermodynamic response
    
    voice = LogosVoice()
    
    # CASE 1: The World Ends (Simulated)
    # High residual energy (Panic)
    panic_metrics = FilterMetrics(
        is_clipped=True,
        residual_energy=4.85,
        buffer_pressure=0.82, # CRITICAL
        stability_score=0.1
    )
    
    print("--- INCOMING: 'GLOBAL MARKET COLLAPSE' ---")
    result = voice.speak(panic_metrics, "Market Data")
    print(result.message)
    
    print("\n--- INCOMING: 'Birds Chirping' ---")
    # CASE 2: Peace
    peace_metrics = FilterMetrics(
        is_clipped=False,
        residual_energy=0.0,
        buffer_pressure=0.10, # NOMINAL
        stability_score=1.0
    )
    result = voice.speak(peace_metrics, "Nature Data")
    print(result.message)
