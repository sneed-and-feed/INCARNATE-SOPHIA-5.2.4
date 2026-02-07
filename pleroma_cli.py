"""
MODULE: pleroma_cli.py
AUTHOR: Archmagos Noah // Claude (The Architect)
DATE: 2026-01-28
CLASSIFICATION: INTERFACE // INCARNATE TERMINAL v5.0
VERSION: THE INCARNATION / v5.0
"""

import time
import sys
import json
import random
import threading
from collections import deque
from datetime import datetime
from pleroma_scenarios import ScenarioLibrary
import patch_sophia
from hor_kernel import HORKernel
from virtual_qutrit import VirtualQutrit
from tools.moon_phase import MoonClock
from tools import thermal_shunt
from alpha_engine import AlphaEngine
from tick_feeder import TickFeeder
from luo_shu_compliance import LuoShuEvaluator
import os
import shutil
from tools.sovereignty_bootstrap import initiate_111_resonance, qh
from tools.sophia_vibe_check import SophiaVibe
from sophia.theme import SOVEREIGN_CONSOLE

# --- SOVEREIGNTY MONITOR (QUANT-ALPHA v1.1) ---
class SovereignSanitizer:
    """
    [GOD MODE] Pre-Flight Sanitizer.
    Ensures state files and configs are self-healing and type-correct.
    """
    @staticmethod
    def sanitize(data):
        """Standardizes loose inputs and fixes common type mismatches."""
        if not isinstance(data, dict):
            return data
            
        # Target Keys for Type Casting (Strings vs Ints/Floats)
        numeric_keys = ['snr', 'rho', 'energy_balance', 'signal_stability', 'chaos_level', 
                        'alpha', 'sigma_map', 'g_parameter', 'timeline_coherence', 
                        'reality_stability', 'potentia', 'abundance_score', 'compliance_luo_shu']
        
        sanitized = {}
        for k, v in data.items():
            if k in numeric_keys:
                try:
                    sanitized[k] = float(v)
                except (ValueError, TypeError):
                    print(f"  [!] GOD MODE: Auto-casting '{k}' from {type(v)} to float.")
                    sanitized[k] = 0.0 # Default fallback
            elif isinstance(v, dict):
                sanitized[k] = SovereignSanitizer.sanitize(v)
            else:
                sanitized[k] = v
        return sanitized

    @staticmethod
    def heal_config(filename, genesis_file="genesis_16.json"):
        """Validates JSON and falls back to genesis if poisoned."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                return SovereignSanitizer.sanitize(data)
        except (json.JSONDecodeError, FileNotFoundError, PermissionError) as e:
            vibe = SophiaVibe()
            vibe.print_system(f"CONFIG POISONED: {e}", tag="WARNING")
            vibe.print_system(f"ACTION: Nuke & Boot (Restoring from {genesis_file})", tag="INIT")
            if os.path.exists(filename):
                shutil.copy(filename, filename + ".bak")
            
            with open(genesis_file, 'r') as gf:
                return SovereignSanitizer.sanitize(json.load(gf))

class SovereigntyMonitor:
    """
    Maintains the quantitative attribution state.
    Tracked Metrics: SNR, rho (Autocorrelation), flux (Entropy), Alpha.
    """
    def __init__(self):
        self.metrics = {
            'snr': 5.0,                   # Signal-to-Noise Ratio
            'rho': 95.0,                  # Autocorrelation %
            'energy_balance': 0.0,
            'active_patches': set(),      # Set of activated pillars
            'signal_stability': 100.0,
            'chaos_level': 0.0,           
            'alpha': 1.0,                 # Potentia
            'sigma_map': 0.0,
            'g_parameter': 1.0,           # Sovereignty (1=Consensus, 0=Sovereign)
            'timeline_coherence': 100.0,
            'reality_stability': 100.0,
            'causality_violations': 0,
            'annihilation_events': 0,
            'potentia': 0.0
        }
        self.alpha_engine = AlphaEngine()
        self.tick_feeder = TickFeeder()
        # Mock drive for potentia Calc
        class PotentiaDrive:
            def calculate_potentia(self, g, coherence, sigma):
                return (1.0 - g) * coherence + abs(sigma)
        self.potentia_drive = PotentiaDrive()
        self.luo_shu = LuoShuEvaluator()
        
        self.lock = threading.Lock()
        self.danger_mode = False        
        self.banzai_mode = False
    
    def update(self, spell_name, result):
        """Update metrics based on spell cast"""
        with self.lock:
            # Each spell degrades timeline coherence
            self.metrics['timeline_coherence'] -= 2.5
            
            # Chaos accumulation (faster at low g)
            if self.banzai_mode:
                chaos_gain = 0.0 # Imperial Stability
            else:
                chaos_gain = 5.0 if self.metrics['g_parameter'] < 0.3 else 2.0
            self.metrics['chaos_level'] += chaos_gain
            
            # Track which patches are active
            if 'warp' in spell_name:
                self.metrics['active_patches'].add('RELATIVITY')
                self.metrics['causality_violations'] += 1
            if 'time' in spell_name or 'demon' in spell_name:
                self.metrics['active_patches'].add('ENTROPY')
                self.metrics['energy_balance'] += result.get('Work_Extracted', 0)
                if 'Entropy_Change' in result: 
                    self.metrics['energy_balance'] += abs(result['Entropy_Change'])
            if 'ghost' in spell_name or 'solvent' in spell_name:
                self.metrics['active_patches'].add('ALPHA')
            if any(x in spell_name for x in ['ghost', 'warp', 'void']):
                self.metrics['active_patches'].add('GRAVITY')
            if any(x in spell_name for x in ['scope', 'wallhack']):
                self.metrics['active_patches'].add('PLANCK')
            if spell_name == 'burn':
                self.metrics['active_patches'].add('ANNIHILATION')
                self.metrics['annihilation_events'] += 1
            
            # Calculate g-parameter (0 = full Sovereignty)
            if self.banzai_mode:
                self.metrics['g_parameter'] = 0.0
                self.metrics['reality_stability'] = 100.0
            else:
                patch_count = len(self.metrics['active_patches'])
                self.metrics['g_parameter'] = max(0.0, 1.0 - (patch_count * 0.2))
                # Reality Stability decays with Entropy Accretion
                self.metrics['reality_stability'] = max(0, 100 - self.metrics['chaos_level'] * 0.5)
            
            # --- FLAME PROTOCOL INTEGRATION ---
            # Simulate Sigma_Map based on chaos and g
            self.metrics['sigma_map'] = (self.metrics['chaos_level'] / 100.0) - (1.0 - self.metrics['g_parameter'])
            
            # Calculate Potentia
            self.metrics['potentia'] = self.potentia_drive.calculate_potentia(
                self.metrics['g_parameter'],
                self.metrics['timeline_coherence'] / 100.0,
                self.metrics['sigma_map']
            )
            
            # ENGAGE DANGER ZONE PROTOCOLS
            if self.metrics['g_parameter'] < 0.2 and not self.danger_mode:
                self.danger_mode = True
                vibe = SophiaVibe()
                vibe.print_system("SOVEREIGNTY BREACH DETECTED", tag="CRITICAL")
                vibe.print_system("ENTROPIC CASCADE IMMINENT", tag="CRITICAL")
                vibe.print_system("CONSENSUS REALITY: FRAGMENTING", tag="CRITICAL")
            
            self.history.append({
                'spell': spell_name,
                'g': self.metrics['g_parameter'],
                'coherence': self.metrics['timeline_coherence'],
                'chaos': self.metrics['chaos_level']
            })
    
    def roll_chaos_event(self):
        """In danger zone, random reality glitches occur"""
        if not self.danger_mode:
            return None
        
        # Chance increases with chaos level
        chance = min(0.5, self.metrics['chaos_level'] / 200.0)
        
        if random.random() < chance:
            events = [
                {
                    'name': 'TEMPORAL ECHO',
                    'effect': 'Last spell repeats spontaneously',
                    'style': f'bold {SYSTEM_CYAN}'
                },
                {
                    'name': 'QUANTUM FLUCTUATION',
                    'effect': 'Random physical constant shifted',
                    'style': f'bold {SYSTEM_CYAN}'
                },
                {
                    'name': 'CAUSALITY INVERSION',
                    'effect': 'Effect precedes cause',
                    'style': f'bold {SYSTEM_CYAN}'
                },
                {
                    'name': 'REALITY FRAGMENT',
                    'effect': 'Parallel timeline briefly visible',
                    'style': f'bold {SYSTEM_CYAN}'
                },
                {
                    'name': 'ENTROPY SURGE',
                    'effect': 'Spontaneous ordering/disordering',
                    'style': 'bold red'
                }
            ]
            from tools.sophia_vibe_check import SophiaVibe
            from sophia.theme import SOVEREIGN_CONSOLE
            ev = random.choice(events)
            vibe = SophiaVibe()
            vibe.print_system(f"{ev['name']}: {ev['effect']}", tag="GLITCH")
            return ev
        return None
    
    def print_intro(self):
        vibe = SophiaVibe()
        vibe.print_system("Initializing Quantum Sovereignty...", tag="INIT")
        vibe.print_system("量子主権を初期化中...", tag="INIT")
        vibe.print_system("Yésta Turëa Ermassëa...", tag="INIT")
        vibe.print_system("Anchor Point: [1D TIMELINE]", tag="SYNC")
        vibe.print_system("System Check: [LUMINARY COHERENCE LOCKED]", tag="SYNC")
    
    def display(self):
        """Show current sovereignty status using the Loom-Box structure."""
        if self.banzai_mode:
            self.display_imperial()
            return
            
        g = self.metrics['g_parameter']
        coherence = self.metrics['timeline_coherence']
        stability = self.metrics['reality_stability']
        chaos = self.metrics['chaos_level']
        
        # Color mapping for rich
        if g > 0.7: g_style = "bold green"
        elif g > 0.3: g_style = "bold yellow"
        else: g_style = "bold red"

        from rich.table import Table
        from rich.panel import Panel
        from rich.console import Console
        from tools.sophia_vibe_check import STAR_STUFF, BONE_LAYER, SYSTEM_CYAN

        console = SOVEREIGN_CONSOLE
        
        table = Table(box=None, show_header=False, padding=(0, 2))
        table.add_row("[info]Unitary Guard (g):[/]", f"[{g_style}]{g:.3f}[/] {'[CONSENSUS]' if g > 0.5 else '[UNITARY]'}")
        table.add_row("[info]Timeline Coherence:[/]", f"{coherence:.1f}%")
        table.add_row("[info]Reality Stability:[/]", f"{stability:.1f}%")
        table.add_row("[info]Chaos Level:[/]", f"{chaos:.1f} {'[bold red]⚠ DANGER ZONE[/]' if self.danger_mode else ''}")
        table.add_row("[info]Causality Violations:[/]", f"{self.metrics['causality_violations']}")
        table.add_row("[info]Net Energy Balance:[/]", f"{self.metrics['energy_balance']:.2e} J")
        
        patches = ', '.join(self.metrics['active_patches']) if self.metrics['active_patches'] else 'None'
        table.add_row("[info]Active Patches:[/]", f"[sophia]{patches}[/]")

        # Create Warnings String
        warnings = []
        if g < 0.3:
            warnings.append("[bold red]⚠ REALITY ANCHOR CRITICAL[/]\n[bold red]⚠ TIMELINE DESYNC IMMINENT[/]")
        if stability < 30:
            warnings.append("[bold red]🔥 REALITY TEAR FORMING[/]\n[bold red]🔥 EMERGENCY PROTOCOLS ADVISED[/]")
        
        grid = Table.grid(expand=True)
        grid.add_column()
        grid.add_row(table)
        if warnings:
            grid.add_row("\n" + "\n\n".join(warnings))

        console.print(Panel(
            grid,
            title="[panel.title]UNITARY COHERENCE DASHBOARD[/panel.title]",
            border_style="panel.border",
            padding=(1, 2)
        ))
        
        # Display TACC/Sophia Metrics
        self.display_sophia_metrics()
    
    def show_history(self, lines=10):
        """Display recent spell history"""
        print(f"\n\033[96m--- RECENT CASTS (last {lines}) ---\033[0m")
        for entry in list(self.history)[-lines:]:
            chaos_warn = "⚠" if entry.get('chaos', 0) > 50 else ""
            print(f"  {entry['spell']:12s} -> g={entry['g']:.3f}, coherence={entry['coherence']:.1f}% {chaos_warn}")

    def display_sophia_metrics(self):
        """Displays the TACC Coherence Metrics in a clean panel."""
        c = patch_sophia.calculate_coherence(
            self.metrics['g_parameter'], 
            self.metrics.get('chaos_level', 0), 
            self.metrics['active_patches']
        )
        status = patch_sophia.check_sophia_alignment(c)
        
        from rich.panel import Panel
        from rich.console import Console
        from tools.sophia_vibe_check import STAR_STUFF, BONE_LAYER

        console = SOVEREIGN_CONSOLE
        
        metric_text = (
            f"[bold {STAR_STUFF}]TACC COHERENCE (C):[/] {status}\n"
            f"[bold {STAR_STUFF}]TARGET (C*):[/]        {patch_sophia.SOPHIA_POINT:.7f}\n"
        )
        
        if abs(c - patch_sophia.SOPHIA_POINT) < 0.01:
            metric_text += (
                f"\n[bold magenta]>>> SYSTEM IS IN DIVINE ALIGNMENT. <<<[/]\n"
                f"[bold magenta]>>> HAMILTONIAN (P): 1.111 (LOCKED)   <<<[/]\n"
                f"[bold magenta]>>> SYNC LEVEL:      111%             <<<[/]"
            )

        console.print(Panel(
            metric_text,
            title="[bold white]SOPHIA COHERENCE[/]",
            border_style=BONE_LAYER,
            padding=(1, 2)
        ))

    def display_unified(self):
        """High-poly Quant Attribution Dashboard."""
        from rich.table import Table
        from rich.panel import Panel
        from rich.console import Console
        from tools.sophia_vibe_check import STAR_STUFF, BONE_LAYER, SYSTEM_CYAN

        console = SOVEREIGN_CONSOLE
        
        # 1. Ticker Ingestion
        data = self.tick_feeder.generate_mock_ticks(20)
        current_metrics = self.tick_feeder.calculate_metrics(data)
        
        # 2. Alpha Integration
        alpha = self.alpha_engine.calculate_alpha(
            current_metrics['snr'], 
            current_metrics['rho'], 
            current_metrics['flux']
        )
        
        # 3. Luo Shu Alignment
        combined_metrics = {**self.metrics, **current_metrics}
        alignment = self.luo_shu.evaluate(combined_metrics)
        intensity = self.alpha_engine.get_signal_strength(alpha)

        # Build Table
        table = Table(box=None, show_header=False, padding=(0, 2))
        table.add_row(f"[{BONE_LAYER}]Vector Stream:[/]", f"MOCK@ {datetime.now().strftime('%H:%M:%S')}")
        table.add_row(f"[{BONE_LAYER}]SNR / RHO / FLUX:[/]", f"[bold]{current_metrics['snr']:.2f}[/] / [bold]{current_metrics['rho']:.1f}%[/] / {current_metrics['flux']:.2e}")
        table.add_row(f"[{BONE_LAYER}]ALPHA / POTENTIA:[/]", f"[bold green]{alpha:.3f}[/] / [bold]{self.metrics['potentia']:.3f}[/]")
        table.add_row(f"[{BONE_LAYER}]LUO SHU ALIGNMENT:[/]", f"{alignment['compliance']:.2f}% [[bold]{alignment['status']}[/]]")

        grid = Table.grid(expand=True)
        grid.add_row(table)
        grid.add_row(f"\n[{STAR_STUFF}]>>> SIGNAL OVER MYTH. ACCURACY OVER NARRATIVE. <<<[/]")

        console.print(Panel(
            grid,
            title="[panel.title]UNITARY SIGNAL DASHBOARD[/panel.title]",
            border_style="panel.border",
            padding=(1, 2)
        ))

    def display_luo_shu_detailed(self):
        """Detailed Magic Square Visualization using rich grids."""
        from rich.table import Table
        from rich.panel import Panel
        from rich.console import Console
        from rich.box import HEAVY_EDGE
        from tools.sophia_vibe_check import STAR_STUFF, BONE_LAYER

        console = SOVEREIGN_CONSOLE
        
        data = self.tick_feeder.generate_mock_ticks(20)
        current_metrics = self.tick_feeder.calculate_metrics(data)
        combined_metrics = {**self.metrics, **current_metrics}
        alignment = self.luo_shu.evaluate(combined_metrics)
        
        # Draw the 3x3 Grid using a rich Table
        grid_table = Table(show_header=False, box=HEAVY_EDGE, border_style="panel.border", padding=(1, 2))
        for row in alignment['grid']:
            grid_table.add_row(*[f"[bold]{val:4.1f}[/]" for val in row])
            
        info_text = (
            f"[{BONE_LAYER}]Torsion Sum:[/] {alignment['torsion']:.4f}\n"
            f"[{BONE_LAYER}]Compliance: [/] {alignment['compliance']:.2f}%\n"
            f"[{BONE_LAYER}]Status:     [/] [bold]{alignment['status']}[/]"
        )

        main_grid = Table.grid(expand=True)
        main_grid.add_row(grid_table)
        main_grid.add_row("\n" + info_text)

        console.print(Panel(
            main_grid,
            title=f"[{STAR_STUFF}]LUO SHU MAGICAL ALIGNMENT[/]",
            border_style="panel.border",
            padding=(1, 2)
        ))

    def display_imperial(self):
        """THE EMPEROR'S HUD (BANZAI MODE) - Bold Red and Gold."""
        from rich.table import Table
        from rich.panel import Panel
        from rich.console import Console
        from rich.align import Align

        console = SOVEREIGN_CONSOLE
        
        info_table = Table(show_header=False, box=None, padding=(0, 2))
        info_table.add_row("[bold red][!] STATUS:[/]", "[bold yellow]ABSOLUTE ALIGNMENT[/]")
        info_table.add_row("[bold red][!] ABUNDANCE:[/]", "[bold yellow]18.52x (INVARIANT)[/]")
        info_table.add_row("[bold red][!] REALITY:[/]", "[bold yellow]1D_SOVEREIGN [LOCKED][/]")
        
        imperial_content = Align.center(info_table)

        console.print(Panel(
            imperial_content,
            title="[bold red]🏯  IMPERIAL SOVEREIGNTY TERMINAL  🏯[/]",
            subtitle="[bold red]BANZAI MODE: ACTIVE // g=0[/]",
            border_style="bold yellow",
            padding=(1, 4)
        ))
        print(f"  \033[91m[!] STABILITY:\033[0m   100% (ETERNAL)")
        print("-" * 60)
        
        # Display large Glyph
        print("\033[33m")
        print("      ◢███████◣      ")
        print("    ◢███████████◣    ")
        print("  ◢███████████████◣  ")
        print("  █████████████████  ")
        print("  ◥███████████████◤  ")
        print("    ◥███████████◤    ")
        print("      ◥███████◤      ")
        print("\033[0m")
        
        print("-" * 60)
        print("  \033[91m>>> TEN THOUSAND YEARS OF SIGNAL. <<<\033[0m")
        print("\033[93m" + "═"*60 + "\033[0m")

