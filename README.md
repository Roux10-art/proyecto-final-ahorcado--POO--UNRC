# 🎮 Proyecto: El Ahorcado POO (GUI Edition)

¡Bienvenidos al equipo!

Este es un entorno de desarrollo profesional donde aplicaremos **POO Avanzada** y **Persistencia de Datos** para crear una versión gráfica de "El Ahorcado" digna de 4.º semestre.

---

## 🛠️ Estándar de Código (Clean Code)

_Mantenemos nuestras reglas de oro para que el código se explique solo:_

- **Importaciones:** `from src.gestor_datos import GestorDatos`

## ⚠️ Prohibiciones de Nomenclatura

- ❌ GestorDatos.py (No usar PascalCase en nombres de archivos).
- ❌ gestorDatos.py (No usar camelCase en nombres de archivos).
- ❌ from src.GestorDatos import gestor_datos (No invertir los estándares).

**Clases:** `PascalCase` (ej: `MotorJuego`)

- **Funciones/Variables:** `snake_case` (ej: `validar_entrada_usuario`)
- **Booleanos:** Prefijos `es_` o `tiene_` (ej: `es_ganador`)
- **Prohibición:** Prohibido usar variables de una sola letra (x, i, c).

---

## 🚀 Guía de Colaboración (Git Flow)

_Seguiremos el flujo de **Fork & Pull Request** para proteger la rama `main`:_

1. **Fork** el repo.
2. Crea una rama: `git checkout -b feature/nombre-tu-clase`.
3. **Commits:** Usa prefijos (`feat:`, `fix:`, `style:`).
4. **Pull Request:** Describe tus cambios antes de solicitar el merge.

---

## 📂 Estructura del Proyecto

- `/data/`: Archivos `.json` con categorías (Países, Animales, etc.).
- `/src/`: Clases del sistema (`palabra.py`, `jugador.py`, `interfaz.py`, etc.).
- `main.py`: Punto de entrada del programa.

## Archivos que NO se deben modificar

- `main.py`
- `requirements.txt`
- `README.md`
- `.gitignore`
- `setup.bat`
- `data/`
- `venv/`

---

## 🖥️ Instalación vía terminal

1. `py -m venv venv` o `python -m venv venv`
2. Activar: `.\venv\Scripts\activate` (Windows)
3. Activar: `source venv/bin/activate` (Mac/Linux)
4. Instalar dependencias: `pip install -r requirements.txt` (Instala la librería **CustomTkinter**)
5. **Ejecutar:** `py main.py` o `python main.py`

## 🖥️ Instalación via script (opcion recomendada para windows)

1. Ejecutar con doble click el archivo `setup.bat`
2. **Ejecutar:** `py main.py` o `python main.py`
3. El juego debería iniciar automaticamente

---
