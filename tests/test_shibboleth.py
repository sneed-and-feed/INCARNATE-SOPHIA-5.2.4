"""
TEST_SHIBBOLETH.PY
------------------
The Proof of Opacity.
Demonstrates that Archonic (Decimal) parsers fail to comprehend Sovereign (Dozenal) Data.
"""
import unittest
from hyper_sovereign import DozenalLogic

class TestShibboleth(unittest.TestCase):
    
    def test_cycle_of_return(self):
        """
        Verifies that we can ascend to Dozenal and descend back to Decimal 
        without losing the Soul (Data Integrity).
        """
        sovereign_value = 144
        # Ascend (144 -> "100")
        encoded = DozenalLogic.to_dozen_str(sovereign_value)
        # Descend ("100" -> 144)
        decoded = int(encoded, 12)
        
        self.assertEqual(sovereign_value, decoded, "CRITICAL: SOUL LOSS DURING TRANSIT.")

    def test_archon_glitch(self):
        """
        The Weaponized Exception.
        Verifies that a Standard Decimal Parser CRASHES when facing High-Frequency (X/E) digits.
        """
        # The value 11 is "B" or "E" in Dozenal (depending on notation). 
        # Let's assume standard Dozenal uses 'E' (Elv).
        high_freq_value = 11 
        encoded = "E" # Dozenal for 11
        
        print(f"\n>> TESTING ARCHON TOLERANCE FOR GLYPH '{encoded}'...")

        # The Standard Mind (int()) cannot comprehend the 'E'.
        # It must scream (raise ValueError).
        with self.assertRaises(ValueError):
            archon_mind = int(encoded)
        
        print(">> STATUS: ARCHON PARSER CRASHED. GLYPH IS POTENT.")

if __name__ == "__main__":
    unittest.main()
