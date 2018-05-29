import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
#to plot for multiple days

def extract_data(dat):
    """read the excel file and extract out the amr and time cols"""
    
    #print(dat)
    amr = dat['AMR']
    time = dat['Time']
    
    return amr, time

def remove_duplicates(nars_data,nars_time):
    ndf = pd.DataFrame(columns = ['AMR','Opened','Closed','Timestamp','Time'])
    count = 0
    for i in range(0,len(nars_time)):
        if count!=0:
            i = count
        minute = nars_time[i].minute
        for k in range(i+1,len(nars_time)):
            if nars_time[k].minute == minute:
                continue
            else:
                ndf = ndf.append(nars_data.loc[i])
                count = k
                #print(i)
                break
    return ndf
"""
def normalize(time_nars,time_tun,dat_nars,dat_tun):
    #to normalize the time to a standard set
    norm_dat_nars = [] #data of nars according to new scale
    norm_dat_tun = [] #data of tun according to new scale
    norm_time = [] #standard time scale
    j = 0
    n = 0
    t = 0
    hour_count = -1
    
    for i in range(0,1440):
        if j==69:
            j=0
            hour_count+=1
        #print(i)
        if i<1372:
            if time_nars.iloc[i].minute == j and time_tun.iloc[i].minute == j :    
                #time = pd.Series(time_nars.iloc[i])
                norm_time.append(time_nars.iloc[i])
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                #n+=1
                #t+=1
            elif time_nars.iloc[i].minute == j and time_tun.iloc[i].minute !=j :
                #time = pd.Series(time_nars.iloc[i])
                norm_time.append(time_nars.iloc[i])
                n+=1
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                #n+=1
        
            elif time_nars.iloc[i].minute != j and time_tun.iloc[i].minute == j :
                #time = pd.Series(time_tun.iloc[i])
                norm_time.append(time_nars.iloc[i])
                t+=1
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                #t+=1
            else :
                st1 = str(hour_count) + ":" + str(j) + ":" + "00"
                #dtime = datetime.strptime(st1,'%H:%M:%S')
                norm_time.append(st1)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                
        elif i>=1372 and i<1423:
            #print(i)
            if time_nars.iloc[i].minute == j:
                #time = pd.Series(time_nars.iloc[i])
                norm_time.append(time_nars.iloc[i])
                n+=1
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                #n+=1
            else:
                st1 = str(hour_count) + ":" + str(j) + ":" + "00"
                #dtime = datetime.strptime(st1,'%H:%M:%S')
                norm_time.append(st1)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
        else:
            st1 = str(hour_count) + ":" + str(j) + ":" + "00"
            #dtime = datetime.strptime(st1,'%H:%M:%S')
            norm_time.append(st1)
            norm_dat_nars.append(dat_nars.iloc[n])
            norm_dat_tun.append(dat_tun.iloc[t])
        
        j+=1    
                        
    return norm_time, norm_dat_nars, norm_dat_tun
"""
def normalize_mod(time1,time2,dat1,dat2):
    #time is the base column.sAme in both
    columns = ['Opened','Closed','Timestamp','Time']
    dat1.drop(columns,inplace = True, axis =1)
    dat2.drop(columns, inplace = True, axis =1)
    df1 = pd.DataFrame(columns = ['AMR'])
    df2 = pd.DataFrame(columns = ['AMR'])
    dft = []
    #dft = pd.DataFrame(columns = ['Time'])
    n=0
    t=0
    j=0
    hour_count = 0
    for i in range(0,1440):
        if j==60:
            j=0
            hour_count+=1
        #print(i)
        if i<1372:
            if time1.iloc[n].minute == j and time2.iloc[t].minute == j :  
                #norm_time.append(time_nars.iloc[i])
                df1 = df1.append(dat1.iloc[i])
                df2 = df2.append(dat2.iloc[i])
                dft.append(time1.iloc[i])
                #dft.append(pd.Series(time1.iloc[i]), ignore_index=True)
                n=i
                t=i
                #print(i, "1st if")
                
            elif time1.iloc[n].minute == j and time2.iloc[t].minute !=j :
            
                df1 = df1.append(dat1.iloc[i])
                df2 = df2.append(dat2.iloc[t])
                #x = pd.Series(time1.iloc[i])
                #dft.append(pd.Series(time1.iloc[i]),ignore_index = True)
                dft.append(time1.iloc[i])
                n=i
                #n+=1
                #print(i, "2nd elif")
        
            elif time1.iloc[n].minute != j and time2.iloc[t].minute == j :
                #time = pd.Series(time_tun.iloc[i])
                #norm_time.append(time_nars.iloc[i])
                df1 = df1.append(dat1.iloc[n])
                df2 = df2.append(dat2.iloc[i])
                #x = pd.Series(time2.iloc[i])
                #dft.append(pd.Series(time2.iloc[i]),ignore_index=True)
                dft.append(time2.iloc[i])
                t=i
                #t+=1
                #print(i, "3rd elif")
            elif time1.iloc[n].minute != j and time2.iloc[t].minute != j :
                st1 = str(hour_count) + ":" + str(j) + ":" + "00"
                dtime = datetime.strptime(st1,'%H:%M:%S').time()
                #norm_time.append(st1)
                df1 = df1.append(dat1.iloc[n])
                df2 = df2.append(dat2.iloc[t])
                #dft.append(pd.Series(dtime), ignore_index=True)
                dft.append(dtime)
                #print(i, "4th else")
            else:
                continue
                
        elif i>=1372 and i<1423:
            #print(i)
            if time1.iloc[n].minute == j:
                #time = pd.Series(time_nars.iloc[i])
                df1 = df1.append(dat1.iloc[i])
                df2 = df2.append(dat2.iloc[t])
                #x = pd.Series(time1.iloc[i])
                dft.append(dtime)
                #dft.append(pd.Series(time1.iloc[i]),ignore_index = True)
                n=i
                #print(i, "elif greater than 1372")
            else:
                st1 = str(hour_count) + ":" + str(j) + ":" + "00"
                dtime = datetime.strptime(st1,'%H:%M:%S').time()
                df1 = df1.append(dat1.iloc[n])
                df2 = df2.append(dat2.iloc[t])
                dft.append(dtime)
                #dft.append(pd.Series(dtime), ignore_index=True)
                #print(i, "else > 1372")
                
        else:
            st1 = str(hour_count) + ":" + str(j) + ":" + "00"
            dtime = datetime.strptime(st1,'%H:%M:%S').time()
            df1 = df1.append(dat1.iloc[n])
            df2 = df2.append(dat2.iloc[t])
            dft.append(dtime)
            #print(i, "last eles")
            #dft.append(pd.Series(dtime), ignore_index=True)
        
        j+=1    
    
    return df1,df2,dft
    
