
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def test_tikkun():
    print("[*] INITIATING TIKKUN HAKLALI VERIFICATION...")
    sophia = SophiaMind()
    
    # 1. State Injection (Create some entropy to purge)
    sophia.memory_bank.append({"content": "ENTROPY", "meta": "CHAOS"})
    sophia.pleroma.monitor.history.append(0.1)
    
    # 2. Execute Tikkun
    print("\n--- EXECUTING /tikkun ---")
    response = await sophia.process_interaction("/tikkun")
    print(response)
    
    # 3. Verify Purge
    print("\n--- VERIFICATION REPORT ---")
    print(f"Memory Bank Size: {len(sophia.memory_bank)} (Expected: 0)")
    # Plenoma loaded lazily during tikkun, verify history cleared
    print(f"Resonance History: {len(sophia.pleroma.monitor.history)} (Expected: 0)")
    
    if len(sophia.memory_bank) == 0 and len(sophia.pleroma.monitor.history) == 0:
        print("[SUCCESS] SYSTEM RECTIFIED.")
    else:
        print("[FAILURE] ENTROPY REMAINS.")

if __name__ == "__main__":
    asyncio.run(test_tikkun())
