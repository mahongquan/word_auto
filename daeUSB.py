# -*- coding: utf-8 -*-
#安装USB2COM驱动
import pywinauto
import pywintypes
from pywinauto import findwindows,handleprops
import os
import _thread
import traceback
from threading import Thread,Event
import time
def runUSB():
    #cmd=r"start c:\9111\PCIS-DASK\PCIS-DASK.exe"
    cmd="start c:\\CS3000备份\\CDM21216_Setup.exe"
    os.system(cmd)      
class Program(object):
    """example for AutoResetEvent"""
    def main(self):
        _thread.start_new_thread(runUSB,())#start program
        wind=EastWind(self.mre)
        wind.start()
        self.mre.wait()#wait install finish
    def __init__(self):
        super(Program, self).__init__()
        self.mre=Event()
class EastWind(Thread):
    """dmretring for EastWind"""
    def __init__(self, mreV):
        super(EastWind, self).__init__()
        self.mre=mreV
    def run(self):
        lookupWindow()#installing
        self.mre.set()#install finish
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
        print(e)
        pass
    except TypeError as e:
        print(e)

    return True
def treatQudong(h):
    try:
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        #print(dir(d))
        cs=d.children()
        d.set_focus()
        for c in cs:
            bt=c.window_text()
            if(bt!=None):
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
        print(e)
        pass
    return True    
def lookupWindow():
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
                    print(e)
                    pass
            time.sleep(1)#每秒检查一次
            idle+=1
            if idle>5 :#连续五秒没有查找到窗口则退出
                break
        except:
            traceback.print_exc()
            a=input("except")
def main():
    program=Program()
    program.main()
if __name__=="__main__":
    lookupWindow()