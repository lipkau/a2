; this is the script that becomes the a2.exe in root!
If (!A_IsCompiled)
{
    MsgBox a2_starter should only be run compiled!
    ExitApp
}

settings_created := _init_check_settings()
a2_ahk := _init_get_autohotkey_exe()

Run, %a2_ahk% lib\a2.ahk, %A_ScriptDir%

if settings_created
{
    MsgBox, 65, a2 Settings Created!, Default settings have just been created, do you want to open up the a2 User Interface to make further changes?
    IfMsgBox, Ok
        Run, a2ui.ahk        
}

Return ; -----------------------------------------------------------------------------
#include a2init_check.ahk
