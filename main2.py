# -*- coding: utf-8 -*-
#import docx_write
import packXml
import pickle
import os
def getold():
	if os.path.exists("start.pickle"):
		old=open("start.pickle","rb").read()
		start=pickle.loads(old)
		return start
	else:
		return None
def main():
	start_old=getold()
	if start_old!=None:
		print("上次打印到"+str(start_old)+"号,直接回车接着上次打印")
	else:
		start_old=1
	start=input("开始号码：")
	try:
		start=int(start)
	except ValueError as e:
		start=start_old
	print(start)
	packXml.getPeizhi(start,"横向收据模板.xml")#xml 2003 file
if __name__=="__main__":
    main()
    #testlink()