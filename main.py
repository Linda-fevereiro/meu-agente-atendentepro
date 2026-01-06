import asyncio
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
        user_input = input("\n👤 Você: ")
        if user_input.lower() in ["sair", "exit"]:
            break
        history.append({"role": "user", "content": user_input})
        result = await Runner.run(network.triage, history)
        print(f"🤖 Bot: {result.final_output}")
        history.append({"role": "assistant", "content": result.final_output})

if __name__ == "__main__":
    asyncio.run(main())