# Remédio na Hora Certa

## Nome do Projeto
Remédio na Hora Certa

## Descrição do Problema Real
O esquecimento de horários de medicamentos é um problema real que pode comprometer a saúde e a qualidade de vida de muitas pessoas. Isso acontece com frequência entre idosos, cuidadores, pessoas com doenças crônicas e pacientes que fazem uso contínuo de remédios. A falta de controle pode causar doses esquecidas, administração duplicada, falhas no tratamento e agravamento do quadro clínico.

## Proposta da Solução
O projeto Remédio na Hora Certa foi desenvolvido para auxiliar no controle de medicamentos de forma simples e prática. A aplicação permite cadastrar remédios, visualizar a lista dos medicamentos registrados, marcar quais já foram tomados e remover registros quando necessário. A proposta é oferecer uma solução acessível e funcional para ajudar na organização da rotina de medicação.

## Público-Alvo
- Idosos
- Cuidadores
- Pessoas com doenças crônicas
- Pacientes em uso contínuo de medicamentos
- Pessoas que precisam de um controle simples de remédios

## Funcionalidades Principais
- Cadastro de medicamentos com nome e horário
- Listagem dos medicamentos cadastrados
- Marcação de medicamento como tomado
- Remoção de medicamento
- Interface visual no terminal

## Tecnologias Utilizadas
- Python 3.10+
- Rich
- Pytest
- Pylint
- GitHub Actions

# Remédio na Hora

Aplicação para auxiliar no controle de horários de medicamentos.

---

🚀 Instruções de Instalação
Pré-requisitos
Python 3.8 ou superior

pip (gerenciador de pacotes do Python)

Git (opcional)

Passo a Passo
Clone o repositório:

bash
git clone https://github.com/ArthurAmaral17/remedio-na-hora.git
Acesse a pasta do projeto:

bash
cd remedio-na-hora
Crie e ative um ambiente virtual (recomendado):

bash
python -m venv venv

# Windows:
venv\Scripts\activate

# Mac/Linux:
source venv/bin/activate
Instale as dependências:

bash
pip install -r requirements.txt
🖥️ Instruções de Execução
Com o ambiente virtual ativado e estando na raiz do projeto, execute:

bash
python -m src.cli
O sistema abrirá um menu interativo com as seguintes opções:

1 - Adicionar novo medicamento

2 - Listar medicamentos cadastrados

3 - Marcar medicamento como tomado

4 - Remover medicamento

5 - Sair do sistema

🧪 Instruções para Rodar os Testes
O projeto possui 5 testes automatizados validando os principais comportamentos do sistema.

Para executá-los, use:

bash
pytest tests/ -v
Saída esperada: 5 testes passando com sucesso (todos PASSED).

🔍 Instruções para Rodar o Lint
A qualidade do código é verificada com Pylint (nota atual: 8.17/10).

Para executar a análise estática:

bash
pylint src
A configuração personalizada está no arquivo .pylintrc na raiz do projeto.


## Versão Atual
**1.0.0**

## Nome do Autor
**Arthur Amaral dos Santos**

## Link do Repositório Público
[GitHub - Remédio na Hora Certa](https://github.com/ArthurAmaral17/remedio-na-hora)
