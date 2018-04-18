# -*- coding: utf-8 -*-
import time
import os
import re
import on
import exp
import getpath
destdrive="C:"
bakdrive="C:"
def mylistdir(p,f):
    a=os.listdir(p)
    fs=myfind(a,f)
    return(fs)
def myfind(l,p):
    lr=[];
    #print p
    p1=p.replace(".",r"\.")
    p2=p1.replace("*",".*")
    p2=p2+"$"
    p2="^"+p2
    for a in l:
        #print a
        if  re.search(p2,a,re.IGNORECASE)==None :
           pass
           #print "pass"
        else:
           lr.append(a)
       #print "append"
    return lr
def ison():
    rundir=os.path.abspath(os.curdir)
    bh=rundir.split("\\")[-1]
    print(bh)
    if bh[:3]=="411":
        iscs=True
    else:
        iscs=False
    return not iscs
def getbh():
    rundir=os.path.abspath(os.curdir)
    bh=rundir.split("\\")[-1]
    return bh
def main():
    curpath=getpath.getpath()
    hm=getbh()
    hm=hm[-8:]
    if not ison():
        fs=mylistdir("../CS","*.ini")
        fn="..\\CS"
        #cmd='xcopy /s /Y  %s "c:\\Program Files\\NCS\\CS3000\\CS\\"' % fn
        cmd='xcopy /s /Y  %s "%s\\Program Files (X86)\\NCS\\CS3000\\CS\\"' % (fn,destdrive)
        print(cmd)
        os.system(cmd)
        cmd=curpath+"\\LicenseManager.exe %s 80" % hm
        print(cmd)
        os.system(cmd)
        #cmd='xcopy /Y sfx.db3 "c:\\Program Files\\NCS\\CS3000\\"'
        cmd='xcopy /Y sfx.db3 "'+destdrive+'\\Program Files (X86)\\NCS\\CS3000\\"'
        print(cmd)
        os.system(cmd)
    else:
        fn="..\\ON"
        fs=mylistdir("../ON","*.ini")
        #cmd='xcopy /s /Y  %s "c:\\Program Files\\NCS\\ONH3000\\ON\\"' % fn
        cmd='xcopy /s /Y  %s %s\\Program Files (X86)\\NCS\\ONH3000\\ON\\"' % (fn,destdrive)
        os.system(cmd)
        fn="Configs.db"
        #cmd='xcopy  /Y  %s "c:\\Program Files\\NCS\\ONH3000\\"' % fn
        cmd='xcopy  /Y  %s %s\\Program Files (X86)\\NCS\\ONH3000\\"' % (fn,destdrive)
        os.system(cmd)
        cmd=curpath+"\\LicenseManager.exe %s 80" % hm
        os.system(cmd)
        #cmd='xcopy /Y sfx.db3 "c:\\Program Files\\NCS\\ONH3000\\"'
        cmd='xcopy /Y sfx.db3 "'+destdrive+'\\Program Files (X86)\\NCS\\ONH3000\\"'
        os.system(cmd)
    #exp.main()
    #on.main()

if __name__=="__main__":
    main()
