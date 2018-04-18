import pywinauto
from pywinauto import *
import win32gui
import time
from pywinauto.timings import Timings, WaitUntil, TimeoutError, WaitUntilPasses
import win32process
import win32event
import os
from subprocess import Popen
from pywinauto.timings import always_wait_until_passes
def findUpdate():
    wins=findwindows.find_windows()
    for win in wins:
        try:
            title=handleprops.text(win)
            print(handleprops.text(win))
            if "更新驱动" in title:
                return win
        except UnicodeEncodeError as e:
            pass
    return None
def findPCI():
    wins=findwindows.find_windows()
    for win in wins:
        try:
            title=handleprops.text(win)
            print(handleprops.text(win))
            if "PCI 数据" in title:
                return win
        except UnicodeEncodeError as e:
            pass
    return None

class AccessDeniedError(Exception):
    """Raise when current user is not an administrator."""
    def __init__(self, arg):
        self.args = arg


class NoExistGroupError(Exception):
    """Raise when group Administrators is not exist."""
    def __init__(self, arg):
        self.args = arg


def is_user_an_admin():
    """ Check user admin """
    import os
    if os.name == 'nt':
        try:
            # only windows users with admin privileges can read the C:\windows\temp
            os.listdir(os.sep.join([os.environ.get('SystemRoot', 'C:\\windows'), 'temp']))
        except Exception:
            return False
        else:
            return True
    else:
        return 'SUDO_USER' in os.environ and os.geteuid() == 0

def main():
    if is_user_an_admin():
        Popen(['devmgmt.msc'], shell=True)


        @always_wait_until_passes(4, 2, application.ProcessNotFoundError)
        def connect_to_mmc():
            """ Returns connect app to instance """
            return application.Application().connect(path="mmc.exe")


        app = connect_to_mmc()
        tree = app.mmc_main_frame.tree_view
        p6208 = tree.get_item('\\ncs-PC\\其他设备')#\\PCI6208 Device')
        print(p6208,dir(p6208))
        cs=p6208.children()
        cs[0].click_input("left",True)
        time.sleep(1)
        h=findPCI()
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        cs=d.children()
        for c in cs:
            if c.class_name()=="Button" and "更新驱动" in c.window_text():
                print("click upgrade")
                c.set_focus()
                c.click_input()
        time.sleep(1)
        h=findUpdate()
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        cs=d.children()
        for c in cs:
            if c.class_name()=="Button" and "自动搜索更新的驱动程序软件" in c.window_text():
                print("click search")
                c.set_focus()
                c.click_input()
        ##########
        p6208 = tree.get_item('\\ncs-PC\\其他设备')#\\PCI6208 Device')
        print(p6208,dir(p6208))
        cs=p6208.children()
        cs[0].click_input("left",True)
        time.sleep(1)
        h=findPCI()
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        cs=d.children()
        for c in cs:
            if c.class_name()=="Button" and "更新驱动" in c.window_text():
                print("click upgrade")
                c.set_focus()
                c.click_input()
        time.sleep(1)
        h=findUpdate()
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        cs=d.children()
        for c in cs:
            if c.class_name()=="Button" and "自动搜索更新的驱动程序软件" in c.window_text():
                print("click search")
                c.set_focus()
                c.click_input()
    else:
        print('\nYou are not an administrator')
if __name__=="__main__":        
    main()