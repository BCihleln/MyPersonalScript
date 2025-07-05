@echo off

:: 改變CMD窗口大小
mode con cols=50 lines=10

:: 獲取臨時管理員權限
%1 %2
ver|find "5.">nul && goto :Admin
mshta vbscript:createobject("shell.application").shellexecute("%~s0","goto :Admin","","runas",1)(window.close)&goto :eof
:Admin

:: 實際命令
taskkill -f -im NMS.exe -t && echo Time to Sleep && pause