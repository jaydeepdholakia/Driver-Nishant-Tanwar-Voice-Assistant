Set-Variable -Name "name" -Value "Bot OP"

pyinstaller -i icon.ico -n $name --hidden-import=pyttsx3.drivers.sapi5 --onefile speech.py
Copy-Item ./dist/$name.exe ./