import time
import random
import logging
from collections import defaultdict
from datetime import datetime, timedelta

# --- CONFIGURAÇÃO DO SISTEMA DE DEFESA ---
# Regra: Se tentar logar mais de 5 vezes em 1 segundo, é um robô.
LIMITE_POR_IP = 5
LIMITE_POR_USUARIO = 5  # Nova regra: Uma conta não pode receber muitos logins
JANELA_TEMPO_SEGUNDOS = 1

# --- CONFIGURAÇÃO DE LOGGING ---
# Configura o logger para registrar mensagens em um arquivo e no console
logging.basicConfig(
    level=logging.INFO,  # Nível mínimo de mensagens a serem registradas (INFO, WARNING, ERROR, DEBUG)
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("sentinela_defesa.log"),  # Salva logs em um arquivo
        logging.StreamHandler()  # Exibe logs no console
    ]
)


class SentinelaAvancado:
    def __init__(self):
        self.logs_ip = defaultdict(list)
        self.logs_usuario = defaultdict(list)
        self.bloqueados = set()
        logging.info("Sentinela Avancado inicializado. Monitoramento ativo.")

    def registrar_acesso(self, ip: str, usuario: str) -> bool:
        try:
            if not isinstance(ip, str) or not isinstance(usuario, str):
                raise ValueError("IP e Usuário devem ser strings.")

            if ip in self.bloqueados:
                logging.warning(
                    f"🚫 [BLOQUEADO] IP {ip} já está na lista negra. Tentativa de acesso para {usuario} recusada.")
                return False

            agora = datetime.now()

            # 1. Ingestão de Dados (Cruzamento de Informações)
            self.logs_ip[ip].append(agora)
            self.logs_usuario[usuario].append(agora)

            # 2. Análise Híbrida
            if self._analisar_ip(ip, agora) and self._analisar_alvo(usuario, agora):
                logging.info(f"✅ Acesso permitido para {usuario} via {ip}")
                return True
            else:
                # Se falhar em qualquer análise, bloqueia
                logging.error(f"🚨 [DETECÇÃO DE ENXAME] Bloqueando IP {ip} por ataque coordenado! Usuário: {usuario}")
                self.bloqueados.add(ip)
                return False
        except ValueError as e:
            logging.error(f"Erro ao registrar acesso: {e}. IP: {ip}, Usuário: {usuario}")
            return False
        except Exception as e:
            logging.critical(f"Erro inesperado no Sentinela: {e}. IP: {ip}, Usuário: {usuario}")
            return False

    def _analisar_ip(self, ip: str, hora_atual: datetime) -> bool:
        historico = self.logs_ip[ip]
        # Filtra apenas os acessos ocorridos na janela de tempo
        recentes = [t for t in historico if (hora_atual - t) <= timedelta(seconds=JANELA_TEMPO_SEGUNDOS)]

        if len(recentes) > LIMITE_POR_IP:
            logging.warning(
                f"   ⚠️ ALERTA: IP {ip} excedeu o limite de requisições ({len(recentes)} em {JANELA_TEMPO_SEGUNDOS}s).")
            return False
        return True

    def _analisar_alvo(self, usuario: str, hora_atual: datetime) -> bool:
        historico = self.logs_usuario[usuario]
        recentes = [t for t in historico if (hora_atual - t) <= timedelta(seconds=JANELA_TEMPO_SEGUNDOS)]

        if len(recentes) > LIMITE_POR_USUARIO:
            logging.warning(
                f"   ⚠️ ALERTA: A conta '{usuario}' está sob ataque massivo! ({len(recentes)} em {JANELA_TEMPO_SEGUNDOS}s).")
            return False
        return True


# --- SIMULAÇÃO DA BATALHA ---

if __name__ == "__main__":
    sistema = SentinelaAvancado()

    logging.info("\n--- 🟢 MONITORAMENTO ATIVADO (Sua defesa está online) ---\n")

    # CENA 1: O Aluno (Você) acessando devagar
    ip_aluno = "192.168.0.1"
    logging.info(f"👤 Usuário Humano tentando logar pelo IP {ip_aluno}...")
    for i in range(3):
        sistema.registrar_acesso(ip_aluno, "Aluno_PUC")
        time.sleep(1)  # Espera 1 segundo (comportamento humano)

    logging.info("\n--- ⚠️ INÍCIO DO ATAQUE DE ENXAME (IA MALICIOSA) ---\n")

    # CENA 2: O Robô atacando rápido com IPs rotativos
    logging.info("🤖 Bot de IA iniciando força bruta com IPs rotativos...")
    for i in range(15):
        ip_falso = f"200.1.1.{i}"
        sistema.registrar_acesso(ip_falso, "Admin_Hacker")

    logging.info("\n--- 🛑 RELATÓRIO FINAL ---")
    logging.info(f"Total de IPs Banidos: {len(sistema.bloqueados)}")

    # Exemplo de acesso com IP já bloqueado
    logging.info("\n--- Tentativa de acesso de IP já bloqueado ---")
    sistema.registrar_acesso("200.1.1.5", "Admin_Hacker")

    # Exemplo de entrada inválida
    logging.info("\n--- Tentativa de acesso com entrada inválida ---")
    sistema.registrar_acesso(123, "usuario_teste")  # Isso vai gerar um erro no log


