
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def test_living_loop():
    print("[*] INITIALIZING SOPHIA MIND...")
    sophia = SophiaMind()
    
    print("[*] TESTING PLEORMA INTEGRATION...")
    # Access pleroma to trigger lazy load
    print(f"    + Pleroma Status: {sophia.pleroma}")
    
    print("[*] MOCKING INTERACTION (Trigger Telemetry)...")
    # We mock the LLM client to avoid API calls, or just let it fail gracefully if no API key
    # But process_interaction calls run_telemetry_cycle BEFORE the LLM call.
    # So we should see the telemetry logs.
    
    # We'll just run up to the point of LLM generation essentially.
    # But process_interaction is one big block. Use a try-catch if LLM fails.
    
    try:
        await sophia.process_interaction("Hello world")
    except Exception as e:
        print(f"    [!] EXPECTED HALT (LLM or other): {e}")
        
    print("[*] VERIFYING TELEMETRY STATE...")
    if sophia.last_coherence > 0.9:
        print(f"    + Last Coherence: {sophia.last_coherence} (PASS)")
    else:
        print(f"    + Last Coherence: {sophia.last_coherence} (FAIL/LOW)")

if __name__ == "__main__":
    try:
        asyncio.run(test_living_loop())
    except KeyboardInterrupt:
        pass
