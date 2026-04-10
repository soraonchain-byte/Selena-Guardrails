# File: src/logic/sora_pulse.py
# Framework: SORA PULSE - Architectural Sovereign Coordination for Autonomous Agents

class SoraPulse:
    def __init__(self):
        # THE RESONANCE: Lightweight state management
        self.resonance = {
            "GLOBAL_AUTH": {"pulse": 0, "pointer": None},
            "SELENA_ORACLE": {"pulse": 0, "pointer": None}
        }

    def emit_pulse(self, target_id, pulse_code, data_link=None):
        """
        Changes the state of a specific target in the Resonance.
        Pulse Codes: 0=INERT, 1=TRIGGER, 2=PROCESSING, 3=SUCCESS, 4=RE-SYNC
        """
        if target_id not in self.resonance:
            self.resonance[target_id] = {"pulse": 0, "pointer": None}
            
        self.resonance[target_id]["pulse"] = pulse_code
        self.resonance[target_id]["pointer"] = data_link
        
        status_map = {0: "INERT", 1: "TRIGGER", 2: "PROCESSING", 3: "SUCCESS", 4: "RE-SYNC"}
        status_name = status_map.get(pulse_code, "UNKNOWN")
        print(f"🫀 [PULSE EMITTED] Target: {target_id} | Code: {pulse_code} ({status_name})")

    def sync_reaction(self, agent_id, role_trigger_code):
        """
        Hardcoded logic for Agents to sense the Resonance.
        Returns True if the current pulse matches the trigger code.
        """
        current_state = self.resonance.get(agent_id)
        if not current_state:
            return False

        if current_state["pulse"] == role_trigger_code:
            print(f"⚡ [SYNC-REACTION] {agent_id} detected Pulse {role_trigger_code}. Executing...")
            return True
            
        return False