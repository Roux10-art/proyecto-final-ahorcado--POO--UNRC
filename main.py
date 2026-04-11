import sys
import random
from src.interfaz import Interfaz
from src.gestor_datos import GestorDatos
from src.palabra import Palabra
from src.jugador import Jugador


class MotorJuego:
    def __init__(self):
        # Conectamos las funciones del motor con la interfaz visual
        self.interfaz = Interfaz(
            callback_adivinar=self.intentar_letra, callback_inicio=self.iniciar_partida
        )
        self.gestor = GestorDatos()
        self.jugador = None
        self.palabra_obj = None

    def iniciar_partida(self, categoria_id):
        """Se activa cuando el usuario elige una categoría en la pantalla principal."""
        # Tomamos el nombre guardado en la interfaz
        nombre = getattr(self.interfaz, 'nombre_jugador', "Jugador")
        self.jugador = Jugador(nombre)

        lista_palabras = self.gestor.cargar_palabras(categoria_id)
        if not lista_palabras:
            print("❌ Error fatal: No hay palabras disponibles.")
            sys.exit()

        seleccion = random.choice(lista_palabras)
        self.palabra_obj = Palabra(seleccion)

        # Pintamos la pantalla de juego
        self.actualizar_pantalla()

    def intentar_letra(self, letra):
        """Se activa cada vez que el usuario presiona el botón 'Adivinar'."""
        if not self.palabra_obj.verificar_letra(letra):
            if letra not in self.jugador.letras_usadas:
                self.jugador.descontar_vida()

        self.jugador.registrar_intento(letra)

        # Validar si ganó o perdió
        if not self.jugador.tiene_vidas() or self.palabra_obj.es_palabra_completa():
            self.interfaz.mostrar_resultado(
                gano=self.palabra_obj.es_palabra_completa(),
                palabra_secreta=self.palabra_obj.secreta,
            )
        else:
            self.actualizar_pantalla()

    def actualizar_pantalla(self):
        """Actualiza los textos visuales de la interfaz."""
        self.interfaz.mostrar_escenario(
            progreso=self.palabra_obj.obtener_progreso(),
            intentos=self.jugador.intentos_restantes,
            usadas=self.jugador.letras_usadas,
        )


if __name__ == "__main__":
    app = MotorJuego()
    # Este comando reemplaza a tu antiguo bucle 'while'.
    # Mantiene la ventana abierta escuchando los clics del mouse.
    app.interfaz.mainloop()
