# -*- coding: utf-8 -*-
import reg
import installcs
import installonh
def main():
    isonh=reg.ison()
    if isonh:
        installonh.main()
    else:
        installcs.main()
# def symlink(source, link_name):
#     '''symlink(source, link_name)
#        Creates a symbolic link pointing to source named link_name'''
#     import ctypes
#     csl = ctypes.windll.kernel32.CreateSymbolicLinkW
#     csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
#     csl.restype = ctypes.c_ubyte
#     flags = 0
#     if source is not None and os.path.isdir(source):
#         flags = 1
#     if csl(link_name, source, flags) == 0:
#         raise ctypes.WinError()
# def symlink2():
#     import ctypes
#     kdll = ctypes.windll.LoadLibrary("kernel32.dll")
#     kdll.CreateSymbolicLinkA("main2.py", "main2.link.py", 0)
# def symlink3():
#     import win32file
#     win32file.CreateSymbolicLinkW(U"main2.py",U"main2.link.py", 1)
# def symlink4():
#     from subprocess import call
#     call(['mklink', 'main2.link.py', 'main2.py'], shell=True)
# def testlink():
#     #symlink("main2.py","main2.py.link")
#     symlink4()
if __name__=="__main__":
    main()
    #testlink()