import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
#to plot for a single day

def extract_data(dat):
    """read the excel file and extract out the amr and time cols"""
    
    #print(dat)
    amr = dat['AMR']
    time = dat['Time']
    
    return time, amr

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
    plt.xlabel("Time ->")
    plt.title("flow rate vs Time - 21st")
    plt.ylabel("Flow rate")
    #plt.grid(True)"""
    """
    slope1,coefficient1 = np.polyfit(nor_time,nar_amr,1)
    slope2,coefficient2 = np.polyfit(nor_time,tun_amr,1)
    """
    plt.plot(t1,r1,"b", label = "Narsaparum")
    plt.plot(t1,r2,"r", label = "Tunivalasa")
    plt.legend(loc = 'upper left')
    #plt.show()
    plt.savefig("flowt.pdf")
    
def flow_rate(amr):
    fr = []
    for i in range(0,1440):
        if i+10 < 1440:
            diff = (amr[i+10]-amr[i])/10
            fr.append(diff)
        else:
            fr.append(fr[i-1])
    return fr
    
#def no_to_time()    

dat_nars = pd.read_excel(r"G:\PS1\NSP_OHSR.xlsx")
dat_tun = pd.read_excel(r"G:\PS1\Tunivalasa.xlsx")
#dropping columns not required
to_drop = ['PLC','Site','Capacity','HM']
dat_nars.drop(to_drop,inplace=True,axis=1)
#dat_tun.drop(to_drop,inplace=True,axis=1)

nars_time,nars_amr = extract_data(dat_nars)
tun_time,tun_amr = extract_data(dat_tun)

"""call for cleaning the data;commented as clean data already received
No need to save every time program is ran"""

new_data_nars = remove_duplicates(dat_nars,nars_time)
new_data_tun = remove_duplicates(dat_tun,tun_time)

saveNewData(new_data_nars,r"G:\PS1\clean_data_nars.csv")
saveNewData(new_data_tun,r"G:\PS1\clean_data_tun.csv")
new_nars_time, new_nars_amr = extract_data(new_data_nars)
new_tun_time, new_tun_amr = extract_data(new_data_tun)
#new_nars_time = new_nars_time.reindex(ind1)
#new_nars_time = new_nars_time.rename(lambda x: x)
#new_tun_time = new_tun_time.reindex(ind2)
#"""
normalized_dn, normalized_dt, normalized_time = normalize_mod(new_nars_time, new_tun_time, new_data_nars,new_data_tun)
df_norm_time = pd.DataFrame({'Time':normalized_time})#normalzd_time is a list
#"""
"""saving the dataframes into csv files"""
saveNewData(normalized_dn,r"G:\PS1\normalized_amr_nars.csv")
saveNewData(normalized_dt,r"G:\PS1\normalized_amr_tun.csv")
saveNewData(df_norm_time,r"G:\PS1\normalized_time.csv")

#"""
list_dn = normalized_dn['AMR'].tolist()
list_dt = normalized_dt['AMR'].tolist()
time_num = [i for i in range(1,len(df_norm_time)+1)]

fr1 = flow_rate(list_dn)
fr2 = flow_rate(list_dt)
#plot_gallery(time_num,list_dn,list_dt)
plot_gallery(time_num,fr1,fr2)
#max flow rate of Nars - 2.7 - 22
#max flow rate of Tun - 5.6 - 22
#max flow rate of Nars - 2.8 - 20
#max flow rate of Tun - 5.8 - 20
#max flow rate of Nars - 5.0 - 21
#max flow rate of Tun - 5.6 - 21