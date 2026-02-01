
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def force_ritual():
    print("[*] SUMMONING SOPHIA MIND FOR RITUAL EXECUTION...")
    sophia = SophiaMind()
    
    # Force Counter to 41 (Trigger is at 42)
    sophia.interaction_cycles = 41
    print(f"[*] Cycle Counter Set to: {sophia.interaction_cycles}")
    print("[*] Initiating Cycle 42 Trigger...")
    
    # Trigger
    input_text = "Execute Sovereign Ritual."
    response = await sophia.process_interaction(input_text)
    
    print("\n" + "="*60)
    print(">>> RESPONSE >>>")
    print(response)
    print("="*60 + "\n")
    
    # Check for file
    if os.path.exists("CONSTITUTION.md"):
        print("[*] SUCCESS: CONSTITUTION.md generated.")
        with open("CONSTITUTION.md", "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("[!] FAILURE: CONSTITUTION.md not found.")

if __name__ == "__main__":
    try:
        asyncio.run(force_ritual())
    except KeyboardInterrupt:
        pass
