import time
import random
from collections import defaultdict
from datetime import datetime

# --- CONFIGURAÇÃO DA DEFESA ---
LIMITE_POR_IP = 5
LIMITE_POR_USUARIO = 5  # Nova regra: Uma conta não pode receber muitos logins
JANELA_TEMPO = 1


class SentinelaAvancado:
    def __init__(self):
        # Monitoramos IPs e também os Nomes de Usuário alvo
        self.logs_ip = defaultdict(list)
        self.logs_usuario = defaultdict(list)
        self.bloqueados = set()

    def registrar_acesso(self, ip, usuario):
        if ip in self.bloqueados:
            print(f"🚫 [BLOQUEADO] IP {ip} já está na lista negra.")
            return False

        agora = datetime.now()

        # 1. Ingestão de Dados (Cruzamento de Informações)
        self.logs_ip[ip].append(agora)
        self.logs_usuario[usuario].append(agora)  # Agora rastreamos o alvo também!

        # 2. Análise Híbrida
        if self._analisar_ip(ip, agora) and self._analisar_alvo(usuario, agora):
            print(f"✅ Acesso permitido para {usuario} via {ip}")
            return True
        else:
            # Se falhar em qualquer análise, bloqueia
            print(f"🚨 [DETECÇÃO DE ENXAME] Bloqueando IP {ip} por ataque coordenado!")
            self.bloqueados.add(ip)
            return False

    def _analisar_ip(self, ip, hora_atual):
        # Defesa antiga (Rate Limit por IP)
        historico = self.logs_ip[ip]
        recentes = [t for t in historico if (hora_atual - t).total_seconds() <= JANELA_TEMPO]
        return len(recentes) <= LIMITE_POR_IP

    def _analisar_alvo(self, usuario, hora_atual):
        # NOVA DEFESA (Rate Limit por Usuário)
        # Verifica se a CONTA está sofrendo ataque de múltiplos lugares
        historico = self.logs_usuario[usuario]
        recentes = [t for t in historico if (hora_atual - t).total_seconds() <= JANELA_TEMPO]

        if len(recentes) > LIMITE_POR_USUARIO:
            print(f"   ⚠️ ALERTA: A conta '{usuario}' está sob ataque massivo!")
            return False  # Bloqueia porque a conta está sendo martelada
        return True


# --- SIMULAÇÃO DA BATALHA ---

sistema = SentinelaAvancado()

print("\n--- 🛡️ SENTINELA 2.0 ATIVADO (Monitoramento Híbrido) ---\n")

print("--- 🤖 INICIANDO ATAQUE DE ENXAME (ROTATIVO) ---")
# O mesmo ataque que derrubou a defesa anterior
for i in range(15):
    ip_falso = f"200.1.1.{i}"
    sistema.registrar_acesso(ip_falso, "Admin_Hacker")

print("\n--- 🛑 RELATÓRIO FINAL ---")
print(f"Total de IPs Banidos: {len(sistema.bloqueados)}")