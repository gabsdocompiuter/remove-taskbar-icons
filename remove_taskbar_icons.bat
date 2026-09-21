@echo off
setlocal

timeout /t 5 /nobreak >nul

cd /d "%~dp0"

if not exist "venv\Scripts\activate.bat" (
    echo Criando ambiente virtual...
    python -m venv venv

    if errorlevel 1 exit /b 1

    call "venv\Scripts\activate.bat"

    echo Instalando dependencias...
    pip install -r requirements.txt

    if errorlevel 1 exit /b 1
) else (
    call "venv\Scripts\activate.bat"
)

python main.py

endlocal
