
def Time_Selection(dataframe,window_h,window_m,val_h,val_m):
    x = randint(0,len(dataframe)-1)
    init_time = dataframe['time'].loc[x]
    h = window_h*60*60
    m = window_m*60
    hv = val_h*60*60
    mv = val_m*60
    final_time = init_time+h+m
    val_time = final_time+hv+mv
    init_time = pd.to_datetime(init_time,utc = True,unit = 's') 
    final_time = pd.to_datetime(final_time,utc = True,unit = 's')
    val_time = pd.to_datetime(val_time,utc = True,unit = 's') 
    lst1 = []
    lst2 = []
    lock = 0
    for i in range(len(dataframe)):        
        curr_time = dataframe['time'].loc[i]
        curr_time = pd.to_datetime(curr_time,utc = True,unit = 's')    
        if init_time < curr_time < val_time:
            if init_time < curr_time < final_time:
                lst1.append(i)
            elif final_time< curr_time < val_time:
                 lst2.append(i)
            lock = 1
        else: 
            if lock == 1:    
                break
            else: pass 
    return lst1,lst2

def filter_size(dataframe,window_h,window_m,val_h,val_m):
    lst1,lst2 = Time_Selection(dataframe,window_h,window_m,val_h,val_m)
    empty_count = 0
    while (len(lst1) < 3) & (len(lst2) < 3): 
            print('Empty, Searching again:  ('+str(empty_count)+'/25)')
            empty_count = empty_count +1
            lst1,lst2 = Time_Selection(dataframe,window_h,window_m,val_h,val_m)   
            if empty_count>25: break 
    return lst1,lst2


def Data_Preprocessing(time_h,time_m,val_h,val_m,pat):
    df,Sensor_ID = Data_Loader(patient_ID[pat])
    buss1,buss2 = filter_size(df,time_h,time_m,val_h,val_m)
    low_t = min(buss1)
    max_t = max(buss1)
    low_t1 = min(buss2)
    max_t1 = max(buss2)
    train_data =  df[low_t:max_t]
    valid_data = df[low_t1:max_t1]
    n = len(valid_data)
    valid_data,anom_lst = anomaly_insertion(n,Sensor_ID,valid_data,5.0)
    train_data.drop('time', axis = 1, inplace = True)
    valid_data.drop('time', axis = 1, inplace = True)

    X_trainD = train_data.loc[:, train_data.columns != 'labels']
    X_valD = valid_data.loc[:, valid_data.columns != 'labels']
    Y_trainD = train_data.loc[:,'labels']
    Y_valD = valid_data.loc[:,'labels']
    X_train = torch.tensor(X_trainD.values).float()
    X_val = torch.tensor(X_valD.values).float()
    Y_train = torch.tensor(Y_trainD.values).float()
    Y_val = torch.tensor(Y_valD.values).float()

    return X_train,Y_train,X_val,Y_val,train_data,valid_data,anom_lst,Sensor_ID,n

