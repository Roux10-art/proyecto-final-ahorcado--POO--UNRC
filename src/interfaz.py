import customtkinter as ctk

# Constantes de diseño
FUENTE_APP = "Segoe UI"
FUENTE_MONO = "Consolas"

# Configuración global de Windows 11
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class Interfaz(ctk.CTk):
    def __init__(self, callback_adivinar, callback_inicio):
        super().__init__()

        self.title("Ahorcado POO - UNRC")
        self.geometry("800x600")

        # Callbacks para comunicarse con MotorJuego
        self.callback_adivinar = callback_adivinar
        self.callback_inicio = callback_inicio

        # Contenedor principal
        self.container = ctk.CTkFrame(self, corner_radius=15)
        self.container.pack(padx=20, pady=20, fill="both", expand=True)

        self.setup_pantalla_inicio()

    def limpiar_pantalla(self):
        """En GUI, esto significa destruir los widgets actuales del contenedor."""
        for widget in self.container.winfo_children():
            widget.destroy()

    def setup_pantalla_inicio(self):
        self.limpiar_pantalla()

        ctk.CTkLabel(
            self.container, text="AHORCADO POO", font=(FUENTE_APP, 36, "bold")
        ).pack(pady=30)
        ctk.CTkLabel(
            self.container, text="Reto Final - 4to Semestre", font=(FUENTE_APP, 16)
        ).pack()

        self.entry_nombre = ctk.CTkEntry(
            self.container, placeholder_text="Tu nombre aquí...", width=300, height=40
        )
        self.entry_nombre.pack(pady=20)

        # NUEVO: Permitir que la tecla Enter también funcione
        self.entry_nombre.bind("<Return>", self.procesar_inicio)

        ctk.CTkButton(
            self.container, text="Continuar", command=self.procesar_inicio, height=40
        ).pack(pady=10)

    def procesar_inicio(self, event=None):
        nombre = self.entry_nombre.get().strip()

        # Esto se imprimirá en la terminal de fondo
        print(f"[DEBUG] Botón presionado. Nombre capturado: '{nombre}'")

        if nombre:
            print("[DEBUG] Nombre válido. Cambiando a pantalla de categorías...")
            self.nombre_jugador = nombre
            self.seleccionar_categoria(nombre)
        else:
            print("[DEBUG] El nombre estaba vacío.")
            self.entry_nombre.configure(
                placeholder_text="¡Por favor, escribe tu nombre!",
                placeholder_text_color="#ff6b6b",
            )

    def seleccionar_categoria(self, nombre):
        self.limpiar_pantalla()
        ctk.CTkLabel(
            self.container,
            text=f"Hola {nombre}, elige una categoría:",
            font=(FUENTE_APP, 20),
        ).pack(pady=20)

        categorias = [
            ("Países", "paises"),
            ("Animales", "animales"),
            ("Alimentos", "alimentos"),
            ("Películas", "peliculas"),
        ]

        for texto, valor in categorias:
            ctk.CTkButton(
                self.container,
                text=texto,
                width=200,
                command=lambda v=valor: self.callback_inicio(v),
            ).pack(pady=5)

    def mostrar_escenario(self, progreso, intentos, usadas):
        self.limpiar_pantalla()

        # Layout de juego: Izquierda (Dibujo/Info) - Derecha (Palabra/Input)
        main_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        main_frame.pack(fill="both", expand=True, padx=20, pady=20)

        # Sección de Palabra (usamos la constante de fuente monoespaciada)
        self.lbl_palabra = ctk.CTkLabel(
            main_frame, text=progreso, font=(FUENTE_MONO, 45, "bold")
        )
        self.lbl_palabra.pack(pady=40)

        # Info de intentos
        self.lbl_info = ctk.CTkLabel(
            main_frame,
            text=f"Intentos: {intentos} | Usadas: {', '.join(usadas)}",
            font=(FUENTE_APP, 14),
        )
        self.lbl_info.pack(pady=10)

        # Entrada de letra
        self.input_letra = ctk.CTkEntry(
            main_frame,
            width=60,
            placeholder_text="A",
            font=(FUENTE_APP, 20),
            justify="center",
        )
        self.input_letra.pack(pady=10)
        self.input_letra.bind("<Return>", lambda event: self.enviar_letra())

        ctk.CTkButton(main_frame, text="Adivinar", command=self.enviar_letra).pack(
            pady=10
        )

    def enviar_letra(self):
        letra = self.input_letra.get().upper()
        self.input_letra.delete(0, "end")
        if len(letra) == 1 and letra.isalpha():
            self.callback_adivinar(letra)

    def mostrar_resultado(self, gano, palabra_secreta):
        self.limpiar_pantalla()
        color = "#28a745" if gano else "#dc3545"
        texto = "¡VICTORIA!" if gano else "GAME OVER"

        ctk.CTkLabel(
            self.container, text=texto, font=(FUENTE_APP, 40, "bold"), text_color=color
        ).pack(pady=30)
        ctk.CTkLabel(
            self.container,
            text=f"La palabra era: {palabra_secreta}",
            font=(FUENTE_APP, 18),
        ).pack(pady=10)

        ctk.CTkButton(
            self.container, text="Jugar de nuevo", command=self.setup_pantalla_inicio
        ).pack(pady=20)
