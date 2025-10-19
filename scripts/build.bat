@echo off
setlocal

where python >nul 2>nul || (
  echo Python is not installed. && exit /b 1
)

python -m pip install -U pip build twine || exit /b 1

rd /s /q dist 2>nul
rd /s /q build 2>nul
for /d %%d in (*.egg-info) do rd /s /q "%%d" 2>nul

python -m build || exit /b 1

twine check dist/* || exit /b 1

echo Build and check OK.
