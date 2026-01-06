import os
from pathlib import Path

# Conteúdo reconstruído baseado nos prints
docs_content = {
    # 1. CHANGELOG (Histórico de Versões)
    "CHANGELOG.md": """# Changelog 📝

## [0.5.0] - 2026-01-06 (Versão Atual)
### Adicionado
- **Escalation Agent:** Novo agente focado exclusivamente em transbordo humano imediato.
- **Feedback Agent:** Novo agente para registrar tickets, reclamações e sugestões para resposta posterior.
- **Roteamento Global:** Agora todos os agentes podem redirecionar para Escalation ou Feedback.

## [0.3.0] - Versão Anterior
- Sistema base de múltiplos agentes.
- Triage, Flow, Knowledge, Usage, Onboarding.
""",

    # 2. FLUXOGRAMA (Desenho da Arquitetura)
    "docs/fluxogramas/arquitetura.txt": """
       (Fluxograma Reconstruído da v0.5.0)

                 [ USUÁRIO ]
                      |
                      v
            +-------------------+
            |   TRIAGE (Router) |  -----> Classifica a Intenção
            +-------------------+
                      |
        +-------------+-------------+-------------+
        |             |             |             |
    +-------+     +-------+     +-------+     +-------+
    | FLOW  |     | KNOWL.|     | USAGE |     |ONBOARD|
    +-------+     +-------+     +-------+     +-------+
        |             |             |             |
        +-------------+-------------+-------------+
                      |
        (Qualquer agente pode acionar abaixo)
                      |
          +-------------------------+
          |      AÇÕES GLOBAIS      |
          +-------------------------+
          | 📞 Escalation (Humano)  | ---> Imediato
          | 📝 Feedback (Ticket)    | ---> Posterior
          +-------------------------+
                      |
                      v
            +-------------------+
            |      ANSWER       | ---> Resposta Final
            +-------------------+
""",

    # 3. DOCUMENTAÇÃO GERAL (Manual)
    "docs/MANUAL.md": """# 📖 Manual do AtendentePro v0.5.0

## Instalação
Necessário Python 3.9+ e chave de licença válida.
Instale via: `pip install -r requirements.txt`

## Agentes Disponíveis

| Agente | Função |
|--------|--------|
| **Triage** | O "chefe". Recebe a mensagem e decide para quem mandar. |
| **Escalation** | **(Novo)** Transfere para humano. Prioridade Alta. |
| **Feedback** | **(Novo)** Registra reclamações/sugestões. |
| **Flow** | Apresenta menus e opções de compra. |
| **Knowledge** | Tira dúvidas técnicas (RAG). |
| **Onboarding** | Ajuda no cadastro inicial. |
| **Usage** | Ensina como usar o sistema. |

## Como Rodar
Execute `python main.py` no terminal.
""",

    # 4. EXEMPLOS (Código Extra)
    "examples/ferramenta_customizada.py": """
# Exemplo: Como criar uma ferramenta (Tool) customizada
# Salve isso em client_templates/standard/tools.py se quiser usar.

from agents import tool

@tool
def consultar_status_pedido(id_pedido: str) -> str:
    '''
    Verifica onde está o pedido do cliente.
    Args:
        id_pedido: O código do pedido (ex: PED-123).
    '''
    # Simulação de banco de dados
    if id_pedido == "123":
        return "Seu pedido saiu para entrega hoje!"
    return "Pedido não encontrado."
"""
}

def gerar():
    print("📚 Gerando documentação...")
    root = Path.cwd()
    
    for path_str, content in docs_content.items():
        file_path = root / path_str
        # Cria pastas se não existirem
        file_path.parent.mkdir(parents=True, exist_ok=True)
        # Escreve o arquivo
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"✅ Criado: {path_str}")

if __name__ == "__main__":
    gerar()