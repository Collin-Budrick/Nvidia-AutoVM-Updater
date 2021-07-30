echo off
for /f "tokens=*" %%a in ('powershell -Command "& {Get-ItemProperty -Path 'HKLM:\SOFTWARE\Microsoft\Virtual Machine\Guest\Parameters'  | Select-Object HostName}"') do set hostvm=%%a
net use Z: \\%hostvm%\DriverHub /persistent:yes
python "\\%hostvm%\DriverHub\autovm-updater.py"
exit /b