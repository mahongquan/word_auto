# -*- coding: utf-8 -*-
import time
import pywinauto
from pywinauto import *
import win32gui
import time
from pywinauto.timings import Timings, WaitUntil, TimeoutError, WaitUntilPasses
import win32process
import win32event
import os
import reg
import traceback
destdrive="C:"
bakdrive="C:"
#cspath = r'c:\Program Files\NCS\CS3000\NCS.exe'
cspath = 'C:\\Users\\ncs\\Desktop\\CS3000_1.6.18\\NCS.exe'
#cspath= r"D:\Documents and Settings\ncs\桌面\CS3000 1.6.19\NCS.exe"
#onhpath = r'c:\Program Files\NCS\ONH3000\NCS.exe'
onhpath = destdrive+ r'\Program Files (X86)\NCS\ONH3000\NCS.exe'
class ONH3000():
    def __init__(self):
        self.app = Application(backend="win32")
    def closeWin(self):
        dlg = self.app.top_window_()
        dlg.PostMessage(win32defines.WM_CLOSE)
        time.sleep(1.5)
        ext=self.app.window_(title=u"退出程序?")
        ext["Button1"].ClickInput()
    def startcs_login(self):
        ison=reg.ison()
        if ison:
            self.app.start(onhpath,3)
            w_login=self.app.top_window_()
            print(dir(w_login))
            w_login.print_control_identifiers()
            w_login[u"Edit1"].SetEditText("adjustor")
            w_login["ComboBox2"].click_input("left",(5,5))
            time.sleep(0.5)
            w_login["ComboBox2"].click_input("left",(15,55))
            time.sleep(0.5)
            w_login[u"Edit2"].SetEditText("ncschina")
            #time.sleep(5)
            w_login[u"登陆Button"].SetFocus()
            #time.sleep(5)
            w_login[u"登陆Button"].ClickInput()
            time.sleep(1.5)
        else:
            self.app.start(cspath,3)
            w_login=self.app.top_window_()
            print(dir(w_login))
            w_login.print_control_identifiers()
            w_login[u"Edit1"].SetEditText("adjustor")
            w_login["ComboBox2"].click_input("left",(5,5))
            time.sleep(0.5)
            w_login["ComboBox2"].click_input("left",(15,35))
            time.sleep(0.5)
            w_login[u"Edit2"].SetEditText("ncschina")
            #time.sleep(5)
            w_login[u"登陆Button"].SetFocus()
            #time.sleep(5)
            w_login[u"登陆Button"].ClickInput()
            time.sleep(1.5)
    def appByWindowHandle(self):
        try:
            win=findwindows.find_window(title=u"钢研纳克检测技术有限公司")
            self.app.connect(handle = win)
        except pywinauto.findwindows.WindowNotFoundError as e:
            self.startcs_login()
    def test(self):
        dlg = self.app.top_window_()
        print(dir(dlg))
        o=dlg.WrapperObject()
        print(dir(o))
        print(dlg.ClientRect())
        o.SetFocus()
        time.sleep(.5)
        img=o.CaptureAsImage()
        img.save("run.png")
    def openSample(self,nday,sampleName):
        dlg = self.app.top_window_()
        t=dlg["toolStrip1"].WrapperObject()
        t.set_focus()
        t.click_input(button=u'left', coords=(90, 10))
        time.sleep(1)
        selfwindow=self.app.window_(title=u"查询数据")
        selfwindow.print_control_identifiers()
        selfwindow[u"Edit4"].SetFocus()
        selfwindow[u"Edit4"].SetEditText(sampleName)
        selfwindow.Children()[22].SetFocus()
        for i in range(nday):
            selfwindow.Children()[22].ClickInput(button=u'left', coords=(5, 8))
        selfwindow[u"查询"].SetFocus()
        selfwindow[u"查询"].ClickInput()
        time.sleep(1)
        selfwindow[u"全选"].SetFocus()
        selfwindow[u"全选"].ClickInput()
        selfwindow[u"打开"].SetFocus()
        selfwindow[u"打开"].ClickInput()
def main():
    try:
        onh=ONH3000()
        onh.appByWindowHandle()
    except:
        #a=input("except")
        traceback.print_exc()
        #traceback.print_stack()
        a=input("error ")
if __name__=="__main__":
    main()