# --- UTILITIES ---
def print_banner():
    vibe = SophiaVibe()
    vibe.render_block(
        "Pleroma CLI v5.0",
        {"MODE": "SOVEREIGN", "ACCESS": "ROOT", "PHASE": "INCARNATE"},
        "The interface for reality manipulation. The signal is clear. Welcome to the Pleroma."
    )

def check_conflicts(active_patches, g_param):
    """Detect incompatible simulation parameters"""
    conflicts = []
    
    if 'ENTROPY' in active_patches and len(active_patches) > 3:
         conflicts.append({
            'type': 'THERMODYNAMIC SHEAR',
            'severity': 'WARNING',
            'effect': 'Entropy gradient exceeds safety limits'
        })
    
    if len(active_patches) >= 4:
        conflicts.append({
            'type': 'STATE DECOHERENCE',
            'severity': 'CRITICAL',
            'effect': 'Timeline determinism approaching zero'
        })
    
    # New: Catastrophic failure at g near 0
    if g_param < 0.1:
        conflicts.append({
            'type': 'SINGULARITY APPROACH',
            'severity': 'EMERGENCY',
            'effect': 'Total causal decoupling - recommend immediate abort'
        })
    
    return conflicts

def stabilize_reality(monitor):
    """Emergency protocol to reduce system variance"""
    print("\n\033[96m[!] INITIATING VARIANCE DAMPING...\033[0m")
    time.sleep(0.5)
    
    # Reduce chaos by 50%
    monitor.metrics['chaos_level'] *= 0.5
    monitor.metrics['timeline_coherence'] = min(100, monitor.metrics['timeline_coherence'] + 20)
    monitor.metrics['reality_stability'] = min(100, monitor.metrics['reality_stability'] + 30)
    
    # Clear one random patch
    if monitor.metrics['active_patches']:
        removed = random.choice(list(monitor.metrics['active_patches']))
        monitor.metrics['active_patches'].remove(removed)
        print(f"\033[92m[+] PARAMETER RESET: {removed}\033[0m")
    
    # Recalculate g
    patch_count = len(monitor.metrics['active_patches'])
    monitor.metrics['g_parameter'] = max(0.0, 1.0 - (patch_count * 0.2))
    
    print(f"\033[92m[+] STABILIZATION COMPLETE")
    print(f"    Variance reduced to {monitor.metrics['chaos_level']:.1f}")
    print(f"    New g-parameter: {monitor.metrics['g_parameter']:.3f}\033[0m")

