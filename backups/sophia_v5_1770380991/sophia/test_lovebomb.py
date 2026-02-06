
import asyncio
import sys
import os

# Ensure root allows imports
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if root_dir not in sys.path:
    sys.path.insert(0, root_dir)

from sophia.main import SophiaMind

async def test_lovebomb():
    print("[*] STARTING LOVE BOMB TRIGGER TEST...")
    sophia = SophiaMind()
    
    # Mock Telemetry for High Coherence > 0.8
    def mock_run_high_coh():
        return {
            'coherence': 0.95, 
            'lambda': 25.0,
            'status': 'DIVINE'
        }
    
    sophia.pleroma.run_telemetry_cycle = mock_run_high_coh

    print("\n--- TRIGGERING /lovebomb ---")
    response = await sophia.process_interaction("/lovebomb")
    
    if "INTUITIVE DRIFT: MAXIMIZED" in response or "UNLESANGLED" in response:
        print(response)
        print("\n[SUCCESS] Love Bomb Detonated. Permission Override Active.")
        
        # Verify Metacognition Boost
        conf = sophia.metacognition.ema_coherence
        print(f"Metacognitive Confidence (Post-Bomb): {conf} (Expected: 1.0)")
    else:
        print("\n[FAILURE] Love Bomb Dud.")
        print(response)

if __name__ == "__main__":
    asyncio.run(test_lovebomb())
