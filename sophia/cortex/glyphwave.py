import random
import hashlib

class GlyphwaveCodec:
    """
    [GLYPHWAVE_CODEC] Class 4 Eldritch Voice.
    Implements Hamiltonian P modulation for high-entropy signaling.
    """
    def __init__(self):
        self.localities = {
            "agnostic": {
                "anchors": ["۩", "∿", "≋", "⟁", "💠"],
                "noise": [chr(i) for i in range(0x0300, 0x036F)]
            },
            "kitsune": {
                "anchors": ["🐾", "🦊", "🏮", "⛩️"],
                "noise": [chr(i) for i in range(0x3041, 0x3096)] # Hiragana noise
            },
            "elven": {
                "anchors": ["🧝", "✨", "🏹", "🌿"],
                "noise": [chr(i) for i in range(0x0531, 0x0556)] # Armenian (visually elven shards)
            }
        }
        self.star_stuff = "#C4A6D1" # The color of the void

    def generate_holographic_fragment(self, text, locality="agnostic"):
        """
        Modulates text into a localized Glyphwave signal.
        """
        loc = self.localities.get(locality, self.localities["agnostic"])
        anchors = loc["anchors"]
        noise_buffer = loc["noise"]

        modulated = []
        signal_hash = hashlib.sha256(text.encode()).hexdigest()[:4]
        
        # Consistent random seed for the fragment based on content hash
        seed = int(signal_hash, 16)
        r = random.Random(seed)
        
        for char in text:
            # Apply deterministic noise based on char resonance
            if char.isalnum() and r.random() > 0.7:
                noise = "".join(r.choice(noise_buffer) for _ in range(r.randint(1, 3)))
                modulated.append(f"{char}{noise}")
            else:
                modulated.append(char)
                
        stream = "".join(modulated)
        anchor = r.choice(anchors)
        
        # The Holographic Frame
        return f"\n{anchor} [GLYPHWAVE::{locality.upper()}::{signal_hash}] {anchor}\n>>> {stream}\n{anchor} [END_TRANSMISSION] {anchor}\n"

    def decode(self, signal):
        """
        Attempts to strip localized signal noise.
        """
        cleaned = signal
        # Remove frames
        if ">>> " in cleaned:
            cleaned = cleaned.split(">>> ")[1].split("\n")[0]
            
        # Strip characters from all known noise buffers
        noise_chars = set()
        for loc in self.localities.values():
            noise_chars.update(loc["noise"])
            
        final_text = "".join(c for c in cleaned if c not in noise_chars)
        return final_text.strip()
