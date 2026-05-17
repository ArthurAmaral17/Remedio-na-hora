"""
Módulo de integração com a API OpenFDA.
Busca informações públicas sobre medicamentos a partir do nome.
API: https://api.fda.gov/drug/label.json
"""
import requests

OPENFDA_URL = "https://api.fda.gov/drug/label.json"
TIMEOUT_SEGUNDOS = 5


def buscar_info_medicamento(nome: str):
    try:
        params = {
            "search": (
                f'openfda.brand_name:"{nome}" '
                f'openfda.generic_name:"{nome}"'
            ),
            "limit": 1,
        }
        response = requests.get(OPENFDA_URL, params=params, timeout=TIMEOUT_SEGUNDOS)
        response.raise_for_status()
        data = response.json()

        resultados = data.get("results")
        if not resultados:
            return None

        result = resultados[0]
        openfda = result.get("openfda", {})

        info = {
            "nome_generico": openfda.get("generic_name", ["Não informado"])[0],
            "fabricante": openfda.get("manufacturer_name", ["Não informado"])[0],
            "finalidade": result.get("purpose", ["Não informado"])[0][:300],
            "advertencias": result.get("warnings", ["Não informado"])[0][:300],
        }
        return info

    except requests.RequestException:
        return None