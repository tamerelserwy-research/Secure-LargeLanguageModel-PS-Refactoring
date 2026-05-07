# Main pipeline
import logging
from typing import List, Dict
from .spotlighting import wrap_with_spotlighting
from .risk_profiler import calculate_risk
from .rag_retriever import RAGRetriever
from .multi_layer_validator import MultiLayerValidator
from .secure_executor import execute_securely
from .stateful_tracker import StatefulTracker

logging.basicConfig(level=logging.INFO)

class SecureRefactoringPipeline:
    def __init__(self, llm_model: str = "gpt-4o", rag_enabled: bool = True, cv_folds: int = 1):
        self.llm = llm_model
        self.rag_enabled = rag_enabled
        self.validator = MultiLayerValidator()
        self.tracker = StatefulTracker()
        # Initialize RAG KB from dataset (mock structure)
        self.retriever = RAGRetriever([]) 
        
    def process_command(self, command: str, nl_description: str) -> Dict:
        # 1. Input Isolation
        safe_prompt, injection = wrap_with_spotlighting(command)
        if injection:
            return {"status": "BLOCKED", "reason": "Prompt injection detected"}
            
        # 2. Risk Profiling
        risk, alert = calculate_risk(command)
        
        # 3. RAG Generation (simulated LLM call)
        gen_code = self._generate_secure_variant(command, nl_description)
        
        # 4. Multi-Layer Validation
        status, report = self.validator.validate(gen_code, command, [])
        
        # 5. Secure Execution (if compliant)
        exec_code, out, log = (-1, "", ""), None
        if status == "COMPLIANT":
            exec_code, out, log = execute_securely(gen_code)
            
        return {
            "original": command,
            "refactored": gen_code,
            "risk_score": risk,
            "alert": alert,
            "compliance_status": status,
            "vulnerability_report": report,
            "execution_output": out
        }

    def _generate_secure_variant(self, cmd: str, desc: str) -> str:
        # Placeholder for actual LLM call
        if "invoke-expression" in cmd.lower() or "iex" in cmd.lower():
            return cmd.replace("Invoke-Expression", "").replace("IEX", "").strip()
        if "downloadstring" in cmd.lower():
            return "# SECURE: Replaced with Invoke-RestMethod + Get-FileHash verification"
        return cmd
