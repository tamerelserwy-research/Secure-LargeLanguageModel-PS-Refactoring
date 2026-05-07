from typing import Tuple, Dict, List
from .ast_validator import validate_ast

class MultiLayerValidator:
    def validate(self, generated_code: str, source_code: str, test_cases: List[Dict]) -> Tuple[str, List[str]]:
        report = []
        compliant = True
        
        # Layer 1: Static AST
        status, vulns = validate_ast(generated_code)
        if status == "FAIL":
            compliant = False
            report.extend(vulns)
            
        # Layer 2: Pattern & Semantic (simplified)
        if len(vulns) > 0:
            report.append("NEW_VULNERABILITY_INTRODUCED")
            compliant = False
            
        # Layer 3: Sandboxed Execution (mock)
        for tc in test_cases:
            if tc.get("expected_behavior") not in generated_code.lower():
                report.append("FUNCTIONAL_INCORRECTNESS")
                compliant = False
                break
                
        # Layer 4: Semantic Preservation (CodeBLEU mock)
        sim = self._mock_codebleu(source_code, generated_code)
        if sim < 0.5:
            report.append("SEMANTIC_DRIFT")
            
        return "COMPLIANT" if compliant else "NON_COMPLIANT", report

    def _mock_codebleu(self, src: str, gen: str) -> float:
        # Placeholder for actual CodeBLEU integration
        import difflib
        return difflib.SequenceMatcher(None, src.lower(), gen.lower()).ratio()