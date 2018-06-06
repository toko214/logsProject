import StringIO
import traceback
import wmi
from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, 
                     OpenKey, QueryValueEx)

errorLog = open('errors.log', 'w')

def get_programs_installed():
    #key_paths = [r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall", r"Software\Microsoft\Windows\CurrentVersion\Uninstall" ]
    programs = []

    r = wmi.Registry()
    result, names = r.EnumKey(hDefKey=HKEY_LOCAL_MACHINE, sSubKeyName=r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall")
    for subkey in names:
        try:
            path = r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall" + "\\" + subkey
            print path
            key = OpenKey(HKEY_LOCAL_MACHINE, path, 0, KEY_ALL_ACCESS)
            try:
                temp = QueryValueEx(key, 'DisplayName')
                display = str(temp[0])
                programs.append(display)
            except:
                if not "{" in subkey:
                    programs.append(str(subkey))

        except:
            fp = StringIO.StringIO()
            traceback.print_exc(file=fp)
            errorMessage = fp.getvalue()
            error = 'Error for ' + path + '. Message follows:\n' + errorMessage
            errorLog.write(error)
            errorLog.write("\n\n")
    return programs

