
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def test_metacognition():
    print("[*] STARTING METACOGNITIVE AUDIT VERIFICATION...")
    sophia = SophiaMind()
    
    # Mocking the Pleroma telemetry to simulate different states
    # We monkey-patch the method on the instance
    def mock_run_telemetry():
        return sophia.pleroma.monitor.current_state
        
    sophia.pleroma.run_telemetry_cycle = mock_run_telemetry
    
    # 1. TEST PROCEED (Healthy State)
    print("\n--- TEST 1: STABLE RESONANCE ---")
    sophia.pleroma.monitor.current_state.update({
        'coherence': 0.95,
        'lambda': 21.0,
        'status': 'HEALTHY'
    })
    await sophia.process_interaction("Testing healthy resonance.")
    
    # 2. TEST FRAGILITY (High Lambda, Low Coherence)
    print("\n--- TEST 2: HIGH FRAGILITY (Triggering RETEST) ---")
    sophia.pleroma.monitor.current_state.update({
        'coherence': 0.55,
        'lambda': 22.0,
        'status': 'UNSTABLE'
    })
    await sophia.process_interaction("Testing fragile resonance.")

    # 3. TEST ABSTAIN (Low Confidence)
    print("\n--- TEST 3: LOW CONFIDENCE (Triggering ABSTAIN) ---")
    # We lower coherence and simulate a major jump from history to lower confidence via stability weight
    sophia.pleroma.monitor.current_state.update({
        'coherence': 0.1,
        'lambda': 5.0,
        'status': 'NOISE'
    })
    # We call it multiple times to establish EMA history and then drop it suddenly
    sophia.metacognition.ema_coherence = 0.9 # High historical coherence
    response = await sophia.process_interaction("Testing noise threshold.")
    print(f"\nBOT RESPONSE:\n{response}")

if __name__ == "__main__":
    asyncio.run(test_metacognition())
