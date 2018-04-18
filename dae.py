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
destdrive="C:"
bakdrive="C:"
def treatadlink(h):
    try:
        d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
        #print(dir(d))
        cs=d.children()
        d.set_focus()
        for c in cs:
            bt=c.window_text()
            if c.class_name()=="Button" and  "Install" in bt:
                c.set_focus()
                c.click_input()
            if c.class_name()=="Button" and "Next" in bt:
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
def treatcs3000setup(h):
    d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
    #print(dir(d))
    cs=d.children()
    for c in cs:
        if c.window_text()=="&Accept":
            c.set_focus()
            c.click_input()
    return True
def treatonh3000setup(h):
    d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
    #print(dir(d))
    cs=d.children()
    for c in cs:
        if c.window_text()=="&Accept":
            c.set_focus()
            c.click_input()
    return True    
def treatonh3000(h):
    d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
    iswelcom=False
    isselect=False
    button=None
    valid=False
    cs=d.children()
    for c in cs:
        #print(c.window_text())
        #print(c.class_name())
        if "Welcome to the ONH3000 Setup Wizard"==c.window_text():
            iswelcom=True
        if "Select Installation Folder"==c.window_text():
            isselect=True
        if c.class_name()=="Button" and ("Next" in c.window_text() or "Close" in c.window_text()):
            button=c
        if c.class_name()=="RichEdit20W":
            edit=c
    if iswelcom:
        button.set_focus()
        button.click_input()
        valid=True
    elif isselect:
        #s=r"c:\Program{SPACE}Files\NCS\ONH3000"
        s=destdrive+r"\Program{SPACE}Files\NCS\ONH3000"
        edit.set_focus() 
        edit.type_keys(s)
        button.set_focus()
        button.click_input()
        valid=True
    else:
        if button!=None:
            button.set_focus()
            button.click_input()
            valid=True
    return valid

def treatcs3000(h):
    d=pywinauto.controls.hwndwrapper.DialogWrapper(h)
    iswelcom=False
    isselect=False
    button=None
    valid=False
    cs=d.children()
    for c in cs:
        #print(c.window_text())
        #print(c.class_name())
        if "Welcome to the CS3000 Setup Wizard"==c.window_text():
            iswelcom=True
        if "Select Installation Folder"==c.window_text():
            isselect=True
        if c.class_name()=="Button" and ("Next" in c.window_text() or "Close" in c.window_text()):
            button=c
        if c.class_name()=="RichEdit20W":
            edit=c
    if iswelcom:
        button.set_focus()
        button.click_input()
        valid=True
    elif isselect:
        s=destdrive+ r"\Program{SPACE}Files\NCS\CS3000"
        #s=r"c:\Program{SPACE}Files\NCS\CS3000"
        edit.set_focus() 
        edit.type_keys(s)
        button.set_focus()
        button.click_input()
        valid=True
    else:
        if button!=None:
            button.set_focus()
            button.click_input()
            valid=True
    return valid
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
                        if title=="CS3000 Setup":
                            print("find:"+title)
                            if treatcs3000setup(win):
                                idle=0
                        if title=="ONH3000 Setup":
                            print("find:"+title)
                            if treatonh3000setup(win):
                                idle=0
                        if title=="ONH3000":
                            print("find:"+title)
                            if treatonh3000(win):
                                idle=0
                        elif title=="CS3000":
                            print("find:"+title)
                            if treatcs3000(win):
                                idle=0
                        elif "ADLINK PCIS-DASK" in title:
                            print("find:"+title)
                            if treatadlink(win):
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
    if os.path.exists(r"C:\ADLINK\PCIS-DASK"):
        return False
    else:
        _thread.start_new_thread(run,())
        return True
def run():
    #cmd=r"start c:\9111\PCIS-DASK\PCIS-DASK.exe"
    cmd="start "+bakdrive+"\\9111\\PCIS-DASK\\PCIS-DASK.exe"
    os.system(cmd)            
class EastWind(Thread):
    def __init__(self):
        Thread.__init__(self)
    def run(self):
        find3000()
def main(isonh):
    wind=EastWind()
    wind.start()
    if os.path.exists(destdrive+ r"\Program Files\NCS"):
    #if os.path.exists(r"c:\Program Files\NCS"):
        pass
    else:
        if isonh:
            #os.system(r"c:\ONH3000V2.1.33\setup.exe")
            os.system(bakdrive+ r"\ONH3000V2.1.33\setup.exe")
        else:
            #os.system(r"c:\CS3000v1.6.19\setup.exe")
            os.system(bakdrive+ r"\CS3000v1.6.19\setup.exe")
if __name__=="__main__":
    find3000()