import sys
import win32com.client 
import pywintypes
import win32gui
from getpath import getpath
initpath=getpath()
sys.path.insert(0,initpath+"\Lib")
print(sys.path)
from main2 import main
main()