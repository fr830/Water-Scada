#It takes data first tuple in repeated time(REMOVING REPEATED DATA)**************************

from openpyxl import workbook,load_workbook
import pandas as pd
import numpy as np
wb = load_workbook(r'C:\Users\anish\Desktop\python_excel\RELIPETA DAY 03.xlsx')
ws = wb.active
df = pd.DataFrame(ws.values)
df[3] = pd.to_datetime(df[3], format='%d/%b/%Y:%H:%M', utc=True)
rows_list = []
for index,row in df.iterrows():
    if index==0:
        rows_list.append(row)
    elif temp!=row[3]:
        rows_list.append(row)
    temp = row[3]
df = pd.DataFrame(rows_list)
#df.reset_index()
#print('Hello\n')
#print(df)
##print('HI\n')
#print(df)
df.to_csv(r'C:\Users\anish\Desktop\python_excel\final2relliinit.csv')


#ADDING DATA(OR NORMALISNG)*******************************************
initialtime = df.ix[0][3]
initialhour = df.ix[0][3].hour
initialminute = df.ix[0][3].minute
initialamr =df.ix[0][2]
newrows_list = []
templist =[]
for index,row in df.iterrows():
    pine = row[3]
    hour = row[3].hour
    minute = row[3].minute
    amr = row[2]
    if index==0:
        dic= {}
        dic['SITE'] = row[0]
        dic['CAPACITY'] = row[1]
        dic['AMR'] = row[2]
        dic['time'] = row[3]
        dic['OPEN'] = row[4]
        dic['CLOSE'] = row[5]
        newrows_list.append(dic)
    else:
        temp1 = hour-initialhour
        temp2 = minute- initialminute
        if temp1==0 and temp2==1:
            dic= {}
            dic['SITE'] = row[0]
            dic['CAPACITY'] = row[1]
            dic['AMR'] = row[2]
            dic['time'] = row[3]
            dic['OPEN'] = row[4]
            dic['CLOSE'] = row[5]
            newrows_list.append(dic)
        elif temp1==0:
            print(minute,initialminute,initialamr,amr,hour,initialhour)
            for i in range(1,temp2):
                prow ={}
                prow = row
                time = initialtime
                hello = initialminute
                time = time.replace(minute =hello+i)
                prow[3] = time
                prow[2] = initialamr
                prow['name'] = index
                print(prow[3])
                dic= {}
                dic['SITE'] = prow[0]
                dic['CAPACITY'] = prow[1]
                dic['AMR'] = prow[2]
                dic['time'] = prow[3]
                dic['OPEN'] = prow[4]
                dic['CLOSE'] = prow[5]
                newrows_list.append(dic)
                templist.append(dic)
                #print(index)
                #index = index+1
            print('endfor')
            row[3] = pine
            row[2] = amr
            print(dic,"TEST")
            dic= {}
            dic['SITE'] = row[0]
            dic['CAPACITY'] = row[1]
            dic['AMR'] = row[2]
            dic['time'] = row[3]
            dic['OPEN'] = row[4]
            dic['CLOSE'] = row[5]
            newrows_list.append(dic)
        elif temp1>0:
            bighour = initialhour
            bigmin = initialminute
            bigtemp = temp1
            bigtime= initialtime
            while bigtemp>0:
                if bigtemp==0:
                    check = minute-bigmin
                else:
                    check=60-bigmin
                for i in range(bigmin,check):
                    prow ={}
                    prow = row
                    time = bigtime
                    hello = bigmin
                    time = time.replace(minute =hello+i)
                    prow[3] = time
                    prow[2] = initialamr
                    prow['name'] = index
                    print(prow[3])
                    dic= {}
                    dic['SITE'] = prow[0]
                    dic['CAPACITY'] = prow[1]
                    dic['AMR'] = prow[2]
                    dic['time'] = prow[3]
                    dic['OPEN'] = prow[4]
                    dic['CLOSE'] = prow[5]
                    newrows_list.append(dic)
                    templist.append(dic)
                bigtime = bigtime.replace(hour =bighour+1)
                bighour = bighour+1
                bigtemp = bigtemp-1
                bigmin = 0

            print('endfor2')
            row[3] = pine
            row[2] = amr
            print(dic,"TEST")
            dic= {}
            dic['SITE'] = row[0]
            dic['CAPACITY'] = row[1]
            dic['AMR'] = row[2]
            dic['time'] = row[3]
            dic['OPEN'] = row[4]
            dic['CLOSE'] = row[5]
            newrows_list.append(dic)
    initialtime = row[3]
    initialhour = pine.hour
    initialminute = pine.minute
    initialamr = amr

df = pd.DataFrame(newrows_list)
df.to_excel(r'C:\Users\anish\Desktop\python_excel\final2relli.xlsx')
df.to_csv(r'C:\Users\anish\Desktop\python_excel\final2relli.csv')
df = pd.DataFrame(templist)
#print(templist)
df.to_csv(r'C:\Users\anish\Desktop\python_excel\final2rellitemp.csv')
