# Automated Security-Centric Refactoring of PowerShell Commands Using Large Language Models

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20040419.svg)](https://doi.org/10.5281/zenodo.20040419)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


A Python-based framework for cross-language automation that refactors insecure PowerShell commands into secure, parameterized equivalents using Retrieval-Augmented Generation (RAG) and multi-layer validation.

## 📊 Dataset
- **Size:** 8,886 labeled commands → 7,719 unique patterns after deduplication
- **Mapping:** 10 MITRE ATT&CK tactics
- **Source:** Zenodo DOI: `10.5281/zenodo.20040419` | GitHub Sync: `data/`

## 🛠️ Setup
```bash
git clone https://github.com/your-org/Secure-LargeLanguageModel-PS-Refactoring.git
cd Secure-LargeLanguageModel-PS-Refactoring
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
