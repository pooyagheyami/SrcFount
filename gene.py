#In the name of GOD
#! use/bin/env python


import os
import wxsq

def Gnrat_name(name,phone,):
    lstmem = wxsq.wxsqltxt("SF.db","select * from member ")
    #print(lstmem)
    if lstmem == []:
        myid = 0
    else:
        myid = int(lstmem[-1][0])+1
        for itm in lstmem:
            if name in itm[1]:
                return ''
    #print(myid)
    dirct = str(myid)+name[:4]+str(phone[-4:])
    os.mkdir(os.getcwd()+"\\members\\"+dirct)
    return myid,dirct


