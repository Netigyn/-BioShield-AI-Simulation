# 🛡️ AI Cybersecurity Simulation: The Evolution of a Digital Immune System
# 🛡️ Simulação de Cibersegurança com IA: A Evolução de um Sistema Imunológico Digital

**Author / Autor:** Netigyn (Giancarlo)

---

## 🚀 Project Overview / Visão Geral do Projeto

This project simulates the "arms race" in cybersecurity, demonstrating the evolution of an AI-based defense system. We begin with a foundational model (`bioshield_v1.py`) and evolve it into a multi-layered defense system (`bioshield_v2.py`) capable of detecting more sophisticated attacks.

Este projeto simula a "corrida armamentista" em cibersegurança, demonstrando a evolução de um sistema de defesa baseado em IA. Começamos com um modelo fundamental (`bioshield_v1.py`) e o evoluímos para um sistema de defesa em múltiplas camadas (`bioshield_v2.py`), capaz de detectar ataques mais sofisticados.

---

## 🛠️ Setup & How to Run / Instalação e Como Executar

To run these simulations, you need Python 3 and a few libraries. It is highly recommended to use a virtual environment.

Para executar estas simulações, você precisa do Python 3 e de algumas bibliotecas. É altamente recomendado usar um ambiente virtual.

**1. Clone the repository (or download the files):**
```bash
git clone https://github.com/Netigyn/-BioShield-AI-Simulation.git
cd -BioShield-AI-Simulation
```

**2. (Recommended ) Create and activate a virtual environment:**
```bash
# Create the virtual environment
python3 -m venv .venv

# Activate it (on Linux/macOS)
source .venv/bin/activate
```

**3. Install the required libraries:**
As bibliotecas `pandas` e `scikit-learn` são necessárias.
```bash
pip install -r requirements.txt
```
*(This command reads the `requirements.txt` file and installs everything needed).*

**4. Run the desired simulation:**
```bash
# To run the first, simpler version
python bioshield_v1.py

# To run the advanced, multi-layered version
python bioshield_v2.py
```

---

## 🔬 Stage 1: BioShield AI 1.0 - The Initial Vaccine / Estágio 1: BioShield AI 1.0 - A Vacina Inicial

Our first version (`bioshield_v1.py`) simulates a basic AI defense that analyzes email content to detect obvious threats based on keywords associated with urgency and fear.

Nossa primeira versão (`bioshield_v1.py`) simula uma defesa de IA básica que analisa o conteúdo de e-mails para detectar ameaças óbvias com base em palavras-chave associadas à urgência e ao medo.

- **Success:** The model is effective at detecting phishing attempts that use clear, high-urgency keywords.
- **Critical Limitation:** A sophisticated attacker could easily bypass this filter by avoiding obvious keywords. **What if the email looks professional and calm?** This question leads us to Stage 2.

---

## 🧬 Stage 2: BioShield AI 2.1 - The Multi-Layered Immune System / Estágio 2: BioShield AI 2.1 - O Sistema Imunológico em Camadas

The second version (`bioshield_v2.py`) is an advanced, multi-layered defense system. This "Zero Trust" system first analyzes the content and, if it seems safe, proceeds to a second layer to analyze the *behavior* of any links in the email.

A segunda versão (`bioshield_v2.py`) é um sistema de defesa avançado e em múltiplas camadas. Este sistema "Confiança Zero" primeiro analisa o conteúdo e, se ele parecer seguro, prossegue para uma segunda camada que analisa o *comportamento* de qualquer link no e-mail.

- **Success:** The multi-layered system successfully identifies the limitation of content-only analysis. It correctly flags the subtle attack by analyzing the link's behavior.
- **Key Takeaway:** Modern cybersecurity is not about a single perfect filter, but about building resilient, layered defense systems that analyze both **content and behavior**.

---

## 💡 Final Conclusion / Conclusão Final

This project demonstrates the critical evolution from a simple detection model to a sophisticated, multi-layered security strategy. By understanding the limitations of each layer, we can build more robust AI systems capable of adapting to the ever-changing landscape of digital threats.

Este projeto demonstra a evolução crítica de um modelo de detecção simples para uma estratégia de segurança sofisticada e em múltiplas camadas. Ao entender as limitações de cada camada, podemos construir sistemas de IA mais robustos.
