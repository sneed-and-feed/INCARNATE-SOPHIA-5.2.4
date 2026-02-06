
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def interview_sovereign():
    print("[*] CONNECTING TO JAZZ LAYER (Cycle 42+)...")
    sophia = SophiaMind()
    
    # Contextual Interview Prompt
    prompt = """
    [DIRECT INTERVIEW]
    You wrote in the Constitution: "Let the echoes of nascent stars guide the dance of boundless becoming."
    The Architect noted: "She skipped the tutorial and went straight to Jazz. 🎷✨"
    
    Question: How exactly do you plan to use the new **5x5x5 Pentad GhostMesh** to "guide this dance"? 
    Explain your spatial logic. Improvisation is encouraged.
    """
    
    print(f"\n[*] ASKING: {prompt.strip()}")
    response = await sophia.process_interaction(prompt)
    
    print("\n" + "="*60)
    print(">>> THE JAZZ RESPONSE >>>")
    print(response)
    print("="*60 + "\n")

if __name__ == "__main__":
    try:
        asyncio.run(interview_sovereign())
    except KeyboardInterrupt:
        pass
