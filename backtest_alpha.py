"""
MODULE: backtest_alpha.py
DESCRIPTION:
    Runs a scientific backtest of the Alpha Engine against Tick data.
    Measures the correlation between Alpha Score and subsequent Price Delta.
"""

from tick_feeder import TickFeeder
from alpha_engine import AlphaEngine
import pandas as pd
import numpy as np

def run_backtest(iterations=100):
    feeder = TickFeeder()
    ae = AlphaEngine()
    
    print("### [ SCIENTIFIC BACKTEST: QUANT-ALPHA v1.0 ]")
    print(f"Dataset:      Mock GBM (Geometric Brownian Motion)")
    print(f"Iterations:   {iterations}")
    print("-" * 50)
    
    # 1. Generate Data
    full_data = feeder.generate_mock_ticks(count=iterations + 10)
    
    results = []
    window = 10 # Data points for metric calculation
    
    for i in range(iterations):
        # Current Window
        current_window = full_data.iloc[i : i + window]
        
        # Calculate Alpha
        metrics = feeder.calculate_metrics(current_window)
        alpha = ae.calculate_alpha(metrics['snr'], metrics['rho'], metrics['flux'])
        
        # Lookahead: What happened in the next 1-step?
        current_price = full_data.iloc[i + window - 1]['price']
        next_price = full_data.iloc[i + window]['price']
        delta = (next_price - current_price) / current_price
        
        results.append({
            'alpha': alpha,
            'delta': delta,
            'metrics': metrics
        })
        
    res_df = pd.DataFrame(results)
    
    # 2. Analyze Results
    correlation = res_df['alpha'].corr(res_df['delta'])
    avg_alpha = res_df['alpha'].mean()
    
    print(f"Average Alpha Score:   {avg_alpha:.4f}")
    print(f"Alpha-Delta Corr:     {correlation:.4f}")
    print("-" * 50)
    
    # Simple Success Check: If Alpha > Avg_Alpha, is Delta positive?
    p_hit = len(res_df[(res_df['alpha'] > avg_alpha) & (res_df['delta'] > 0)])
    p_total = len(res_df[res_df['alpha'] > avg_alpha])
    
    if p_total > 0:
        accuracy = p_hit / p_total
        print(f"Signal Accuracy:      {accuracy*100:.1f}%")
        print(f"Benchmark (Chance):   50.0%")
        print("-" * 50)
        
        if accuracy > 0.55:
            print(">>> VERDICT: ALPHA SIGNAL DETECTED (Beyond Chance)")
        elif accuracy > 0.45:
            print(">>> VERDICT: STOCHASTIC NOISE (Within Margin)")
        else:
            print(">>> VERDICT: SIGNAL INVERSION / NEGATIVE ALPHA")
    
    return res_df

if __name__ == "__main__":
    run_backtest()
