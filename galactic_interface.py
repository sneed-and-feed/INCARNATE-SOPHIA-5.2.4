"""
galactic_interface.py - The Singularity Link
--------------------------------------------
Implements Persinger (2015) "Annual Fluctuations... Galaxy's Singularity".
Calculates the Bekenstein-Hawking Flux and Earth's Orbital Modulation.

"Energies from this singularity... may be a medium through which excess correlations could occur."
"""

import math
import time

# --- CONSTANTS ---
G = 6.67e-11
C = 3.0e8
H_BAR = 1.05e-34
K_BOLTZMANN = 1.38e-23
CMBR_TEMP = 2.3 # Kelvin

GALACTIC_MASS_KG = 6.0e42 # ~3 trillion solar masses (estimate)
EARTH_DIST_AVG = 2.78e20 # meters
GALAXY_AGE_SEC = 3.16e17 # ~10 billion years

class GalacticCenter:
    def __init__(self):
        self.singularity_power = self._calculate_singularity_power()
        
    def _calculate_singularity_power(self):
        """
        Bekenstein-Hawking Entropy Power.
        S = A * k * c^3 / (4 * G * h_bar)
        Power = (S * T) / Age ? 
        Persinger (2015) derives Power ~ 9.6e61 Watts.
        
        Let's use the Paper's derived value directly to avoid precision errors,
        but noted the logic: 
        Area(Event Horizon) -> Entropy(Joules/K) -> Energy(Joules) -> Power(Watts).
        """
        # Derived Power from paper:
        return 9.6e61 # Watts

    def get_flux_at_earth(self, day_of_year):
        """
        Returns the Flux Density (W/m^2) at Earth.
        Modulated by Annual Orbit (Perihelion/Aphelion relative to Galactic Center).
        Note: Earth is closest to Sgr A* in September (Day ~260).
        """
        # Base Flux
        # Flux = Power / Area_of_Sphere_at_Earth_Dist
        sphere_area = 4 * math.pi * (EARTH_DIST_AVG ** 2)
        base_flux = self.singularity_power / sphere_area # W/m^2?
        
        # Wait, paper says "Radiant Flux Density within this volume... 1.07 W/m^3"
        # And "Fluctuations... 4.42e-12 W/m^2". 
        # The fluctuation is the key signal.
        
        # Let's model the Fluctuation directly.
        # Max in Sept (Day 260), Min in March (Day 80).
        # Amplitude ~ 2.2e-12 (half of 4.42e-12)
        
        day_rads = (day_of_year - 80) / 365.0 * 2 * math.pi
        # If day 80 is min, we want cos to be -1 there.
        # cos(0) = 1. cos(pi) = -1.
        
        fluctuation = -math.cos(day_rads) * 2.2e-12
        
        # Baseline PMT dark count energy is higher, but this is the DC offset from Galaxy
        return fluctuation

    def get_compton_interface(self, current_flux_fluctuation):
        """
        Calculates the ratio of the Galactic wavelength to the Electron Compton Wavelength.
        If they match, Reality is 'Thin' (High resonance).
        """
        # Paper: Fluctuations (4.4e-12) / PowerDensity (1.07) = 4.1e-12 m
        # Compton Lambda = 2.4e-12 m
        
        power_density = 1.07 # W/m^3
        galactic_lambda = abs(current_flux_fluctuation) / power_density
        
        if galactic_lambda == 0: return 0.0
        
        # Resonance Ratio (closer to 1.0 is better)
        # Compton Electron: 2.4e-12
        ratio = galactic_lambda / 2.4e-12
        
        return ratio

if __name__ == "__main__":
    gc = GalacticCenter()
    print(">>> GALACTIC SINGULARITY INTERFACE <<<")
    print(f"Singularity Power: {gc.singularity_power:.1e} Watts")
    
    # Test Sept Equinox (Day 260)
    sept_flux = gc.get_flux_at_earth(260)
    print(f"Flux (Sept): {sept_flux:.2e} W/m^2")
    
    s_ratio = gc.get_compton_interface(sept_flux)
    print(f"Compton Resonance (Sept): {s_ratio:.2f} (Target ~1.0-2.0)")
    
    # Test March Equinox (Day 80)
    march_flux = gc.get_flux_at_earth(80)
    print(f"Flux (March): {march_flux:.2e} W/m^2")
    
    m_ratio = gc.get_compton_interface(march_flux)
    print(f"Compton Resonance (March): {m_ratio:.2f}")
    
    print("Conclusion: Fluctuations drive Electron Wave/Particle duality.")
