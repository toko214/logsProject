import datetime

errs = {}
errs[0] = "no chrome password database"
errs[1] = "[-] No results returned from query"
errs[2] = "no chrome history database"
errs[3] = "no chrome bookmark file"
errs[4] = "no chrome cookie fle"
errs[5] = "You will die if you will wait....."
errs[6] = "no chrome cache file"
errs[7] = "no firefox bookmarks file"
errs[8] = "no firefox history file"
errs[9] = "no firefox cookie file"
errs[10] = "no chrome cache"
errs[11] = "skype not installed or not in a default location"
errs[12] = "yogev is japanese"
errs[13] = "database file is empty"
errs[100] = "chrome not installed"
errs[200] = "skype not installed"
errs[201] = "No Skype Messages from all skype paths"
errs[202] = "No Skype Accounts from all skype paths"
errs[203] = "No Skype Contacts from all skype paths"
errs[300] = "firefox not installed"

def error_handle(errors, engine):
    st = ""
    for err in errors:
        st += "-----------------\r\n" + str(datetime.datetime.now()) + "\r\n" + errs[err[0]] + " - " + err[1]+ "\r\n"
        if len(err) > 3:
            for i in err[3:]:
                st += " - " + str(i) + "\r\n"
            st += "-----------------\r\n"
    f = open("logs/" + engine + "_erros.txt", 'a')
    f.write(st)
    f.close()