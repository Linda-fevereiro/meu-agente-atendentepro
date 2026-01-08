import asyncio
import os
from pathlib import Path
from dotenv import load_dotenv

# Importamos a biblioteca padrão da OpenAI (que sabemos que você tem)
from openai import AsyncAzureOpenAI
# Importamos a sua configuração de agentes
from atendentepro import create_standard_network

# Carrega senhas
load_dotenv()

async def main():
    print("☁️  Iniciando Sistema (Modo Direto Azure)...")

    # 1. Configurar a Conexão com a Microsoft
    try:
        client_azure = AsyncAzureOpenAI(
            api_key=os.getenv("AZURE_OPENAI_API_KEY"),
            api_version=os.getenv("OPENAI_API_VERSION"),
            azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT")
        )
        deploy_name = os.getenv("AZURE_DEPLOYMENT_NAME")
    except Exception as e:
        print(f"❌ Erro de Configuração: {e}")
        return

    # 2. Carregar o Cérebro do Agente (Suas regras YAML)
    print("🧠 Carregando regras de negócio...")
    network = create_standard_network(
        templates_root=Path("./client_templates"),
        client="meu_cliente"
    )
    
    # Pegamos o Agente de Triagem (o recepcionista)
    agente = network.triage
    
    # Extraímos as instruções dele (O Prompt do Sistema)
    # Se for uma função, executamos. Se for texto, usamos direto.
    instrucoes_sistema = agente.instructions
    if callable(instrucoes_sistema):
        instrucoes_sistema = instrucoes_sistema({}) # Executa para pegar o texto

    print(f"✅ Conectado na Azure! (Deploy: {deploy_name})")
    print(f"🤖 Agente Ativo: {agente.name}")
    print("💬 Digite 'sair' para encerrar.\n")

    # 3. Histórico da Conversa
    # Começamos ensinando o robô quem ele é (System Message)
    messages = [
        {"role": "system", "content": instrucoes_sistema}
    ]

    # 4. Loop de Conversa
    while True:
        user_input = input("👤 Você: ")
        if user_input.lower() in ["sair", "exit"]:
            break
            
        # Adiciona sua fala ao histórico
        messages.append({"role": "user", "content": user_input})

        try:
            # Envia para a Azure processar
            response = await client_azure.chat.completions.create(
                model=deploy_name,
                messages=messages,
                temperature=0.7
            )
            
            # Pega a resposta do robô
            bot_reply = response.choices[0].message.content
            print(f"🤖 Bot: {bot_reply}\n")
            
            # Guarda a resposta no histórico para ele lembrar do contexto
            messages.append({"role": "assistant", "content": bot_reply})

        except Exception as e:
            print(f"❌ Erro na Azure: {e}")
            print("Dica: Verifique se o 'AZURE_DEPLOYMENT_NAME' no .env está igualzinho ao site da Azure.")

if __name__ == "__main__":
    asyncio.run(main())