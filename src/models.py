from dataclasses import dataclass

@dataclass
class Medicamento:
    nome: str
    horario: str
    tomado: bool = False