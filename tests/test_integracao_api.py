"""
Testes de integração — API OpenFDA
Valida o fluxo de comunicação com o serviço externo usando mocks,
garantindo que a aplicação não quebre em caso de erros de rede.
"""
from unittest.mock import patch, Mock
import requests as req
import pytest

from src.drug_info import buscar_info_medicamento


def _mock_response(data: dict) -> Mock:
    """Cria um mock de resposta HTTP com os dados fornecidos."""
    mock = Mock()
    mock.json.return_value = data
    mock.raise_for_status = Mock()
    return mock


# ── Cenário 1: medicamento encontrado ────────────────────────────────────────

def test_buscar_medicamento_retorna_info_correta():
    """Deve retornar as informações do medicamento quando a API responde com sucesso."""
    payload = {
        "results": [
            {
                "openfda": {
                    "generic_name": ["PARACETAMOL"],
                    "manufacturer_name": ["Generic Pharma Inc"],
                },
                "purpose": ["Pain reliever and fever reducer."],
                "warnings": ["Do not exceed recommended dose."],
            }
        ]
    }

    with patch("src.drug_info.requests.get") as mock_get:
        mock_get.return_value = _mock_response(payload)

        info = buscar_info_medicamento("paracetamol")

        assert info is not None
        assert info["nome_generico"] == "PARACETAMOL"
        assert info["fabricante"] == "Generic Pharma Inc"
        assert "Pain reliever" in info["finalidade"]


# ── Cenário 2: medicamento não encontrado ─────────────────────────────────────

def test_buscar_medicamento_nao_encontrado_retorna_none():
    """Deve retornar None quando a API não encontra resultados."""
    payload = {"results": []}

    with patch("src.drug_info.requests.get") as mock_get:
        mock_get.return_value = _mock_response(payload)

        info = buscar_info_medicamento("xyzremedioinexistente")

        assert info is None


# ── Cenário 3: falha de conexão ───────────────────────────────────────────────

def test_buscar_medicamento_erro_de_conexao_retorna_none():
    """Deve retornar None e não lançar exceção quando há falha de rede."""
    with patch("src.drug_info.requests.get") as mock_get:
        mock_get.side_effect = req.ConnectionError("Sem conexão com a internet")

        info = buscar_info_medicamento("paracetamol")

        assert info is None


# ── Cenário 4: timeout ────────────────────────────────────────────────────────

def test_buscar_medicamento_timeout_retorna_none():
    """Deve retornar None quando a requisição excede o tempo limite."""
    with patch("src.drug_info.requests.get") as mock_get:
        mock_get.side_effect = req.Timeout("Tempo limite excedido")

        info = buscar_info_medicamento("ibuprofeno")

        assert info is None


# ── Cenário 5: API retorna erro HTTP ──────────────────────────────────────────

def test_buscar_medicamento_erro_http_retorna_none():
    """Deve retornar None quando a API retorna um status de erro (4xx/5xx)."""
    with patch("src.drug_info.requests.get") as mock_get:
        mock_get.side_effect = req.HTTPError("503 Service Unavailable")

        info = buscar_info_medicamento("amoxicilina")

        assert info is None
