import random
import sys
from src.interfaz import Interfaz
from src.gestor_datos import GestorDatos
from src.palabra import Palabra
from src.jugador import Jugador


class MotorJuego:
    def __init__(self):
        self.interfaz = Interfaz()
        self.gestor = GestorDatos()
        self.jugador = None
        self.palabra_obj = None

    def preparar_partida(self):
        self.interfaz.mostrar_bienvenida()

        # 1. Registro de jugador
        nombre = self.interfaz.pedir_nombre()
        self.jugador = Jugador(nombre)

        # 2. Selección de categoría y carga de datos
        categoria_id = self.interfaz.seleccionar_categoria()
        lista_palabras = self.gestor.cargar_palabras(categoria_id)

        if not lista_palabras:
            print("❌ Error fatal: No hay palabras disponibles para jugar.")
            sys.exit()

        # 3. Elegir palabra al azar e instanciar lógica de Palabra
        seleccion = random.choice(lista_palabras)
        self.palabra_obj = Palabra(seleccion)

    def jugar(self):
        self.preparar_partida()

        # Bucle principal de la partida
        while self.jugador.tiene_vidas() and not self.palabra_obj.es_palabra_completa():
            # Actualizar visuales
            self.interfaz.mostrar_escenario(
                progreso=self.palabra_obj.obtener_progreso(),
                intentos=self.jugador.intentos_restantes,
                usadas=self.jugador.letras_usadas,
            )

            # Entrada del usuario
            letra = self.interfaz.pedir_letra()

            # Lógica de validación
            if not self.palabra_obj.verificar_letra(letra):
                if letra not in self.jugador.letras_usadas:
                    self.jugador.descontar_vida()

            self.jugador.registrar_intento(letra)

        # Fin del juego
        self.interfaz.limpiar_pantalla()
        self.interfaz.mostrar_resultado(
            gano=self.palabra_obj.es_palabra_completa(),
            palabra_secreta=self.palabra_obj.secreta,
        )


if __name__ == "__main__":
    app = MotorJuego()
    try:
        app.jugar()
    except KeyboardInterrupt:
        print("\n\n👋 Partida finalizada por el usuario. ¡Hasta pronto!")
