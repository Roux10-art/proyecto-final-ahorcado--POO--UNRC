@echo off
echo ==========================================
echo   CONFIGURADOR AUTOMATICO - AHORCADO POO
echo ==========================================

:: 1. Intentar crear el entorno virtual
echo [+] Creando entorno virtual (venv)...
py -m venv venv || python -m venv venv || python3 -m venv venv

:: 2. Activar e instalar dependencias
echo [+] Instalando librerias desde requirements.txt...
call .\venv\Scripts\activate
pip install -r requirements.txt

echo.
echo ==========================================
echo   ¡TODO LISTO! 
echo   Para jugar, escribe: python main.py
echo ==========================================
pause