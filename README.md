# 💊 Remédio na Hora Certa

![Versão](https://img.shields.io/badge/versão-1.0.0-blue)
![Python](https://img.shields.io/badge/Python-3.10+-yellow)
![Licença](https://img.shields.io/badge/licença-MIT-green)
![CI Status](https://github.com/ArthurAmaral17/remedio-na-hora/actions/workflows/ci.yml/badge.svg)

## 📖 Sobre o Projeto

O **Remédio na Hora Certa** é uma aplicação de linha de comando (CLI) desenvolvida para auxiliar no **controle de medicamentos**, permitindo cadastrar, visualizar, marcar como tomado e remover remédios de forma simples e prática.

A proposta do projeto é oferecer uma solução acessível para pessoas que precisam acompanhar tratamentos contínuos, especialmente em cenários em que o esquecimento de horários pode comprometer a saúde e a qualidade de vida.

---

## 📌 Problema Real

O esquecimento de horários de medicamentos é uma das principais causas de complicações em tratamentos de saúde, principalmente entre:

- **Idosos** que utilizam vários medicamentos diariamente
- **Cuidadores familiares** que precisam gerenciar múltiplas prescrições
- **Pessoas com doenças crônicas**, como hipertensão e diabetes
- **Profissionais de home care** que acompanham pacientes em rotina contínua

Essas situações podem resultar em:

- doses esquecidas
- administração duplicada
- falhas no acompanhamento do tratamento
- agravamento do quadro clínico

---

## 🎯 Solução Proposta

O **Remédio na Hora Certa** foi criado para facilitar o gerenciamento de medicamentos por meio de uma interface CLI intuitiva, organizada e visualmente amigável.

Com ele, o usuário pode:

- cadastrar medicamentos e horários
- visualizar a lista de remédios com status atualizado
- marcar doses como administradas
- remover medicamentos quando necessário

Tudo isso diretamente no terminal, sem depender de internet ou hardware específico.

---

## 👥 Público-Alvo

Este projeto é voltado para:

- idosos
- cuidadores familiares
- profissionais de saúde
- qualquer pessoa que precise de um controle simples e confiável de medicamentos

---

## ⚙️ Funcionalidades

- ✅ **Cadastro de medicamentos**  
  Permite registrar o nome e o horário de cada remédio.

- 📋 **Listagem visual**  
  Exibe os medicamentos em tabela formatada com status como **Pendente** ou **Tomado**.

- ✔️ **Marcação de doses**  
  Possibilita confirmar quando um medicamento foi administrado.

- 🗑️ **Remoção de medicamentos**  
  Remove itens que não fazem mais parte da rotina do usuário.

- 🎨 **Interface rica no terminal**  
  Utiliza a biblioteca **Rich** para melhorar a experiência visual com cores, painéis e tabelas.

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Finalidade |
| :--- | :--- |
| **Python 3.10+** | Linguagem principal do projeto |
| **Rich** | Interface CLI com tabelas, painéis e estilização |
| **Pytest** | Testes automatizados |
| **Pylint** | Análise estática e padronização do código |
| **GitHub Actions** | Integração contínua (CI) |

---

## 📂 Estrutura do Projeto

## 📂 Estrutura do Projeto

```bash
remedio-na-hora/
├── .github/
│   └── workflows/
│       └── ci.yml              # Pipeline de CI (lint + testes)
├── src/
│   ├── __init__.py
│   ├── models.py               # Classes de domínio
│   ├── services.py             # Lógica de negócio
│   └── cli.py                  # Interface de linha de comando
├── tests/
│   ├── __init__.py
│   └── test_services.py        # Testes automatizados
├── .gitignore
├── .pylintrc                   # Configurações do Pylint
├── requirements.txt            # Dependências do projeto
├── VERSION                     # Controle de versão
├── demo.gif
└── README.md

```

## 🖥️ Demonstração

Veja abaixo a aplicação em funcionamento diretamente no terminal:

<p align="center">
  <img src="demo.gif" alt="Demonstração do sistema Remédio na Hora Certa" width="700">
</p>

### 💡 Fluxo da aplicação

A demonstração mostra:

- Cadastro de um medicamento
- Visualização da lista em tabela
- Marcação como tomado
- Uso completo via terminal
