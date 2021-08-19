#NoEnv
#Warn
SendMode Input  
SetWorkingDir %A_ScriptDir%  
SetTitleMatchMode 2

#q:: closePythonPlot() 
closePythonPlot()
{
    isExist = 1
    while isExist
    {
        PostMessage, 0x112, 0xF060,,, Figure
        IfWinNotExist, Figure
        {
            isExist = 0
        }
    }
}

#o::  Winset, Alwaysontop, , A

