# (Algorithm 1 - Implementation)

import re
from typing import Tuple

CRITICAL_PATTERNS = {"invoke-expression", "iex", "invoke-mimikatz", "downloadstring", "encodedcommand"}
HIGH_PATTERNS = {"executionpolicy bypass", "token manipulation", "rid hijacking"}
MED_PATTERNS = {"windowstyle hidden", "registry set", "new-scheduledtask"}

def normalize_and_deobfuscate(cmd: str) -> str:
    cmd = cmd.lower()
    cmd = re.sub(r'\s+', ' ', cmd)
    return cmd

def calculate_risk(cmd: str) -> Tuple[int, str]:
    cmd = normalize_and_deobfuscate(cmd)
    risk = 0
    alert = False
    
    for p in CRITICAL_PATTERNS:
        if p in cmd:
            risk += 3; alert = True
    for p in HIGH_PATTERNS:
        if p in cmd: risk += 2
    for p in MED_PATTERNS:
        if p in cmd: risk += 1
            
    return min(risk, 10), "CRITICAL_ALERT" if alert and risk >= 5 else "NORMAL"
