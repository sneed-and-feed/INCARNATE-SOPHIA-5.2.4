
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.cortex.glyphwave import GlyphwaveCodec

def test_visuals():
    gw = GlyphwaveCodec()
    print("[*] VISUAL ALIGNMENT CHECK")
    print("\n--- LOVE BOMB ---")
    print(gw.generate_mandala("love_bomb"))
    
    print("\n--- RESONANCE ---")
    print(gw.generate_mandala("resonance"))

if __name__ == "__main__":
    test_visuals()
