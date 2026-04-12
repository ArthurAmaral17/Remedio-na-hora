import sys
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt, Confirm

from src.services import ControleMedicamentos

console = Console()
controle = ControleMedicamentos()

def cabecalho():
    console.print(Panel.fit(
        "[bold cyan]💊 REMÉDIO NA HORA CERTA[/bold cyan]\n"
        "[dim]Sistema de apoio para idosos e cuidadores[/dim]",
        border_style="cyan"
    ))

def exibir_tabela():
    table = Table(title="📋 Lista de Medicamentos", show_header=True, header_style="bold magenta")
    table.add_column("ID", style="dim", width=4)
    table.add_column("Medicamento", min_width=20)
    table.add_column("Horário", justify="center")
    table.add_column("Status", justify="center")

    medicamentos = controle.listar_todos()
    if not medicamentos:
        table.add_row("---", "Nenhum remédio cadastrado", "---", "---")
    else:
        for idx, med in enumerate(medicamentos):
            status = "[green]✓ TOMADO[/green]" if med.tomado else "[yellow]⏳ PENDENTE[/yellow]"
            table.add_row(str(idx+1), med.nome, med.horario, status)

    console.print(table)

def menu_principal():
    console.print("\n")
    console.print(Panel(
        "[1] [bold green]Adicionar[/bold green] novo remédio\n"
        "[2] [bold cyan]Listar[/bold cyan] medicamentos\n"
        "[3] [bold blue]Marcar como tomado[/bold blue]\n"
        "[4] [bold red]Remover[/bold red] medicamento\n"
        "[5] [bold yellow]Sair[/bold yellow]",
        title="Menu Principal",
        border_style="white"
    ))

def adicionar_medicamento():
    cabecalho()
    console.print("[bold]Novo Medicamento[/bold]\n")
    nome = Prompt.ask("Nome do remédio")
    horario = Prompt.ask("Horário (ex: 08:00, 14:30)")
    controle.adicionar(nome, horario)
    console.print(f"\n✅ [green]'{nome}' adicionado com sucesso![/green]")
    Prompt.ask("\nPressione ENTER para continuar")

def marcar_tomado():
    cabecalho()
    exibir_tabela()
    if not controle.listar_todos():
        Prompt.ask("\nPressione ENTER para voltar")
        return
    try:
        idx = Prompt.ask("\nDigite o [bold]ID[/bold] do medicamento que foi tomado", default="0")
        idx = int(idx) - 1
        if controle.marcar_como_tomado(idx):
            console.print("[green]✅ Status atualizado![/green]")
        else:
            console.print("[red]❌ ID inválido![/red]")
    except ValueError:
        console.print("[red]❌ Entrada inválida![/red]")
    Prompt.ask("\nPressione ENTER para continuar")

def remover_medicamento():
    cabecalho()
    exibir_tabela()
    if not controle.listar_todos():
        Prompt.ask("\nPressione ENTER para voltar")
        return
    try:
        idx = Prompt.ask("\nDigite o [bold red]ID[/bold red] do medicamento a remover", default="0")
        idx = int(idx) - 1
        if Confirm.ask(f"Tem certeza que deseja remover [red]{controle.listar_todos()[idx].nome}[/red]?"):
            if controle.remover(idx):
                console.print("[green]✅ Removido com sucesso![/green]")
            else:
                console.print("[red]❌ ID inválido![/red]")
    except (ValueError, IndexError):
        console.print("[red]❌ Entrada inválida ou ID inexistente![/red]")
    Prompt.ask("\nPressione ENTER para continuar")

def main():
    while True:
        console.clear()
        cabecalho()
        exibir_tabela()
        menu_principal()
        opcao = Prompt.ask("Escolha uma opção", choices=["1","2","3","4","5"], default="2")

        if opcao == "1":
            adicionar_medicamento()
        elif opcao == "2":
            pass
        elif opcao == "3":
            marcar_tomado()
        elif opcao == "4":
            remover_medicamento()
        elif opcao == "5":
            console.print("[yellow]Saindo... Obrigado por usar![/yellow]")
            sys.exit(0)

if __name__ == "__main__":
    main()