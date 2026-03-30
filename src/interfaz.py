import os
from art import tprint
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.prompt import Prompt, IntPrompt

console = Console()


class Interfaz:
    def __init__(self):
        self.console = console

    def limpiar_pantalla(self):
        # Comando para Windows (cls) o Linux/Mac (clear)
        os.system("cls" if os.name == "nt" else "clear")

    def mostrar_bienvenida(self):
        self.limpiar_pantalla()
        # 'art' genera el título ASCII gigante
        tprint("AHORCADO  POO", font="small")
        self.console.print(
            Panel(
                "[bold white]Bienvenido al reto final de 4to Semestre[/bold white]",
                style="on blue",
                expand=False,
            )
        )

    def pedir_nombre(self):
        return Prompt.ask("[bold green]¿Cuál es tu nombre, jugador?[/bold green]")

    def seleccionar_categoria(self):
        self.console.print("\n[bold yellow]Selecciona una categoría:[/bold yellow]")
        self.console.print("1. Países\n2. Animales\n3. Alimentos\n4. Películas")

        opcion = IntPrompt.ask("Elige un número", choices=["1", "2", "3", "4"])
        categorias = {1: "paises", 2: "animales", 3: "alimentos", 4: "peliculas"}
        return categorias[opcion]

    def mostrar_escenario(self, progreso, intentos, usadas):
        """
        Dibuja la tabla de estado y la palabra oculta.
        """
        self.limpiar_pantalla()
        tprint("JUGANDO", font="minis")

        # Tabla de información
        tabla = Table(show_header=True, header_style="bold magenta")
        tabla.add_column("Intentos Restantes", justify="center")
        tabla.add_column("Letras Probadas", justify="center")

        col_intentos = (
            f"[bold red]{intentos}[/bold red]" if intentos < 3 else str(intentos)
        )
        tabla.add_row(col_intentos, ", ".join(usadas))

        self.console.print(tabla)

        # Mostrar el progreso de la palabra (ej: A _ _ O)
        self.console.print(
            f"\n[bold cyan]PALABRA:[/bold cyan] [white]{progreso}[/white]\n"
        )

    def pedir_letra(self):
        return Prompt.ask("[bold green]Ingresa una letra[/bold green]").upper()

    def mostrar_resultado(self, gano, palabra_secreta):
        if gano:
            self.console.print(
                Panel(
                    f"[bold green]¡FELICIDADES! Has adivinado: {palabra_secreta}[/bold green]"
                )
            )
        else:
            self.console.print(
                Panel(
                    f"[bold red]GAME OVER. La palabra era: {palabra_secreta}[/bold red]"
                )
            )
