import os
from pathlib import Path

# Cria a pasta docs se não existir
Path("docs").mkdir(exist_ok=True)

# Conteúdo do guia
conteudo =  """# ⚙️ Guia de Configuração de Handoffs

Este documento demonstra como inicializar a rede neural do **AtendentePro**.

## 1. Configuração Completa (Padrão) ✅
Ideal para ambientes de produção.


from pathlib import Path
from atendentepro import create_standard_network

network = create_standard_network(
    templates_root=Path("./client_templates/meu_cliente"),
    client="config",
    include_escalation=True,
    include_feedback=True
)
network = create_standard_network(
    client="config",
    include_escalation=False,
    include_feedback=False
)"""