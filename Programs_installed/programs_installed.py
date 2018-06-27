"""
Author: Tomer Perets
Date: 27.6.2018
this file contains a function that help receiving all the programs installed on this pc.
"""

import wmi
from _winreg import HKEY_LOCAL_MACHINE


def get_programs_installed():
    """
    searching in the registry for the programs installed on this pc.
    its possible its wont find all the programs cause sometime the programs not installed/uninstalled properly.
    :return: list of programs installed on the pc
    """
    key_path = r"Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall"
    programs = []
    r = wmi.Registry()
    result, names = r.EnumKey(hDefKey=HKEY_LOCAL_MACHINE,
                              sSubKeyName=key_path)
    for subkey in names:
        if "{" not in subkey and subkey not in programs:
            programs.append(subkey)
    return programs


