"""
author: Tomer Perets
date: 5.5.2018
this file uses the skype_info to get the data from skype.
"""


import skype_info
import os
import threading
import erros as err

class SkypeEngine():
    def __init__(self):
        self.name = "skype"
        if skype_info.PATH == []:
            self.is_valid = False
        else:
            self.is_valid = True
        if self.is_valid:
            self.dir_path = os.getcwd() + "/saved/Skype/"
            if not os.path.exists(os.path.dirname(self.dir_path)):
                os.makedirs(os.path.dirname(self.dir_path))
            self.info_bank = {}

    def do(self, props):
        if props == 'all':
            t = threading.Thread(target=self.get_messages)
            t.start()
            t = threading.Thread(target=self.get_contacts)
            t.start()
            t = threading.Thread(target=self.get_accounts)
            t.start()
        else:
            if props['Accounts']:
                t = threading.Thread(target=self.get_accounts)
                t.start()
            if props['Messages']:
                t = threading.Thread(target=self.get_messages)
                t.start()
            if props['Contacts']:
                t = threading.Thread(target=self.get_contacts)
                t.start()

    def get_messages(self):
        messages = []
        f = open('logs/skype_erros.txt', 'a')
        for i in skype_info.PATH:
            mseg = skype_info.get_messages(i)
            if mseg[0] == 'err':
                err.error_handle([mseg[1:]], self.name)
            else:
                messages.append(mseg[0])
        if messages == []:
            err.error_handle([[201, str(skype_info.PATH)]], self.name)
        else:
            self.info_bank['messages'] = messages
            c = open(self.dir_path + "messages.txt",'w')
            c.write(str(self.info_bank['messages']))
            c.close()
        f.close()

    def get_accounts(self):
        accounts = []
        f = open('logs/skype_erros.txt', 'a')
        for i in skype_info.PATH:
            acc = skype_info.get_accounts(i)
            if acc[0] == 'err':
                err.error_handle([acc[1:]], self.name)
            else:
                accounts.append(acc[0])
        if accounts == []:
            err.error_handle([[202, str(skype_info.PATH)]], self.name)
        else:
            self.info_bank['accounts'] = accounts
            c = open(self.dir_path + "accounts.txt",'w')
            c.write(str(self.info_bank['accounts']))
            c.close()
        f.close()


    def get_contacts(self):
        contacts = []
        f = open('logs/skype_erros.txt', 'a')
        for i in skype_info.PATH:
            conc = skype_info.get_contacts(i)
            if conc[0] == 'err':
                err.error_handle([conc[1:]], self.name)
            else:
                contacts.append(conc[0])
        if contacts == []:
            err.error_handle([[203, str(skype_info.PATH)]], self.name)
        else:
            self.info_bank['contacts'] = contacts
            c = open(self.dir_path + "contacts.txt",'w')
            c.write(str(self.info_bank['contacts']))
            c.close()
        f.close()