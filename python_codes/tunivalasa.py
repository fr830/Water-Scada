import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


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

def normalize(time_nars,time_tun,dat_nars,dat_tun):
    """to normalize the time to a standard set"""
    norm_dat_nars = pd.Series() #data of nars according to new scale
    norm_dat_tun = pd.Series() #data of tun according to new scale
    norm_time = pd.Series() #standard time scale
    j = 0
    n = 0
    t = 0
    hour_count = 0
    
    for i in range(0,1440):
        if j==59:
            j=0
            hour_count+=1
        #print(i)
        if i<1372:
            if time_nars.iloc[i].minute == j and time_tun.iloc[i].minute == j :    
                time = pd.Series(time_nars.iloc[i])
                norm_time.append(time)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                n+=1
                t+=1
            if time_nars.iloc[i].minute == j and time_tun.iloc[i].minute !=j :
                time = pd.Series(time_nars.iloc[i])
                norm_time.append(time)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                n+=1
        
            if time_nars.iloc[i].minute != j and time_tun.iloc[i].minute == j :
                time = pd.Series(time_nars.iloc[i])
                norm_time.append(time)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                t+=1
            if time_nars.iloc[i].minute != j and time_tun.iloc[i].minute != j :
                st1 = str(hour_count) + ":" + str(j) + ":" + "00"
                dtime = datetime.strptime(st1,'%H:%M:%S')
                norm_time.append(dtime)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
        elif i>=1372 and i<=1423:
            if time_nars.iloc[i].minute == j:
                time = pd.Series(time_nars.iloc[i])
                norm_time.append(time)
                norm_dat_nars.append(dat_nars.iloc[n])
                norm_dat_tun.append(dat_tun.iloc[t])
                n+=1
            elif time_nars.iloc[i].minute != j:
                
         j+=1               
            
        
            
            
            
    
             
             
            
    return norm_time, norm_dat_nars, norm_dat_tun

def saveNewData(ndata, path):
    ndata.to_csv(path)
    
def plot_gallery(nars_time,nars_amr):
    plt.xlabel("Time ->")
    plt.title("AMR vs Time")
    plt.ylabel("Total AMR") 
    plt.grid(True)
    #plt.plot(nars_time[:2770],nars_amr[:2770],"b", label = "Narsaparum")
    #plt.plot(tun_amr,"r", label = "Tunivalasa")
    plt.plot(nars_time,nars_amr,"b",label= "Narsapuram")
    plt.legend(loc = 'upper left')
    plt.show()
    

dat_nars = pd.read_excel(r"G:\PS1\NSP_OHSR.xlsx")
dat_tun = pd.read_excel(r"G:\PS1\Tunivalasa.xlsx")
#dropping columns not required
to_drop = ['PLC','Site','Capacity','HM']
dat_nars.drop(to_drop,inplace=True,axis=1)
dat_tun.drop(to_drop,inplace=True,axis=1)

nars_time,nars_amr = extract_data(dat_nars)
tun_time,tun_amr = extract_data(dat_tun)

"""call for cleaning the data;commented as clean data already received
No need to save every time program is ran"""

new_data_nars = remove_duplicates(dat_nars,nars_time)
new_data_tun = remove_duplicates(dat_tun,tun_time)
ind1 = [i for i in range(0,1423)]
ind2 = [i for i in range(0, 1372)]
#saveNewData(new_data_nars,r"G:\PS1\clean_data_nars.csv")
#saveNewData(new_data_tun,r"G:\PS1\clean_data_tun.csv")
new_nars_time, new_nars_amr = extract_data(new_data_nars)
new_tun_time, new_tun_amr = extract_data(new_data_tun)
#new_nars_time = new_nars_time.reindex(ind1)
#new_nars_time = new_nars_time.rename(lambda x: x)
#new_tun_time = new_tun_time.reindex(ind2)

normalized_time, normalized_dn, normalized_dt = normalize(new_nars_time, new_tun_time, new_data_nars,new_data_tun)

#plt.savefig(r"G:\PS1\flowsT.pdf")
