# -*- coding: utf-8 -*-
import traceback
import os
import reg
import copyfile
import re
import getpath
import on
import daeUSB
import mklink

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
def getbh():
    rundir=os.path.abspath(os.curdir)
    bh=rundir.split("\\")[-1]
    return bh            
def regcs():
    curpath=getpath.getpath()
    hm=getbh()
    hm=hm[-8:]
    fs=mylistdir("../CS","*.ini")
    fn="..\\CS"
    #cmd='xcopy /s /Y  %s "c:\\Program Files\\NCS\\CS3000\\CS\\"' % fn
    cmd='xcopy /s /Y  %s "C:\\Users\\ncs\\Desktop\\CS3000_1.6.18\\"' % (fn)
    print(cmd)
    os.system(cmd)
    cmd=curpath+"\\LicenseManager.exe %s 80" % hm
    print(cmd)
    os.system(cmd)
    #cmd='xcopy /Y sfx.db3 "c:\\Program Files\\NCS\\CS3000\\"'
    cmd='xcopy /Y sfx.db3 "C:\\Users\\ncs\\Desktop\\CS3000_1.6.18\\"'
    print(cmd)
    os.system(cmd)
def installcs():
    cmd='xcopy /s "C:\\CS3000备份\\CS3000_1.6.18" C:\\Users\\ncs\\Desktop\\CS3000_1.6.18\\'
    print(cmd)
    if os.path.exists("C:\\Users\\ncs\\Desktop\\CS3000_1.6.18"):
        pass
    else:
        os.system(cmd)            
def installDriver():
    try:
        daeUSB.main()
    except:
        traceback.print_exc()
        a=input("error ")
def main():
    # regcs()
    mklink.main()
    return
    if (os.path.exists(destdrive+r"\CS3000备份")):
        #if os.path.exists(r"C:\ADLINK\PCIS-DASK"):
        #    third()
        installDriver()
        installcs()
        mklink.main()
        regcs()
        on.main()#start ncs.exe
    else:
        copyfile.main(False)#copy 
        installDriver()
        installcs()  
        mklink.main()  
        regcs()
        on.main()#start ncs.exe
if __name__=="__main__":
    main()
