import os
from pathlib import Path

# Configuração do conteúdo dos arquivos
files = {
    "requirements.txt": """openai>=1.107.1
openai-agents>=0.3.3
atendentepro>=0.5.0
pydantic>=2.0.0
PyYAML>=6.0
python-dotenv>=1.0.0""",

    ".gitignore": """.env
__pycache__/
venv/
.DS_Store""",

    ".env": """ATENDENTEPRO_LICENSE_KEY=ATP_seu-token-aqui
OPENAI_API_KEY=sk-sua-chave-openai-aqui""",

    "README.md": """# Meu Agente AtendentePro v0.5.0
Projeto de atendimento automatizado com Escalation e Feedback.""",

    "main.py": """import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv
from atendentepro import activate, create_standard_network
from agents import Runner

load_dotenv()
activate(os.getenv("ATENDENTEPRO_LICENSE_KEY"))

async def main():
    print("🚀 Iniciando AtendentePro v0.5.0...")
    network = create_standard_network(
        templates_root=Path("./client_templates"),
        client="standard"
    )
    print("✅ Sistema pronto. Digite 'sair' para encerrar.")

    history = []
    while True:
        user_input = input("\\n👤 Você: ")
        if user_input.lower() in ["sair", "exit"]:
            break
        history.append({"role": "user", "content": user_input})
        result = await Runner.run(network.triage, history)
        print(f"🤖 Bot: {result.final_output}")
        history.append({"role": "assistant", "content": result.final_output})

if __name__ == "__main__":
    asyncio.run(main())""",

    "client_templates/standard/triage_config.yaml": """system_prompt: |
  Você é o Agente de Triagem (Triage) v0.5.0.
  Analise a intenção e roteie:
  PRIORIDADE MÁXIMA:
  1. Pediu humano/atendente -> Escalation Agent (Imediato)
  2. Reclamação/Sugestão -> Feedback Agent (Posterior)
  ROTEAMENTO PADRÃO:
  3. Cadastro -> Onboarding Agent
  4. Duvidas de uso -> Usage Agent
  5. Menu/Opções -> Flow Agent
  6. Técnico -> Knowledge Agent
model: gpt-4o
temperature: 0.0""",

    "client_templates/standard/escalation_config.yaml": """system_prompt: |
  Você é o Agente de Transbordo (Escalation).
  Transfira o usuário IMEDIATAMENTE para um humano.
  Não tente resolver. Apenas avise que o humano está chegando.
model: gpt-4o
priority: high""",

    "client_templates/standard/feedback_config.yaml": """system_prompt: |
  Você é o Agente de Feedback.
  Receba o feedback, agradeça e gere um protocolo.
  Avise que a resposta será posterior via e-mail.
model: gpt-4o""",

    "client_templates/standard/usage_config.yaml": "system_prompt: Explique como usar o sistema.\nmodel: gpt-4o",
    "client_templates/standard/onboarding_config.yaml": "system_prompt: Ajude no cadastro inicial.\nmodel: gpt-4o",
    "client_templates/standard/knowledge_config.yaml": "system_prompt: Tire dúvidas técnicas.\nmodel: gpt-4o",
    "client_templates/standard/flow_config.yaml": "system_prompt: Apresente o menu.\nmodel: gpt-4o",
    "client_templates/standard/confirmation_config.yaml": "system_prompt: Valide Sim/Não.\nmodel: gpt-4o-mini",
    "client_templates/standard/interview_config.yaml": "system_prompt: Colete dados (Nome, Email).\nmodel: gpt-4o",
    "client_templates/standard/answer_config.yaml": "system_prompt: Formate a resposta final.\nmodel: gpt-4o",
}

def install():
    print("📦 Iniciando instalação dos arquivos...")
    current_dir = Path.cwd()
    
    for filename, content in files.items():
        # Cria o caminho completo
        file_path = current_dir / filename
        
        # Cria as pastas necessárias se não existirem
        file_path.parent.mkdir(parents=True, exist_ok=True)
        
        # Escreve o arquivo
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Criado: {filename}")

    print("\n🎉 Instalação concluída! Pode apagar este arquivo instalador.py se quiser.")

if __name__ == "__main__":
    install()