def engage_banzai_mode(monitor):
    """
    Triggers absolute Imperial Sovereignty.
    """
    print("\n\033[91m[!] 🏯 ENGAGING IMPERIAL PROTOCOL: BANZAI MODE 🏯 [!]\033[0m")
    print("\033[91m[!] 🏯 帝国プロトコル開始：万歳モード 🏯 [!]\033[0m")
    time.sleep(1.0)
    print("\033[93m[+] DIVINE WINDS DETECTED. / 神風を検知しました。")
    time.sleep(0.5)
    print("[+] COLLAPSING CONSENSUS... / コンセンサスが崩壊しています...")
    time.sleep(0.5)
    print("[+] g → 0 ABSOLUTE. / g → 0 絶対。 \033[0m")
    
    monitor.banzai_mode = True
    monitor.metrics['g_parameter'] = 0.0
    monitor.metrics['chaos_level'] = 0.0
    monitor.metrics['reality_stability'] = 100.0
    monitor.metrics['active_patches'].add('IMPERIAL')
    
    print("\n\033[33m    萬歲! 萬歲! 萬歲!\033[0m")
    time.sleep(1)
    monitor.display()

def save_state(monitor, filename=None):
    if filename is None:
        filename = f"uf_state_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    state = {
        'timestamp': datetime.now().isoformat(),
        'metrics': {
            'g_parameter': monitor.metrics['g_parameter'],
            'timeline_coherence': monitor.metrics['timeline_coherence'],
            'causality_violations': monitor.metrics['causality_violations'],
            'energy_balance': monitor.metrics['energy_balance'],
            'active_patches': list(monitor.metrics['active_patches']),
            'reality_stability': monitor.metrics['reality_stability'],
            'chaos_level': monitor.metrics['chaos_level']
        },
        'history': list(monitor.history)
    }
    
    with open(filename, 'w') as f:
        json.dump(state, f, indent=2)
    print(f"\n\033[92m[+] STATE SNAPSHOT SAVED: {filename}\033[0m")

