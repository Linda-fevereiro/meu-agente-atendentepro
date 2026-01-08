# 🤖 Projeto AtendentePro - Arquitetura Multi-Agentes (v0.6.1)

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/iaragomes-dev/meu-agente-atendentepro)

Este projeto implementa a arquitetura de atendimento inteligente baseada na biblioteca **AtendentePro**.

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
Veja o arquivo [DEMONSTRACAO.md](DEMONSTRACAO.md) para visualizar os logs de execução e os cenários de teste validados.

## 🚀 Como Rodar (Localmente)
```bash
# 1. Instalar dependências
pip install -r requirements.txt

# 2. Executar o simulador
python main.py