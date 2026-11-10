@echo off
setlocal EnableDelayedExpansion

echo ======================================================================
echo   ATTACH & PUSH PROJECT TO GITHUB
echo ======================================================================

set "GIT_CMD=C:\Users\User\AppData\Local\Programs\Git\cmd\git.exe"
if not exist "%GIT_CMD%" (
    where git >nul 2>&1
    if %ERRORLEVEL% EQU 0 (
        set "GIT_CMD=git"
    ) else (
        echo [ERROR] Git was not found. Please verify Git installation.
        pause
        exit /b 1
    )
)

cd /d "%~dp0"

echo [*] Current Git status:
"%GIT_CMD%" status --short

echo.
set /p REPO_URL="Enter your GitHub repository URL (e.g. https://github.com/username/repo.git): "

if "%REPO_URL%"=="" (
    echo [ERROR] No URL entered. Aborting.
    pause
    exit /b 1
)

echo [*] Configuring remote origin -> %REPO_URL%
"%GIT_CMD%" remote remove origin >nul 2>&1
"%GIT_CMD%" remote add origin %REPO_URL%

echo [*] Pushing 'main' branch to GitHub...
"%GIT_CMD%" push -u origin main

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ======================================================================
    echo   PROJECT SUCCESSFULLY PUBLISHED TO GITHUB!
    echo ======================================================================
) else (
    echo.
    echo [NOTE] If this is a private repo or first push, GitHub may ask you to sign in.
    echo You can also click 'Publish Branch' directly in the VS Code Source Control tab.
)

pause
