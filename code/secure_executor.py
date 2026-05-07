# (Algorithm 4 - Implementation)
import subprocess
import shlex
import logging
from typing import Tuple

logger = logging.getLogger(__name__)

def execute_securely(ps_cmd: str, context: str = "DEFAULT") -> Tuple[int, str, str]:
    args = shlex.split(ps_cmd)
    safe_args = ["pwsh", "-NoProfile", "-NonInteractive", "-Command"] + args
    
    log_entry = f"[{context}] Executing: {' '.join(safe_args)}"
    logger.info(log_entry)
    
    try:
        proc = subprocess.Popen(safe_args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        out, err = proc.communicate(timeout=30)
        return proc.returncode, out.strip(), log_entry
    except Exception as e:
        logger.error(f"Execution failed: {e}")
        return -1, "", log_entry
