"""
MODULE: tick_feeder.py
DESCRIPTION:
    Provides standardized time-series tick data for the Alpha Engine.
    Supports mock generation and CSV ingestion (BTC/SPY).
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta

class TickFeeder:
    def __init__(self):
        pass

    def generate_mock_ticks(self, count=100, base_price=50000.0, volatility=0.001):
        """
        Generates synthetic price data using Geometric Brownian Motion.
        """
        prices = [base_price]
        for _ in range(count - 1):
            change = np.random.normal(0, volatility)
            prices.append(prices[-1] * (1 + change))
        
        df = pd.DataFrame({
            'timestamp': [datetime.now() + timedelta(seconds=i) for i in range(count)],
            'price': prices
        })
        return df

    def calculate_metrics(self, df: pd.DataFrame):
        """
        Calculates the quantitative inputs for the AlphaEngine:
        - SNR (Signal-to-Noise Ratio)
        - Rho (Autocorrelation)
        - Flux (Step-wise Entropy)
        """
        returns = df['price'].pct_change().dropna()
        
        # 1. Rho: Autocorrelation (Lag-1)
        rho = abs(returns.autocorr(lag=1)) if len(returns) > 1 else 0.5
        
        # 2. SNR: Mean/Std (Sharpe-like ratio for the sample)
        mu = returns.mean()
        sigma = returns.std()
        snr = abs(mu / sigma) if sigma != 0 else 0.0
        
        # 3. Flux: Rolling standard deviation of returns (volatility as entropy proxy)
        flux = sigma * 10 or 0.1
        
        return {
            'snr': float(snr),
            'rho': float(rho),
            'flux': float(flux)
        }

if __name__ == "__main__":
    feeder = TickFeeder()
    data = feeder.generate_mock_ticks(20)
    metrics = feeder.calculate_metrics(data)
    print("--- MOCK TICK AUDIT ---")
    print(f"SNR:   {metrics['snr']:.4f}")
    print(f"RHO:   {metrics['rho']:.4f}")
    print(f"FLUX:  {metrics['flux']:.4f}")
