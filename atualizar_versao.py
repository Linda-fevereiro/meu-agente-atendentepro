import os
from pathlib import Path

# Conteúdo Profissional do Changelog
novo_changelog = """# Changelog 📝

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [0.5.3] - 2026-01-06
### 📚 Documentação
- **README:** Documentação completa atualizada para padrões PyPI.
- **Estrutura:** Organização final dos arquivos de configuração e exemplos.

## [0.5.0] - 2026-01-06
### Adicionado
- **Arquitetura:** Implementação do roteamento entre Triage, Escalation e Feedback.
- **Simulação:** Script `main.py` com modo de demonstração visual.
- **Docs:** Fluxogramas de navegação e guia de handoffs.

## [0.3.0] - Versão Inicial
- Sistema base de múltiplos agentes.
- Integração preliminar com OpenAI.
"""

# Conteúdo do README atualizado com a versão nova no título
novo_readme = """# 🤖 Projeto AtendentePro - Arquitetura Multi-Agentes (v0.5.3)

Este projeto implementa a arquitetura de atendimento inteligente baseada na biblioteca **AtendentePro**.

O foco desta implementação é demonstrar o **Roteamento Semântico** e a orquestração entre agentes especializados.

## 📦 Versão Atual: 0.5.3
**Status:** Pronta para publicação e testes de integração.

## 🏗️ Arquitetura Implementada

O sistema utiliza um Agente de Triagem (Router) que distribui as mensagens para:

1.  **🚨 Escalation Agent:** Para transbordo humano imediato (Alta Prioridade).
2.  **📝 Feedback Agent:** Para registro de tickets e reclamações.
3.  **📚 Knowledge Agent:** Para suporte técnico e tira-dúvidas.
4.  **👋 Onboarding Agent:** Para novos cadastros.

## 📂 Estrutura do Projeto
- `main.py`: Núcleo da simulação e lógica de roteamento.
- `client_templates/`: Configurações YAML de cada agente (Prompts do Sistema).
- `docs/`: Fluxogramas e documentação técnica.

## 🧪 Evidências de Teste
Veja o arquivo [DEMONSTRACAO.md](DEMONSTRACAO.md) para visualizar os logs de execução.

## 🚀 Como Rodar
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar o simulador
python main.py"""