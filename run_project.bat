@echo off
setlocal EnableDelayedExpansion

echo ======================================================================
echo   DATA SCIENCE FUNDAMENTALS ASSESSMENT - WINDOWS RUNNER
echo ======================================================================

set SCRIPT_DIR=%~dp0
cd /d "%SCRIPT_DIR%"

set PYTHON_CMD=

:: Check if standard python works
python --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=python
    goto run_script
)

:: Check if py launcher works
py --version >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    set PYTHON_CMD=py
    goto run_script
)

:: Fallback to installed MySQL Workbench Python 3.13
if exist "C:\Program Files\MySQL\MySQL Workbench 8.0\swb\shell\lib\Python3.13\python.exe" (
    set "PYTHONHOME=C:\Program Files\MySQL\MySQL Workbench 8.0\swb\shell\lib\Python3.13"
    set "PYTHONPATH="
    set "PYTHON_CMD=C:\Program Files\MySQL\MySQL Workbench 8.0\swb\shell\lib\Python3.13\python.exe"
    goto run_script
)

echo [ERROR] No working Python 3 installation detected.
echo Please install Python 3.10+ from https://www.python.org or run:
echo    winget install Python.Python.3.12
pause
exit /b 1

:run_script
echo [*] Executing Data Science Assessment using: %PYTHON_CMD%
"%PYTHON_CMD%" run.py

if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Assessment run finished with errors.
) else (
    echo.
    echo ======================================================================
    echo   ASSESSMENT SUCCESSFULLY COMPLETED!
    echo ======================================================================
)

pause

