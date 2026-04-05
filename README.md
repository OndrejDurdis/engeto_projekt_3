# engeto_projekt_3
Třetí projekt pro Engeto Akademii - Tři automatizované testy


# Automatizované testy pro Engeto.cz

Tento projekt obsahuje automatizované UI testy pro webovou stránku [engeto.cz](https://www.engeto.cz/) napsané pomocí **Playwright** + **pytest**.

# Použité technologie
- Python 3
- Playwright
- pytest
- pytest-playwright


## Spuštění testů

### 1. Instalace závislostí
bash

pip install pytest pytest-playwright
playwright install

### 2. Spuštění všech testů

pytest test_engeto.py -v