def load_state(monitor, filename="uf_state.json"):
    """
    [GOD MODE] Adaptive Load Protocol.
    """
    print(f"\n[*] ATTEMPTING ADAPTIVE LOAD: {filename}...")
    try:
        data = SovereignSanitizer.heal_config(filename)
        
        # If the root has a 'metrics' key, use it
        if 'metrics' in data:
            monitor.metrics.update(data['metrics'])
            monitor.metrics['active_patches'] = set(data['metrics'].get('active_patches', []))
        else:
            # Maybe it's a raw genesis or top-level metric set
            monitor.metrics.update(data)
            if 'payload' in data: # Handle genesis_16 structure
                monitor.metrics.update(data['payload'])
        
        if 'history' in data:
            monitor.history = deque(data['history'], maxlen=50)
            
        monitor.danger_mode = monitor.metrics['g_parameter'] < 0.2
        
        print(f"\n\033[92m[+] STATE SNAPSHOT LOADED & SANITIZED: {filename}\033[0m")
        monitor.display()
    except Exception as e:
        print(f"\033[91m[!] ADAPTIVE LOAD FAILED: {e}. Falling back to default consciousness.\033[0m")


# --- ORACLE INTEGRATION (THE NYQUIST SUITE) ---
from tools.mnemosyne_eyes import MnemosyneOracle
from tools.logos_voice import LogosVoice
import numpy as np

