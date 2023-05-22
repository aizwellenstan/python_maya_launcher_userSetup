@echo off

:: set Maya env
set MAYA_VERSION=2022

set MAYA_UI_LANGUAGE=en_US

set MAYA_APP_DIR=%userprofile%\Documents\NMA\projects\%PROJNAME%\Documents\maya
if not exist %MAYA_APP_DIR% mkdir %MAYA_APP_DIR%

set MODULE_FOLDER=%MAYA_APP_DIR%\modules
if not exist %MODULE_FOLDER% mkdir %MODULE_FOLDER%

set SCRIPT_FOLDER=%MAYA_APP_DIR%\%MAYA_VERSION%\scripts
if not exist %SCRIPT_FOLDER% mkdir %SCRIPT_FOLDER%

robocopy I:\script\bin\td\bin\project\%PROJNAME%\mod %MODULE_FOLDER%\ /it /E /IS /IT
robocopy I:\script\bin\td\bin\project\add\userSetup %SCRIPT_FOLDER%\ /it /E /IS /IT
set MAYA_SHELF_PATH=J:/%PROJNAME%/work/project_tools/shelves

set OCIO=J:\%PROJNAME%\proj\add\tool\settings\ocio\v5\config.ocio

call %NMA_MAYA_EXE% %* -pythonver 2