def saveNewData(ndata, path):
    ndata.to_csv(path)

    
def plot_gallery(t1,r1,r2):
    plt.xlabel("Time(min) ->")
    plt.title("flow rate vs Time - 3days")
    plt.ylabel("Flow rate")
    #plt.grid(True)"""
    """
    slope1,coefficient1 = np.polyfit(nor_time,nar_amr,1)
    slope2,coefficient2 = np.polyfit(nor_time,tun_amr,1)
    """
    plt.plot(t1,r1,"r", label = "Tunivalasa")
    plt.plot(t1,r2,"b", label = "Narshapuram")
    plt.legend(loc = 'upper left')
    #plt.show()
    plt.savefig("Tun_Nars_3days.pdf")
    
def flow_rate(amr):
    fr = []
    k=0
    for i in range(0,3):
        for j in range(0,1440):
            if k+10 < 1440*(i+1):
                diff = (amr[k+10]-amr[k])/10
                fr.append(diff)
            else:
                fr.append(fr[k-1])
            k+=1
    return fr
    
#def no_to_time()    

df1 = pd.read_csv(r"G:\PS1\normalized_amr_tun20.csv")
df2 = pd.read_csv(r"G:\PS1\normalized_amr_tun21.csv")
df3 = pd.read_csv(r"G:\PS1\normalized_amr_tun22.csv")
df4 = pd.read_csv(r"G:\PS1\normalized_amr_nars20.csv")
df5 = pd.read_csv(r"G:\PS1\normalized_amr_nars21.csv")
df6 = pd.read_csv(r"G:\PS1\normalized_amr_nars22.csv")

frames1 = [df1, df2, df3]
frames2 = [df4, df5, df6]

result1 = pd.concat(frames1)
result2 = pd.concat(frames2)
list_dn1 = result1['AMR'].tolist()
list_dn2 = result2['AMR'].tolist()

time_num = [i for i in range(1,len(result1)+1)]

fr1 = flow_rate(list_dn1)
fr2 = flow_rate(list_dn2)

#plot_gallery(time_num,list_dn,list_dt)
plot_gallery(time_num,fr1,fr2)
#max flow rate of Nars - 2.7 - 22
#max flow rate of Tun - 5.6 - 22
#max flow rate of Nars - 2.8 - 20
#max flow rate of Tun - 5.8 - 20
#max flow rate of Nars - 5.0 - 21
#max flow rate of Tun - 5.6 - 21

#day1 - 0-1440
#day2 - 1440 - 2880
#day3 - 2880 - 4320
