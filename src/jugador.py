# src/jugador.py


class Jugador:
    def __init__(self, nombre, intentos_maximos=6):
        self.nombre = nombre
        self.intentos_restantes = intentos_maximos
        self.letras_usadas = []

    def registrar_intento(self, letra):
        letra = letra.upper()
        if letra not in self.letras_usadas:
            self.letras_usadas.append(letra)

    def descontar_vida(self):
        self.intentos_restantes -= 1

    def tiene_vidas(self):
        return self.intentos_restantes > 0
