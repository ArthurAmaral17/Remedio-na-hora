# Remédio na Hora Certa

![Versão](https://img.shields.io/badge/vers%C3%A3o-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10%2B-yellow)
![Licença](https://img.shields.io/badge/licen%C3%A7a-MIT-green)

## Sobre o Projeto

O **Remédio na Hora Certa** é uma aplicação de linha de comando (CLI) desenvolvida para auxiliar no controle de medicamentos, permitindo cadastrar, visualizar, marcar como tomado e remover remédios de forma simples e prática.

A proposta do projeto é oferecer uma solução acessível para pessoas que precisam acompanhar tratamentos contínuos, especialmente em cenários em que o esquecimento de horários pode comprometer a saúde e a qualidade de vida.

---

## Problema Real

O esquecimento de horários de medicamentos é uma dor real que afeta principalmente:

- idosos que utilizam vários medicamentos diariamente;
- cuidadores familiares que acompanham rotinas de tratamento;
- pessoas com doenças crônicas;
- pacientes em uso contínuo de remédios.

Essas situações podem gerar:

- doses esquecidas;
- administração duplicada;
- falhas no tratamento;
- agravamento do quadro clínico.

---

## Solução Proposta

A aplicação foi criada para facilitar o gerenciamento de medicamentos por meio de uma interface CLI simples e intuitiva.

Com ela, o usuário pode:

- cadastrar medicamentos e horários;
- visualizar a lista de remédios com status atualizado;
- marcar medicamentos como tomados;
- remover medicamentos da rotina.

Tudo isso diretamente no terminal, sem depender de internet.

---

## Público-Alvo

Este projeto é voltado para:

- idosos;
- cuidadores;
- profissionais de saúde;
- qualquer pessoa que precise de um controle simples de medicamentos.

---

## Funcionalidades

- Cadastro de medicamentos com nome e horário
- Listagem dos medicamentos cadastrados
- Marcação de medicamento como tomado
- Remoção de medicamento
- Interface visual no terminal com a biblioteca Rich

---

## Tecnologias Utilizadas

- **Python 3.10+**
- **Rich**
- **Pytest**
- **Pylint**
- **GitHub Actions**

---

## Estrutura do Projeto

```bash
remedio-na-hora/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   ├── __init__.py
│   ├── cli.py
│   ├── models.py
│   └── services.py
├── tests/
│   ├── __init__.py
│   └── test_services.py
├── .gitignore
├── requirements.txt
├── VERSION
└── README.md