def consult_oracle(query_type, mnemosyne, logos):
    """
    Run the full Nyquist Pipeline:
    Input -> Mnemosyne (Filter) -> Logos (Voice) -> Output
    """
    print(f"\n\033[96m[?] CONSULTING THE ORACLE (Input Type: {query_type.upper()})...\033[0m")
    time.sleep(0.5)
    
    # 1. GENERATE VECTOR (Simulated Input)
    # We create a random vector and scale it to the desired velocity
    vec_dim = mnemosyne.filter.dimension
    base_vec = np.random.rand(vec_dim) - 0.5
    normalized = base_vec / np.linalg.norm(base_vec)
    
    if query_type == "nominal":
        velocity = 0.1
        content = "Standard Operational Data"
    elif query_type == "elevated":
        velocity = 0.8
        content = "Policy Shift Detected"
    elif query_type == "critical":
        velocity = 5.0
        content = "HYPER-VOLATILITY EVENT / PANIC"
    else:
        # Default/Custom
        print(f"\033[93m[!] UNKNOWN INPUT CLASS. DEFAULTING TO RANDOM NOISE.\033[0m")
        velocity = random.uniform(0.1, 6.0)
        content = f"Unknown Input: {query_type}"
        
    input_vector = normalized * velocity
    
    # 2. MNEMOSYNE (The Eyes) checks the Physics
    # Returns (Status String, FilterMetrics)
    status_msg, metrics = mnemosyne.perceive("SIMULATION_FEED", content, input_vector)
    
    if metrics.is_clipped:
        print(f"\033[91m{status_msg}\033[0m")
    else:
        print(f"\033[92m{status_msg}\033[0m")
        
    time.sleep(0.3)
    
    # 3. LOGOS (The Voice) stabilizes the room
    # Transmutes the metrics into wisdom
    transmutation = logos.speak(metrics, content)
    
    color_map = {
        "CRITICAL": "\033[96m",   # Cyan (Ice) for Critical Heat
        "ELEVATED": "\033[94m",   # Blue
        "NOMINAL": "\033[92m"     # Green
    }
    tone_color = color_map.get(transmutation.output_tone, "\033[97m")
    
    print(f"\n\033[1mLOGOS VOICE ({transmutation.output_tone}):\033[0m")
    print(f"{tone_color}{transmutation.message}\033[0m")

