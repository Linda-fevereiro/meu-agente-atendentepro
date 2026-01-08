import os

reqs_content = """annotated-types==0.7.0
anyio==4.9.0
atendentepro==0.6.1
attrs==25.4.0
certifi==2026.1.4
cffi==2.0.0
charset-normalizer==3.4.4
click==8.2.1
colorama==0.4.6
cryptography==46.0.3
distro==1.9.0
fastapi==0.116.1
griffe==1.15.0
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.10
mcp==1.25.0
numpy==2.4.0
openai==2.14.0
pydantic==2.12.5
python-dotenv==1.2.1
PyYAML==6.0.3
requests==2.32.5
scikit-learn==1.8.0
uvicorn==0.35.0
"""

changelog_content = """# Changelog 📝

Todas as mudanças notáveis neste projeto serão documentadas neste arquivo.

## [0.6.1] - 2026-01-08
### 🚀 Melhorias
- **Core:** Atualização da dependência `atendentepro` para v0.6.1.
- **Security:** Correção de codificação no arquivo `requirements.txt`.
- **Docs:** Atualização de links e emblemas de status.

## [0.5.3] - 2026-01-06
### 📚 Documentação
- README atualizado para padrões PyPI.
- Estrutura de arquivos oficializada.

## [0.5.0] - 2026-01-06
### Adicionado
- Arquitetura de roteamento (Triage, Escalation, Feedback).
- Modo de Simulação.
"""

if os.path.exists("README.md"):
    with open("README.md", "r", encoding="utf-8") as f:
        readme_txt = f.read()
    
    readme_txt = readme_txt.replace("v0.5.3", "v0.6.1")
    readme_txt = readme_txt.replace("Versão Implementada: 0.5.3", "Versão Implementada: 0.6.1")
else:
    readme_txt = "# AtendentePro v0.6.1\n\nProjeto atualizado."


print("🔄 Iniciando atualização para v0.6.1...")

with open("requirements.txt", "w", encoding="utf-8") as f:
    f.write(reqs_content)
print("✅ requirements.txt atualizado para atendentepro==0.6.1")

with open("CHANGELOG.md", "w", encoding="utf-8") as f:
    f.write(changelog_content)
print("✅ CHANGELOG.md registrado com sucesso.")

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_txt)
print("✅ README.md atualizado.")

print("\n🚀 Tudo pronto! Agora é só enviar para o GitHub.")