import pywinauto
import pywintypes
from pywinauto import *
import win32gui
import time
from pywinauto.timings import Timings, WaitUntil, TimeoutError, WaitUntilPasses
import win32process
import win32event
from threading import Thread
import os
import time
import _thread
import traceback
from threading import Thread,Event
import time
destdrive="C:"
bakdrive="C:"
program=None
def runUSB():
    #cmd=r"start c:\9111\PCIS-DASK\PCIS-DASK.exe"
    cmd="start c:\\CS3000备份\\CDM21216_Setup.exe"
    os.system(cmd)      
class Program(object):
    """example for AutoResetEvent"""
    def main(self):
        _thread.start_new_thread(runUSB,())
        wind=EastWind(self.mre)
        wind.start()
        self.mre.wait()
        print("got wind")
        # self.mre.clear() 
        # self.mre.wait()
        # print("got wind")
    def __init__(self):
        super(Program, self).__init__()
        self.mre=Event()#False)
class EastWind(Thread):
    """dmretring for EastWind"""
    def __init__(self, mreV):
        super(EastWind, self).__init__()
        self.mre=mreV
    def run(self):
        find3000()
        self.mre.set()
def treatadlink(h):
    try:
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        #print(dir(d))
        cs=d.children()
        d.set_focus()
        for c in cs:
            bt=c.window_text()
            if c.class_name()=="Button" and  "Extract" in bt:
                c.set_focus()
                c.click_input()
            if c.class_name()=="Button" and "下一步" in bt:
                c.set_focus()
                c.click_input()            
            if c.class_name()=="Button" and  "Finish" in bt:
                c.set_focus()
                c.click_input()            
            if c.class_name()=="Button" and  "No" in bt:
                c.set_focus()
                c.click_input() 
    except pywintypes.error as e:
        pass
    return True
def treatQudong(h):
    try:
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        #print(dir(d))
        cs=d.children()
        d.set_focus()
        for c in cs:
            bt=c.window_text()
            if c.class_name()=="Button" and  "我接受" in bt:
                c.set_focus()
                c.click_input()            
            if c.class_name()=="Button" and "下一步" in bt:
                c.set_focus()
                c.click_input()   
            # if c.class_name()=="Button" and "完成" in bt:
            #     c.set_focus()
            #     c.click_input()            
            # if c.class_name()=="Button" and  "No" in bt:
            #     c.set_focus()
            #     c.click_input() 
    except pywintypes.error as e:
        pass
    return True    
def find3000():
    idle=0
    while(True):
        print("=================")
        try:
            wins=findwindows.find_windows()
            for win in wins:
                try:
                    title=handleprops.text(win)
                    print(title)
                    if title!=None:
                        if "FTDI" in title:
                            print("--------------------find:"+title)
                            if treatadlink(win):
                                idle=0
                        elif "设备驱动程序" in title:
                            print("、、、、、、、、、、、find:"+title)
                            if treatQudong(win):
                                idle=0
                except UnicodeEncodeError as e:
                    pass
            time.sleep(1)
            idle+=1
            if idle>5 :
                if not nextCmd():
                    break
                else:
                    idle=-10
            if idle>20:
                break
        except:
            traceback.print_exc()
            a=input("except")
            
def nextCmd():
    return False
def run():
    #cmd=r"start c:\9111\PCIS-DASK\PCIS-DASK.exe"
    cmd="start "+bakdrive+"\\9111\\PCIS-DASK\\PCIS-DASK.exe"
    os.system(cmd)            
# class EastWind(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#     def run(self):
#         find3000()
def main():
    global program
    program=Program()
    program.main()
if __name__=="__main__":
    find3000()