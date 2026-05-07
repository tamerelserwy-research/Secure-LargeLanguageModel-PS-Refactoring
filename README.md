# Automated Security-Centric Refactoring of PowerShell Commands Using Large Language Models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20040419.svg)](https://doi.org/10.5281/zenodo.20040419)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A Python-based framework for cross-language automation that refactors insecure PowerShell commands into secure, parameterized equivalents using Retrieval-Augmented Generation (RAG) and multi-layer validation.
## 📁 Repository Structure
```txt
Secure-LargeLanguageModel-PS-Refactoring/
├── README.md
├── requirements.txt
├── colab_reproduction.ipynb
├── code/
│   ├── __init__.py
│   ├── spotlighting.py
│   ├── risk_profiler.py
│   ├── rag_retriever.py
│   ├── ast_validator.py
│   ├── stateful_tracker.py
│   ├── multi_layer_validator.py
│   ├── secure_executor.py
│   └── main_pipeline.py
├── tests/
│   ├── __init__.py
│   ├── test_pipeline.py
│   └── adversarial_cases.json
└── data/
    └── README.md (points to Zenodo/GitHub dataset)
```

## 📊 Dataset
- **Size:** 8,886 labeled commands → 7,719 unique patterns after deduplication
- **Mapping:** 10 MITRE ATT&CK tactics
- **Source:** Zenodo DOI: `10.5281/zenodo.20040419` | GitHub Sync: `data/dataset_with_mitre.json`

## 🛠️ Setup
```bash
git clone https://github.com/your-org/Secure-LargeLanguageModel-PS-Refactoring.git
cd Secure-LargeLanguageModel-PS-Refactoring
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```
## 🚀 Reproduction
Run the complete pipeline and reproduce Table 4 & 5 results:
```bash
python -m code.main_pipeline --mode evaluate --cv_folds 5
```

Adversarial robustness test (Atomic Red Team, PyRIT, Garak):
```bash
pytest tests/test_pipeline.py::test_adversarial_robustness -v
```
## 🚀 Deployment Instructions
### 1- Clone & Setup:
```bash
git clone <repo-url>
cd Secure-LargeLanguageModel-PS-Refactoring
pip install -r requirements.txt
```
### 2- Run Tests
```bash
pytest tests/ -v
```
### 3- Run Colab
Upload `colab_reproduction.ipynb` to Google Colab, set `OPENAI_API_KEY`, and run sequentially.

### 4- Full Reproduction
Replace placeholders in `code/main_pipeline.py` and `code/rag_retriever.py` with fine-tuned 7B model weights and FAISS index.
```bash
python -m code.main_pipeline --mode evaluate
```

## 📜 Citation
```bibtex
@article{elserwy2025secureps,
  title={Automated Security-Centric Refactoring of PowerShell Commands Using Large Language Models: A Python-Based Framework for Cross-Language Automation},
  author={Authors},
  journal={Egyptian Informatics Journal Preprint},
  year={2026}
}
```

