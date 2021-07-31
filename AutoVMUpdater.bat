echo off
for /f "tokens=*" %%a in ('powershell -Command "& {Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters'  | Select-Object PhysicalHostName}"') do set hostvm=%%a
net use Z: \\%hostvm%\DriverHub
powershell -Command "$env:HostVM = '%hostvm%'"
pause
exit /b

python "\\%hostvm%\DriverHub\scripts\autovm-updater.py"
exit /b