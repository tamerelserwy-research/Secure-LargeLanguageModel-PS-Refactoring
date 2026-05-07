import re
from typing import Tuple, Set

def validate_ast(powershell_code: str) -> Tuple[str, Set[str]]:
    code = powershell_code.lower()
    vulns = set()
    
    if re.search(r'invoke[-\s]?expression|iex', code):
        if re.search(r'(\$[a-z_]|args|\$\{)', code):
            vulns.add("CWE-94: Code Injection Risk")
            
    if re.search(r'downloadstring|invoke-restmethod', code):
        if not re.search(r'get-filehash|verify|hash', code):
            vulns.add("CWE-494: Download of Code Without Integrity Check")
            
    if re.search(r'invoke-command|enter-pssession', code):
        if re.search(r'-computername\s+\$[a-z_]', code):
            vulns.add("CWE-78: OS Command Injection via Remote Execution")
            
    return "FAIL" if vulns else "PASS", vulns