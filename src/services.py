from typing import List
from src.models import Medicamento

class ControleMedicamentos:
    def __init__(self):
        self.medicamentos: List[Medicamento] = []

    def adicionar(self, nome: str, horario: str) -> None:
        self.medicamentos.append(Medicamento(nome, horario))

    def listar_todos(self) -> List[Medicamento]:
        return self.medicamentos

    def marcar_como_tomado(self, indice: int) -> bool:
        if 0 <= indice < len(self.medicamentos):
            self.medicamentos[indice].tomado = True
            return True
        return False

    def remover(self, indice: int) -> bool:
        if 0 <= indice < len(self.medicamentos):
            self.medicamentos.pop(indice)
            return True
        return False