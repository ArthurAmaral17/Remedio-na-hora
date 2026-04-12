import pytest
from src.services import ControleMedicamentos

def test_adicionar_medicamento():
    """Teste do caminho feliz: adicionar remédio válido"""
    c = ControleMedicamentos()
    c.adicionar("Dipirona", "08:00")
    assert len(c.listar_todos()) == 1
    assert c.listar_todos()[0].nome == "Dipirona"

def test_marcar_como_tomado_valido():
    """Teste: marcar um remédio existente como tomado"""
    c = ControleMedicamentos()
    c.adicionar("Rivotril", "22:00")
    assert c.marcar_como_tomado(0) is True
    assert c.listar_todos()[0].tomado is True

def test_marcar_como_tomado_invalido():
    """Teste: tentar marcar ID que não existe"""
    c = ControleMedicamentos()
    c.adicionar("Rivotril", "22:00")
    assert c.marcar_como_tomado(5) is False

def test_remover_medicamento_valido():
    """Teste: remover um remédio existente"""
    c = ControleMedicamentos()
    c.adicionar("AAS", "12:00")
    assert c.remover(0) is True
    assert len(c.listar_todos()) == 0

def test_remover_medicamento_invalido():
    """Teste: tentar remover ID que não existe"""
    c = ControleMedicamentos()
    assert c.remover(0) is False