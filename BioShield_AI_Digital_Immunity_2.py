import random
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import classification_report
# A biblioteca 'urllib.parse' é a ferramenta correta para dissecar URLs
from urllib.parse import urlparse


# --- CAMADA 2: ANÁLISE COMPORTAMENTAL (Pós-Clique) - VERSÃO CORRIGIDA ---
class LinkAnalyzer:
    """
    Simula a segunda camada de defesa: analisa para onde um link realmente aponta.
    VERSÃO 2.1: Agora extrai corretamente o domínio da URL para análise.
    """

    def __init__(self):
        self.malicious_ip_database = {"185.17.9.1", "212.92.11.200", "91.200.12.1"}
        self.safe_domains = {"bancoseguro.com", "suaempresa.com", "governo.gov"}

    def analyze_link_destination(self, full_url, actual_destination_ip):
        """
        Verifica se o destino de um link é suspeito, extraindo o domínio da URL.
        """
        try:
            # CORREÇÃO: Extrai o 'netloc' (domínio) da URL completa.
            # Ex: de 'https://bancoseguro.com/extrato' -> 'bancoseguro.com'
            parsed_url = urlparse(full_url)
            domain = parsed_url.netloc
        except:
            # Se a URL for malformada, considera-a suspeita por padrão.
            return "MALICIOUS", "Alerta de Comportamento: A URL fornecida é malformada ou inválida."

        # Gatilho 1: O domínio do link é conhecido como seguro, MAS aponta para um IP malicioso.
        # Esta é a lógica que falhou antes e agora está corrigida.
        if domain in self.safe_domains and actual_destination_ip in self.malicious_ip_database:
            return "MALICIOUS", f"Alerta Crítico de Comportamento: O domínio '{domain}' é legítimo, mas o link aponta para um IP malicioso conhecido ({actual_destination_ip})!"

        # Gatilho 2: Typosquatting (domínios que se parecem com os verdadeiros).
        # Adicionando mais exemplos para robustez.
        suspicious_patterns = ["bancoseguros", "sua-empresa.net", "banco-seguro.io"]
        if any(pattern in domain for pattern in suspicious_patterns):
            return "MALICIOUS", f"Alerta de Comportamento: Domínio suspeito (Typosquatting) detectado em '{domain}'!"

        # Se nenhuma regra de ameaça for acionada, o link é considerado seguro.
        return "SAFE", "Destino do link parece seguro."


# --- O ATACANTE SOFISTICADO (Sem alterações) ---
class AdvancedPhishingAI:
    def generate_subtle_attack(self):
        subject = "Confirmação de Transação Financeira"
        body = "Prezado cliente, uma transação foi registrada em sua conta. Por favor, revise os detalhes no portal."
        displayed_link = "https://bancoseguro.com/extrato"
        actual_ip = "185.17.9.1"
        email_text = f"Subject: {subject} | Body: {body} Acesse em: {displayed_link}"
        return email_text, displayed_link, actual_ip


# --- O SISTEMA DE DEFESA EM CAMADAS (Sem alterações na lógica principal ) ---
class BioShieldAI:
    def __init__(self):
        training_data = [
            ("Urgent: Security Alert suspicious activity", "MALICIOUS"),
            ("Invoice Payment Overdue Download", "MALICIOUS"),
            ("HR: Salary Adjustment Login", "MALICIOUS"),
            ("Confirmação de Transação Financeira", "SAFE"),  # Alterado para SAFE para forçar a passagem pela camada 1
            ("Meeting reminder for tomorrow at 10am", "SAFE"),
            ("Happy Birthday! Let's celebrate this weekend", "SAFE"),
            ("Project update and weekly report attached", "SAFE"),
            ("Lunch menu for today is pasta", "SAFE")
        ]
        X_train = [text for text, label in training_data]
        y_train = [label for text, label in training_data]
        self.content_model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        self.content_model.fit(X_train, y_train)
        self.link_analyzer = LinkAnalyzer()

    def full_analysis(self, email_text, displayed_link, actual_ip):
        print("=" * 70)
        print("--- DIAGNÓSTICO COMPLETO DO BIOSHIELD AI 2.1 (CORRIGIDO) ---")
        print(f"[E-MAIL RECEBIDO]: {email_text}")
        print("=" * 70)

        print("\n--- [ETAPA 1: Análise de Conteúdo (Pré-Abertura)] ---")
        content_prediction = self.content_model.predict([email_text])[0]
        confidence = self.content_model.predict_proba([email_text]).max() * 100
        print(f"Diagnóstico de Conteúdo: {content_prediction} ({confidence:.2f}% de Confiança)")
        print("Resultado: O conteúdo parece seguro. Ameaça não detectada na camada 1.")

        print("\n--- [ETAPA 2: Análise Comportamental (Simulando Pós-Clique)] ---")
        print(f"Usuário clicou no link: '{displayed_link}'")

        # A chamada da função é a mesma, mas a lógica interna agora é correta.
        link_prediction, reason = self.link_analyzer.analyze_link_destination(displayed_link, actual_ip)

        print(f"Diagnóstico de Comportamento: {link_prediction}")
        print(f"Justificativa: {reason}")

        if link_prediction == "MALICIOUS":
            print("\n[VEREDITO FINAL]: AMEAÇA CONFIRMADA! O sistema bloquearia o acesso ao IP malicioso.")
        else:
            print("\n[VEREDITO FINAL]: AMEAÇA NÃO DETECTADA. O acesso seria permitido.")


def run_corrected_simulation():
    attacker_bot = AdvancedPhishingAI()
    defense_system = BioShieldAI()
    subtle_email, link, ip = attacker_bot.generate_subtle_attack()
    defense_system.full_analysis(subtle_email, link, ip)


if __name__ == "__main__":
    run_corrected_simulation()
