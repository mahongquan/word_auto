import pywinauto
from pywinauto import *
import win32gui
import time
from pywinauto.timings import Timings, WaitUntil, TimeoutError, WaitUntilPasses
import win32process
import win32event
class Install3000:
    def __init__(self,ison):
        self.ison=ison
        if self.ison:
            self.csonh="ONH"
        else:
            self.csonh="CS"
    def closeWin(self):
        dlg = self.top_window_()
        dlg.PostMessage(win32defines.WM_CLOSE)
        time.sleep(1)
        ext=self.window_(title=u"退出程序?")
        #print "------------"
        #print ext,dir(ext)
        ext["Button1"].ClickInput()
        #ext.print_control_identifiers()
        #[u"是"].ClickInput()
    def startDotnet(self):
        if self.ison:
            self.app = Application(backend="win32").start(r"e:\ONH3000V2.1.31\setup.exe",3)
            time.sleep(3)
            w_login=self.app.window_(title=u"ONH3000 Setup")
        else:
            self.app = Application(backend="win32").start(r"e:\CS3000\setup.exe",3)
            time.sleep(3)
            w_login=self.app.window_(title=u"CS3000 Setup")

        #print ("["+w_login.criteria[-1]["title"]+"]")

        print(self.app.windows())
        print(w_login)
        w_login.print_control_identifiers()
        w_login["Accept"].SetFocus()
        time.sleep(1)
        w_login["Accept"].ClickInput()
        self.startcs()
    def findyonghu(self):
        while (True):
            time.sleep(1)
            try:
                win=findwindows.find_window(title="用户账户控制")
                win["是"].ClickInput()
                print(win)
                break
            except pywinauto.findwindows.WindowNotFoundError as e:
                print("no")
    def continueCS(self,w_login):
        print("============================continueCS")
        print(w_login,dir(w_login))
        bw=w_login["Next"]
        button=bw.WrapperObject()
        button.set_focus()
        time.sleep(1)
        button.click_input()
        time.sleep(1)
        w_login=self.app.top_window_()
        e=w_login.Edit.wrapper_object()
        e.TypeKeys("d:\\Program Files\\NCS\\%s3000\\" % self.csonh)
        time.sleep(1)
        w_login=self.app.top_window_()
        w_login["Next"].ClickInput()
        time.sleep(1)
        w_login=self.app.top_window_()
        w_login["Next"].ClickInput()
    def startcs(self):
        self.find3000()
        if self.ison:
            w_login=self.window_(title=u"ONH3000")
        else:
            w_login=self.window_(title=u"CS3000")
        time.sleep(1)
        self.continueCS()
    def find3000(self):
        while(True):
            try:
                if self.ison:
                    wins=findwindows.find_windows(title=u"ONH3000")
                else:
                    wins=findwindows.find_windows(title=u"CS3000")
                for win in wins:
                    print(handleprops.text(win))
                    print(dir(self))
                    self.app = Application(backend="win32")
                    self.app.connect(handle = win)
                    #print(dir(self.window_))
                    break
                break
            except  pywinauto.findwindows.WindowNotFoundError as e:
                time.sleep(1)
        if self.ison:
            w=self.app.window_(title=u"ONH3000")
        else:
            w=self.app.window_(title=u"CS3000")
        #w.print_control_identifiers()
        self.continueCS(w)
    def appByWindowHandle(self):
        pass
        # try:
            # win=findwindows.find_window(title=u"钢研纳克检测技术有限公司")
            # #print win
            # self.connect_(handle = win)
        # except  pywinauto.findwindows.WindowNotFoundError e:
            # self.startcs_login()