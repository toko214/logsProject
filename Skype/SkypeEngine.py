"""
author: Tomer Perets
date: 5.5.2018
this file uses the skype_info to get the data from skype.
"""


import skype_info
import os
import datetime
import threading
import erros as err

class SkypeEngine():
    def __init__(self):
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
        print "k"
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
                st = "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[mseg[1]] + " - " + mseg[2] + "\r\n"
                if len(mseg) > 3:
                    for j in mseg[3:]:
                        st += " - " + str(j) + "\r\n"
                f.write(st + "-----------------\r\n")
            else:
                messages.append(mseg[0])
        if messages == []:
            f.write("-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + "No Skype Messages from all skype paths\r\n-----------------\r\n")
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
                st = "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[acc[1]] + " - " + acc[2] + "\r\n"
                if len(acc) > 3:
                    for j in acc[3:]:
                        st += " - " + str(j) + "\r\n"
                f.write(st + "-----------------\r\n")
            else:
                accounts.append(acc[0])
        if accounts == []:
            f.write("-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + "No Skype Accounts from all skype paths\r\n-----------------\r\n")
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
                st = "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + err.errs[conc[1]] + " - " + conc[2] + "\r\n"
                if len(conc) > 3:
                    for j in conc[3:]:
                        st += " - " + str(j) + "\r\n"
                f.write(st + "-----------------\r\n")
            else:
                contacts.append(conc[0])
        if contacts == []:
            f.write("-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + "No Skype Contacts from all skype paths\r\n-----------------\r\n")
        else:
            self.info_bank['contacts'] = contacts
            c = open(self.dir_path + "contacts.txt",'w')
            c.write(str(self.info_bank['contacts']))
            c.close()
        f.close()