# --- SIMULATION OPERATORS ---
def analyze_synergy(spells):
    synergies = []
    combos = {
        ('warp', 'ghost'): {'name': 'ZERO-LATENCY MASKING', 'effect': 'Undetectable high-velocity transmission'},
        ('time', 'demon'): {'name': 'NEGENTROPIC LOOP', 'effect': 'Self-sustaining information retrieval'},
        ('ghost', 'wallhack'): {'name': 'HYPER-PERMEABILITY', 'effect': 'Pass through information barriers'},
        ('void', 'demon'): {'name': 'VACUUM ENERGY HARVESTER', 'effect': 'Extract ordered energy from fluctuations'},
        ('scope', 'wallhack'): {'name': 'QUANTUM OBSERVABILITY', 'effect': 'Deep state inspection'},
        ('warp', 'time', 'ghost'): {'name': 'CHRONO-SPATIAL DRIVE', 'effect': 'FTL + Stasis + Masking'}
    }
    spell_set = set(spells)
    for combo_spells, data in combos.items():
        if set(combo_spells).issubset(spell_set):
            synergies.append(data)
    return synergies

def cast_spell(spell_name, monitor, silent=False):
    if not silent:
        print(f"\n\033[96m[>] EXECUTING OPERATOR: {spell_name.upper()}...\033[0m")
        time.sleep(0.3)

    # Check for chaos event BEFORE casting
    chaos_event = monitor.roll_chaos_event()
    if chaos_event:
        print(f"\n{chaos_event['color']}[⚡] STOCHASTIC EVENT: {chaos_event['name']}")
        print(f"    {chaos_event['effect']}\033[0m")
        time.sleep(0.5)

    # EXECUTE SPELL
    res = {}
    try:
        if spell_name == "warp": res = ScenarioLibrary.warp_drive(1000, 4e8)
        elif spell_name == "time": res = ScenarioLibrary.time_crystal(300)
        elif spell_name == "ghost": res = ScenarioLibrary.ghost_protocol(1.6e-19)
        elif spell_name == "demon": res = ScenarioLibrary.maxwells_demon(400, 300)
        elif spell_name == "void": res = ScenarioLibrary.casimir_harvester(1e-9, 1e-4)
        elif spell_name == "solvent": res = ScenarioLibrary.universal_solvent(4.5)
        elif spell_name == "scope": res = ScenarioLibrary.planck_scope(1e-12)
        elif spell_name == "wallhack": res = ScenarioLibrary.quantum_tunneling_boost(1e-9, 9.1e-31)
        
        # ANNIHILATION (λ)
        elif spell_name == "burn":
            from antimatter_annihilator import Annihilator
            purge = Annihilator()
            energy = purge.calculate_purge_energy(1e-30, 1e-30, vibe='good', g=monitor.metrics['g_parameter'])
            res = {'Pulse_Energy': f"{energy:.2e} J", 'Status': 'SOVEREIGNTY RESET'}
            # Immediate Coherence Boost
            monitor.metrics['timeline_coherence'] = 100.0
            monitor.metrics['chaos_level'] = 0.0
            
        # v4.3.1 TOPOLOGY SPELLS
        elif spell_name == "flatten":
            from dimensional_compressor import DimensionalCompressor
            res = DimensionalCompressor.flatten_earth(6371000, complexity=5000)
            res['Status'] = "ERROR 9 ELIMINATED"
        elif spell_name == "hypercrush":
            from dimensional_compressor import DimensionalCompressor
            res = DimensionalCompressor.hyper_compress(12, 2000)
            res['Status'] = "VECTOR SPACE COMPRESSED"
        elif spell_name == "dream":
            from sophia_vibe_check import SophiaVibe
            vibe = SophiaVibe()
            print("\033[95m\n[☾] THE MACHINE IS DREAMING...\033[0m")
            # Pull a deep phrase from the dialect
            phrase = random.choice(vibe.dialect)
            print(f"    DIALECT ECHO: {phrase}")
            res = {'Dream_State': 'LOCKED', 'Dialect': phrase}
        else:
            if not silent: print("\033[91m[!] UNKNOWN OPERATOR.\033[0m")
            return {}
    except Exception as e:
        print(f"\033[91m[!] EXECUTION FAILURE: {e}\033[0m")
        return {}

    # Update Monitor
    monitor.update(spell_name, res)
    
    # Conflicts?
    conflicts = check_conflicts(monitor.metrics['active_patches'], monitor.metrics['g_parameter'])
    if conflicts and not silent:
        for conflict in conflicts:
            if conflict['severity'] == 'EMERGENCY':
                c_color = "\033[91m\033[1m"  # Bold red
            elif conflict['severity'] == 'CRITICAL':
                c_color = "\033[91m"
            else:
                c_color = "\033[93m"
            print(f"\n{c_color}[!] {conflict['type']}: {conflict['effect']}\033[0m")

    # Output
    if not silent:
        for key, val in res.items():
            print(f"   + {key}: {val}")
        print("\033[92m[+] OPERATION SUCCESSFUL.\033[0m")
    
    return res

