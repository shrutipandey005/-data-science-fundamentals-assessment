<#
.SYNOPSIS
    Data Science Fundamentals Assessment - One-Click PowerShell Execution Script
#>

Write-Host "======================================================================" -ForegroundColor Cyan
Write-Host "  DATA SCIENCE FUNDAMENTALS ASSESSMENT - ONE CLICK RUNNER" -ForegroundColor Cyan
Write-Host "======================================================================" -ForegroundColor Cyan

$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
Set-Location $ScriptDir

# Try standard Python first, then MySQL Python fallback
$PythonExe = $null

if (Get-Command python -ErrorAction SilentlyContinue) {
    try {
        $ver = & python -c "import sys; print(sys.version)" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $PythonExe = "python"
        }
    } catch {}
}

if (-not $PythonExe -and (Get-Command py -ErrorAction SilentlyContinue)) {
    try {
        $ver = & py -c "import sys; print(sys.version)" 2>$null
        if ($LASTEXITCODE -eq 0) {
            $PythonExe = "py"
        }
    } catch {}
}

$FallbackPython = "C:\Program Files\MySQL\MySQL Workbench 8.0\swb\shell\lib\Python3.13\python.exe"
if (-not $PythonExe -and (Test-Path $FallbackPython)) {
    $PythonExe = $FallbackPython
    $env:PYTHONHOME = "C:\Program Files\MySQL\MySQL Workbench 8.0\swb\shell\lib\Python3.13"
    $env:PYTHONPATH = ""
    Write-Host "[*] Using verified Python 3.13 runtime engine at: $PythonExe" -ForegroundColor Yellow
}

if (-not $PythonExe) {
    Write-Host "[ERROR] No usable Python executable found." -ForegroundColor Red
    Write-Host "Please install Python 3 via: winget install Python.Python.3.12" -ForegroundColor Yellow
    exit 1
}

Write-Host "[*] Executing Unified Assessment Runner..." -ForegroundColor Green
& $PythonExe run.py

