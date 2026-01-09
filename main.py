import asyncio
import os
import random
from dotenv import load_dotenv

load_dotenv()

configure_application_insights(
    connection_string=os.getenv("AZURE_CONNECTION_STRING")
)
class Cor:
    AZUL = '\033[94m'
    VERDE = '\033[92m'
    AMARELO = '\033[93m'
    VERMELHO = '\033[91m'
    RESET = '\033[0m'
    NEG = '\033[1m'

async def main():
    print(f"\n{Cor.NEG}{'='*60}{Cor.RESET}")
    print(f"{Cor.AZUL}🚀 ATENDENTE PRO - SIMULADOR DE ARQUITETURA v0.5.0{Cor.RESET}")
    print(f"{Cor.NEG}{'='*60}{Cor.RESET}")
    print("Baseado em: https://pypi.org/project/atendentepro/")
    print("Status: MODO OFFLINE (Simulação de Inteligência)\n")

    print(f"{Cor.VERDE}✅ Rede Neural Carregada: Triage, Flow, Usage, Knowledge, Escalation, Feedback.{Cor.RESET}")
    print("💬 Digite sua mensagem para testar o roteamento (ou 'sair').\n")

    history = []
    
    while True:
       
        user_input = input(f"{Cor.NEG}👤 Você:{Cor.RESET} ")
        
        if user_input.lower() in ["sair", "exit"]:
            print(f"\n{Cor.VERMELHO}👋 Encerrando sessão.{Cor.RESET}")
            break

        print(f"{Cor.AMARELO}⚙️  Processando Triage...{Cor.RESET}", end="", flush=True)
        await asyncio.sleep(1.5) 
        print(f"\r{' '*30}\r", end="", flush=True) 

        msg = user_input.lower()
        agente_ativo = ""
        resposta = ""

        if any(x in msg for x in ["humano", "atendente", "pessoa", "falar com gente"]):
            agente_ativo = "ESCALATION AGENT"
            resposta = "Entendi que você precisa de ajuda humana. Estou transferindo seu chat para a fila prioritária. Um atendente entrará em contato em até 2 minutos."
        
        elif any(x in msg for x in ["reclama", "sugest", "ruim", "elogio", "não gostei"]):
            agente_ativo = "FEEDBACK AGENT"
            protocolo = random.randint(10000, 99999)
            resposta = f"Sinto muito que sua experiência não tenha sido ideal. Registrei sua mensagem no ticket #{protocolo}. Nossa equipe de qualidade analisará hoje."

        elif any(x in msg for x in ["cadastro", "criar conta", "inscrever", "entrar"]):
            agente_ativo = "ONBOARDING AGENT"
            resposta = "Bem-vindo! Para iniciar seu cadastro no sistema Aura, preciso que você me informe seu e-mail principal."

        elif any(x in msg for x in ["como usa", "ajuda", "o que faz", "funciona"]):
            agente_ativo = "USAGE AGENT"
            resposta = "O AtendentePro é um sistema modular. Você pode me pedir para comprar itens, tirar dúvidas técnicas ou falar com o suporte."

        elif any(x in msg for x in ["erro", "bug", "falha", "não abre", "travou"]):
            agente_ativo = "KNOWLEDGE AGENT"
            resposta = "Parece um problema técnico. Tente limpar o cache do seu navegador (Ctrl+F5). Se o erro persistir, me avise para abrir um chamado."

        else:
            agente_ativo = "FLOW AGENT"
            resposta = "Olá! Sou o assistente virtual. Posso te ajudar com:\n   1. Cadastro\n   2. Suporte Técnico\n   3. Falar com Humano\n   Como posso ser útil?"

        print(f"{Cor.AZUL}🤖 [{agente_ativo}]:{Cor.RESET} {resposta}\n")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n👋 Encerrado.")