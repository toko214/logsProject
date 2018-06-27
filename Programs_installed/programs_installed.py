import StringIO
import traceback
import wmi
from _winreg import (HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, 
                     OpenKey, QueryValueEx,KEY_SET_VALUE)

errorLog = open('errors.log', 'w')

def get_programs_installed():
    """
    pasdasdasd
    :return:
    """
    key_paths = [r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall", r"Software\Microsoft\Windows\CurrentVersion\Uninstall" ]
    programs = []

    r = wmi.Registry()
    result, names = r.EnumKey(hDefKey=HKEY_LOCAL_MACHINE,
                              sSubKeyName=key_paths[1])
    for i in key_paths:
        for subkey in names:
            try:
              #  print subkey
              #   path = key_paths[0] + "\\" + subkey
              #   key = OpenKey(HKEY_LOCAL_MACHINE, path, 0,KEY_SET_VALUE)
                try:
                    if "{" not in subkey and subkey not in programs:
                        programs.append(subkey)
                except Exception, ex:
                    pass
                    # if not "{" in subkey:
                    #     programs.append(str(subkey))

            except Exception, ex:
                print ex
    return programs


