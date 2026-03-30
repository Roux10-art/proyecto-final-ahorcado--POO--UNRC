import json
import os


class GestorDatos:
    @staticmethod
    def cargar_palabras(nombre_archivo):
        """
        Lee un archivo JSON y devuelve la lista de palabras.
        Maneja errores si el archivo no existe o está mal formado.
        """
        ruta = os.path.join("data", f"{nombre_archivo}.json")
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                datos = json.load(archivo)
                return datos.get("palabras", [])
        except FileNotFoundError:
            # Aquí lanzamos una alerta pero el programa no "explota"
            print(f"⚠️ Error: No se encontró el archivo en {ruta}")
            return []
        except json.JSONDecodeError:
            print(
                f"⚠️ Error: El archivo {nombre_archivo}.json tiene un formato inválido"
            )
            return []
