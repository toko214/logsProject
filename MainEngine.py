from Chrome import ChromeEngine as ce
from Skype import  SkypeEngine as se
from Firefox import FireFoxEngine as ff
from Programs_installed import programs_installed as pi
import threading
import datetime
import erros as err

class MainEngine:
    def __init__(self):
        pass

    def do(self, objs):
        f = open('logs/erros.txt','a')
        if objs['Chrome']['state'] > 0:
            ch_obj = ce.ChromeEngine()
            if ch_obj.is_valid:
                state = objs['Chrome']['state']
                arg = ""
                if state == 1:
                    arg = objs['Chrome']
                else:
                    arg = 'all'
                t = threading.Thread(target=ch_obj.do)
                t.start()
            else:
                f.write(str(datetime.datetime.now()) + "  "+err.errs[100])
        if objs['Skype']['state'] > 0:
            sky_obj = se.SkypeEngine()
            if sky_obj.is_valid:
                state = objs['Skype']['state']
                arg = ""
                if state == 1:
                    arg = objs['Skype']
                else:
                    arg = 'all'
                t = threading.Thread(target=sky_obj.do,args=(arg,))
                t.start()
            else:
                f.write(str(datetime.datetime.now()) + "  " + err.errs[200])
        if objs['Firefox']['state'] > 0:
            fire_obj = ff.FireFoxEngine()
            if fire_obj.is_valid:
                state = objs['Firefox']['state']
                arg = ""
                if state == 1:
                    arg = objs['Firefox']
                else:
                    arg = 'all'
                t = threading.Thread(target=ff.FireFoxEngine().do,args=(arg,))
                t.start()
            else:
                f.write(str(datetime.datetime.now()) + "  " + err.errs[300])
        if objs['Programs Installed']:
            pi.get_programs_installed()
        f.close()

