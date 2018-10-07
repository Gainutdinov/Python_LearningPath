set UIFILE=%1
set UIDIR=%~dp1
set FILENAME=%~n1
set PQTNAME=%UIDIR%%FILENAME%_ui.py
CALL "C:\Program Files (x86)\Python36-32\Scripts\pyuic5.exe" %UIFILE% -o %PQTNAME%