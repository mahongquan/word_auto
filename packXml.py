from lxml import etree as ET
from io import BytesIO,StringIO
import pickle
addSerial=0
def addStart(start):
    global addSerial
    addSerial+=1
    if addSerial % 2==0:
        start+=1
    return start
def getGrid(tbl,rowv,colv):
    tbl_childs=tbl.getchildren()
    row1=tbl_childs[rowv+2]
    columns=row1.getchildren()[1:]
    print(columns)
    column1=columns[colv]
    cell=column1.getchildren()[1]
    paras=cell.getchildren()[1:]
    r=[]
    for p in paras:
        r.append(p.getchildren()[1].text)
    return "".join(r)
def getGrid2(tbl,rowv,colv):
    tbl_childs=tbl.getchildren()
    row1=tbl_childs[rowv+2]
    columns=row1.getchildren()
    column1=columns[colv]
    cell=column1.getchildren()
    para=cell[1].getchildren()[1]
    para=para.getchildren()[0].text
    return para
def getElement(chanels,first):
    eles=first.split("(")
    ele=eles[0]#2C
    if ele[0]=="2":
        chanels.append("L"+ele[1])
        chanels.append("H"+ele[1])
    else:
        ele_set=eles[1][:-1]#移去括号
        print(ele_set)
        if ele_set[0]=="高":
            chanels.append("H"+ele[1])
        else:
            chanels.append("L"+ele[1])
    pass
def getPeizhi(start,fn):
    tree = ET.parse(fn)
    root = tree.getroot()#{http://schemas.microsoft.com/office/word/2003/wordml}wordDocument
    #{http://schemas.microsoft.com/office/2006/xmlPackage}package
    #{http://schemas.microsoft.com/office/2006/xmlPackage}part
    #{http://schemas.microsoft.com/office/2006/xmlPackage}xmlData
    #{http://schemas.openxmlformats.org/package/2006/relationships}Relationships
    #body=root.find("{http://schemas.microsoft.com/office/word/2003/wordml}body")
    body=root.getchildren()[2].getchildren()[0].getchildren()[0].getchildren()[0]
    cs=body.getchildren()
    ps=cs[:-1]
    for p in ps:
	    print("p children len",len(p.getchildren()))
	    at=5
	    #print(txbxContent.getchildren()[0].getchildren()[0].getchildren()[1].text) #第一联
	    txbxContent=p.getchildren()[at].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[0]
	    # bkd=txbxContent.getchildren()[2].getchildren()[1].getchildren()[1] #北京科技大学
	    # yu=txbxContent.getchildren()[2].getchildren()[2].getchildren()[1] #预

	    # print(txbxContent.getchildren()[2].getchildren()[3].getchildren()[1].text) #收款凭
	    # print(txbxContent.getchildren()[2].getchildren()[4].getchildren()[1].text) #条
	    # print(txbxContent.getchildren()[2].getchildren()[5].getchildren()[1].text) #No
	    runs=txbxContent.getchildren()[2].getchildren()
	    for i in range(len(runs)):
	    	print(i,runs[i].getchildren()[1].text)
	    runs[5].getchildren()[1].text="No  0018%04d" %start
	    i=6
	    while(i<len(runs)):
	        runs[i].getchildren()[1].text=""
	        i+=1
	    start=addStart(start)
	    at=4
	    txbxContent=p.getchildren()[at].getchildren()[1].getchildren()[0].getchildren()[0].getchildren()[0]
	    runs=txbxContent.getchildren()[2].getchildren()
	    for i in range(len(runs)):
	    	print(i,runs[i].getchildren()[1].text)
	    runs[5].getchildren()[1].text="No  0018%04d" %start
	    i=6
	    while(i<len(runs)):
	        runs[i].getchildren()[1].text=""
	        i+=1
	    start=addStart(start)
    s=BytesIO()
    tree.write(s, encoding="gb2312", xml_declaration=True, method="xml")
    s.seek(0)
    data=s.read()
    data=data.decode('gb2312')
    data= data.replace('\n', '\r\n')
    print("新生成文件名称out.xml,文件格式为word xml")
    f=open("out.xml","w")
    f.write(data)
    f.close()
    pickle.dump(start, open("start.pickle","wb"), protocol=None)    
if __name__=="__main__":
    pass