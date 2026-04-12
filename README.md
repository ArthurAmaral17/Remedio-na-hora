\# 💊 Remédio na Hora Certa



!\[Versão](https://img.shields.io/badge/versão-1.0.0-blue)

!\[Python](https://img.shields.io/badge/Python-3.10+-yellow)

!\[Licença](https://img.shields.io/badge/licença-MIT-green)

!\[CI Status](https://github.com/ArthurAmaral17/remedio-na-hora/actions/workflows/ci.yml/badge.svg)



\## 📌 Descrição do Problema Real



O esquecimento de horários de medicamentos é uma das principais causas de complicações de saúde em idosos e pessoas com rotinas de tratamento contínuo. Muitos cuidadores familiares também enfrentam dificuldades em gerenciar múltiplas prescrições, resultando em \*\*doses perdidas ou duplicadas\*\* que podem agravar quadros clínicos.



\*\*Quem é afetado?\*\*

\- Idosos que fazem uso de múltiplos medicamentos diários

\- Cuidadores familiares sobrecarregados

\- Pessoas com doenças crônicas (hipertensão, diabetes, etc.)

\- Profissionais de home care



\## 🎯 Proposta da Solução



O \*\*Remédio na Hora Certa\*\* é uma aplicação CLI (Interface de Linha de Comando) com \*\*interface rica e intuitiva\*\* que permite o cadastro, visualização e controle de medicamentos de forma simples e eficiente. A ferramenta foi desenvolvida para ser executada em qualquer terminal, sem necessidade de internet ou hardware especial.



\*\*Público-alvo:\*\* Idosos, cuidadores familiares, profissionais de saúde e qualquer pessoa que necessite de um controle simples e confiável de medicamentos.



\## ⚙️ Funcionalidades Principais



\- ✅ \*\*Cadastro de Medicamentos:\*\* Registre nome e horário de cada remédio

\- 📋 \*\*Listagem Visual:\*\* Tabela formatada com status (Pendente/Tomado)

\- ✔️ \*\*Marcação de Doses:\*\* Confirme quando um medicamento foi administrado

\- 🗑️ \*\*Remoção de Itens:\*\* Exclua medicamentos que não são mais necessários

\- 🎨 \*\*Interface Rica:\*\* Utiliza a biblioteca `Rich` para cores, painéis e tabelas formatadas



\## 🛠️ Tecnologias Utilizadas



| Tecnologia | Finalidade |

| :--- | :--- |

| \*\*Python 3.10+\*\* | Linguagem de programação principal |

| \*\*Rich\*\* | Biblioteca para interface CLI rica (tabelas, cores, painéis) |

| \*\*Pytest\*\* | Framework de testes automatizados |

| \*\*Pylint\*\* | Análise estática de código (qualidade e padronização) |

| \*\*GitHub Actions\*\* | Pipeline de Integração Contínua (CI/CD) |



\## 📂 Estrutura do Projeto

remedio-na-hora/

├── .github/

│ └── workflows/

│ └── ci.yml # Pipeline de CI (Lint + Testes)

├── src/

│ ├── init.py

│ ├── models.py # Classes de domínio (Medicamento)

│ ├── services.py # Lógica de negócio (CRUD)

│ └── cli.py # Interface com Rich (Menu principal)

├── tests/

│ ├── init.py

│ └── test\_services.py # Testes automatizados (5 casos)

├── .gitignore

├── .pylintrc # Configuração do Pylint

├── requirements.txt # Dependências do projeto

├── VERSION # Versionamento semântico

└── README.md


\## 🚀 Instruções de Instalação



\### Pré-requisitos

\- \*\*Python 3.8 ou superior\*\* instalado no sistema

\- \*\*pip\*\* (gerenciador de pacotes do Python)

\- \*\*Git\*\* (opcional, para clonar o repositório)



\### Passo a Passo



1\. \*\*Clone o repositório\*\* (ou baixe o ZIP):

&#x20;  ```bash

&#x20;  git clone https://github.com/ArthurAmaral17/remedio-na-hora.git

&#x20;  cd remedio-na-hora



