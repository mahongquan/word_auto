# -*- coding: utf-8 -*-
import traceback
import os
import reg
import copyfile
import re
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

def first():
    global iscs
    import reg
    import dae
    copyfile.main(isonh)
    if isonh:
        try:
            dae.main(isonh)
        except:
            traceback.print_exc()
            a=input("error ")
def third():
    import pci
    try:
        pci.main()
    except:
        #a=input("except")
        traceback.print_exc()
        #traceback.print_stack()
        a=input("error ")
def last():
    import reg
    import on
    try:
        reg.main()
        on.main()
    except:
        #a=input("except")
        traceback.print_exc()
        #traceback.print_stack()
        a=input("error ")
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
    regcs()
def main():
    if (os.path.exists(destdrive+r"\CS3000备份")):
        #if os.path.exists(r"C:\ADLINK\PCIS-DASK"):
        #    third()
        installcs()
    else:
        copyfile.main(isonh)#copy 
        installcs()    
if __name__=="__main__":
    main()
