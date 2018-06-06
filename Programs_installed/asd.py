import StringIO
import traceback
import wmi
from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS,
                     OpenKey,EnumValue, QueryValueEx)

errorLog = open('errors.log', 'w')
programs = []
r = wmi.Registry()

result, names = r.EnumKey(hDefKey=HKEY_LOCAL_MACHINE, sSubKeyName=r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall")
print result
for subkey in names:
    try:
        path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall" + "\\" + subkey
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

for i in programs:
    print i