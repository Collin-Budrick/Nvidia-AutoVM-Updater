echo off
mkdir "%APPDATA%\DriverHub\scripts"
mkdir "%APPDATA%\DriverHub\share"
Net Share DriverHub=%APPDATA%\DriverHub
Cacls %APPDATA%\DriverHub /e /r Everyone
Cacls %APPDATA%\DriverHub /e /g Everyone:F
pause
exit /b

python "%APPDATA%/DriverHub/scripts/autohost-updater.py"

exit /b