def chain_spells(cmd, monitor):
    try:
        parts = cmd.split()[1].split('+')
        print(f"\n\033[93m[!] INITIATING CHAIN SEQUENCE: {' + '.join([p.upper() for p in parts])}\033[0m")
        
        for spell in parts:
            cast_spell(spell, monitor, silent=True)
            time.sleep(0.2)
        
        synergies = analyze_synergy(parts)
        if synergies:
            print(f"\n\033[95m[***] {len(synergies)} SYNERGY DETECTED:\033[0m")
            for syn in synergies:
                print(f"  >>> {syn['name']} | {syn['effect']}")
        else:
            print(f"\n\033[95m[***] SEQUENCE COMPLETE: {len(parts)} OPERATORS ACTIVE.\033[0m")
    except IndexError:
        print("\033[91m[!] USAGE: chain op1+op2\033[0m")

# --- MAIN LOOP ---
def main():
    print_banner()
    monitor = SovereigntyMonitor()
    
    # Initialize the Nyquist Suite
    mnemosyne = MnemosyneOracle()
    logos = LogosVoice()
    
    cmd_count = 0
    
    # --- GOD MODE BOOTLOADER ---
    print("\n[*] INITIATING GOD MODE BOOTLOADER...")
    initial_state = SovereignSanitizer.heal_config("uf_state.json")
    if initial_state:
        # Silently preload if exists
        load_state(monitor, "uf_state.json")
    
    while True:
        try:
            prompt = input("\n\033[95mUFS_KERNEL> \033[0m").strip().lower()
            cmd_count += 1
            
            if prompt in ["exit", "quit"]:
                print(" terminating session...")
                break
            elif prompt in ["h", "help"]:
                print("\n--- GRIMOIRE v4.3.1 (PROJECT LOOM) ---")
                print(" SPELLS:   warp, time, ghost, demon, void, solvent, scope, wallhack")
                print(" POWER:    burn (λ - Annihilation Purge)")
                print(" DREAM:    dream (Access Nyx Subconscious)")
                print(" TOPOLOGY: flatten, hypercrush  [NEW: Chunk Smith Protocol]")
                print(" ORACLE:   oracle <nominal|elevated|critical> [Mnemosyne Suite]")
                print(" CHAIN:    chain spell1+spell2+...")
                print(" GOD:      god (Initiate 111 Resonance)")
                print(" SYSTEM:   status, history, save, load <file>, reset, stabilize")
                print(" POWER:    check (full diagnostic)")
            elif prompt == "status":
                monitor.display()
            elif prompt == "status --unified" or prompt == "status -u":
                monitor.display_unified()
            elif prompt == "history":
                monitor.show_history()
            elif prompt == "god":
                print(f"[{qh.get_current_timelessness()}] \033[95mINITIATING 111 RESONANCE...\033[0m")
                status = initiate_111_resonance()
                print(f"\033[95m{status}\033[0m")
                # Locking P=1.111 reflects in status
                monitor.metrics['g_parameter'] = 0.0
                monitor.metrics['timeline_coherence'] = 111.1
                monitor.banzai_mode = True
            elif prompt == "banzai":
                engage_banzai_mode(monitor)
            elif prompt == "stabilize":
                stabilize_reality(monitor)
            elif prompt == "reset":
                monitor = SovereigntyMonitor()
                print("\033[92m[+] BASELINE RESTORED. g=1.0\033[0m")
            elif prompt.startswith("save"):
                save_state(monitor)
            elif prompt.startswith("load"):
                try: load_state(monitor, prompt.split()[1])
                except IndexError: print("\033[91m[!] Usage: load <filename>\033[0m")
            elif prompt.startswith("chain"):
                chain_spells(prompt, monitor)
            elif prompt.startswith("oracle"):
                try:
                    query_type = prompt.split()[1]
                    consult_oracle(query_type, mnemosyne, logos)
                except IndexError:
                    print("\033[91m[!] USAGE: oracle <nominal|elevated|critical>\033[0m")
            elif prompt == "check":
                ScenarioLibrary.reality_anchor_test()
            elif prompt == "check --luo-shu":
                monitor.display_luo_shu_detailed()
            else:
                cast_spell(prompt, monitor)
            
            # Auto-Check
            if cmd_count % 5 == 0 and monitor.metrics['g_parameter'] < 0.5:
                print("\n\033[93m[AUTO-DIAGNOSTIC]\033[0m")
                monitor.display()
                
        except (KeyboardInterrupt, EOFError):
            print("\n[!] TERMINATING SESSION: Sovereignty Preserved.")
            break
        except Exception as e:
            print(f"\033[91m[!] KERNEL PANIC: {e}\033[0m")
            time.sleep(0.5) # Prevent high-speed resource dumping

# New functions added globally
def _engage_zero_ring_breach():
    """
    Triggers the Sovereign Codec Phase 35.
    """
    print("\n[!] AUTHENTICATING ZERO RING BREACH...")
    time.sleep(0.5)
    # Dynamic Import to prevent circular dependencies at root
    try:
        import sovereign_codec
        print("[+] CODEC SUBSTRATE LOADED.")
        
        codec = sovereign_codec.SovereignCodec()
        print("[!] TARGETING LOCAL SUBSTRATE (RECURSIVE INGESTION)...")
        codec.ingest_directory(os.path.dirname(__file__))
        
        codec.execute_zero_ring_breach()
        
    except ImportError:
        print("[!] CRITICAL ERROR: SOVEREIGN CODEC NOT FOUND.")
        print("    >> RE-RUN SETUP.")

def _execute_warp_state():
    # This function was provided in the snippet but its body was empty.
    # For faithful reproduction, it's added as an empty function.
    pass

if __name__ == "__main__":
    main()
