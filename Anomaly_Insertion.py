from random import gauss


anomaly_delta_t = x # enter
def activity_pir_anomaly(time,n,id): #spam
    global pir_time
    global pir_key
    global switch
    value = 5.
    if pir_key == 0.0:
        time_p = time
        return [time_p,id,0,1.0] 
    if pir_key == 1.0:
        time_p = time + 1.0
        return [time_p] + [value] + [0] + [anomaly_delta_t]

def ambient_temp_anomaly(time,n,id): # variance
    global pir_time
    global pir_key
    variancen =  gauss(25,25)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +1.0
        return [pir_time] + [id]+ [variancen]+ [0] + [anomaly_delta_t]

def appliance_use_anomaly(time,n,id): # spam
    global pir_time
    global pir_key
    intiger = 3.0
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + 1.0
        return [pir_time]  + [intiger]+ [0] + [anomaly_delta_t]

def blood_pressure_anomaly(time,n,id): # spike
    global pir_time
    global pir_key
    varianc1 = float(randint(1000,2000))
    varianc2 = float(randint(600,900))
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +1.0
        return [pir_time] + [varianc1]+ [varianc2]+ [0] + [anomaly_delta_t]

def body_mass_index_anomaly(time,n,id): # variance
    global pir_time
    global pir_key
    variancen = gauss(0,10)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +1.0
        return [pir_time] + [variancen]+ [0] + [anomaly_delta_t]

def body_temperature_anomaly(time,n,id): # #Variance
    global pir_time
    global pir_key
    variancen = gauss(0,100)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + 1.0
        return [pir_time] + [variancen]+ [0] + [anomaly_delta_t]

def body_weight_anomaly(time,n,id): #Spike
    global pir_time
    global pir_key
    spike = randint(500.0,600.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + 1.0
        return [pir_time] + [spike]+ [0] + [anomaly_delta_t]

def door_sensor_anomaly(time,n,value):#create
    global pir_time
    global pir_key
    if pir_key == 0.0:
        time_p = time
        return [time_p,id,value,0,1.0] 
    if pir_key == 1.0:
        time_p = time + 1.0
        return [time_p] + [id] + [value] + [0] + [anomaly_delta_t]

def heart_rate_anomaly(time,n,id): #spike
    global pir_time
    global pir_key
    spike = randint(300.0,400.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + 1.0
        return [pir_time] + [spike]+ [0] + [anomaly_delta_t]

def light_anomaly(time,n,id): #variance
    global pir_time
    global pir_key
    variancen =gauss(0.0,1000.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +1.0
        return [pir_time] + [id]+ [variancen]+ [0] + [anomaly_delta_t]

def oxygen_saturation_anomaly(time,n,id): # variance
    global pir_time
    global pir_key
    variancen = gauss(0.0,200.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +1.0
        return [pir_time] + [variancen] + [0] + [anomaly_delta_t]

def skin_temperature_anomaly(time,n,id): #spike
    global pir_time
    global pir_key
    variancen = randint(200.0,1000.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time +20.0
        return [pir_time] + [variancen]+ [0] + [anomaly_delta_t]

def sleep_event_anomaly(time,n,value):#create
    global pir_time
    global pir_key
    if pir_key == 0.0:
        time_p = time
        return [time_p,value,0,1.0] 
    if pir_key == 1.0:
        time_p = time + 10.0
        return [time_p] + [value] + [0] + [anomaly_delta_t]

def sleep_mat_heart_rate_anomaly(time,n,id): #spike
    global pir_time
    global pir_key
    variancen = randint(100.0,1000.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + delta_t 
        return [pir_time] + [variancen]+ [0] + [anomaly_delta_t]

def sleep_mat_respiratory_rate_anomaly(time,n,id): #spike
    global pir_time
    global pir_key
    variancen = randint(25.0,100.0)
    if pir_key == 0:
        pir_time = time     
        pir_key = 1
    if pir_key == 1:
        pir_time = pir_time + delta_t 
        return [pir_time] + [variancen]+ [0] + [anomaly_delta_t]

def sleep_mat_snoring_rate_anomaly(time,n,value):#create
    global pir_time
    global pir_key
    if pir_key == 0.0:
        time_p = time
        return [time_p,value,0,1.0] 
    if pir_key == 1.0:
        time_p = time + 10.0
        return [time_p] + [value] + [0] + [anomaly_delta_t]

def sleep_mat_state_anomaly(time,n,value):#create
    global pir_time
    global pir_key
    if pir_key == 0.0:
        time_p = time
        return [time_p,value,0,1.0] 
    if pir_key == 1.0:
        time_p = time + 1.0
        return [time_p] + [value] + [0] + [anomaly_delta_t]

def anomaly_insertion(n,type,dataframe,id):
    df = dataframe
    anomaly_lst = []
    col_name = df.columns
    col_len = len(df.columns)
    start_t = min(dataframe['time'])
    end_t = max(dataframe['time'])
    value = 0
    for i in range(n):
        random_timestamp = random.randint(start_t,end_t)
        value = i%2 #for the create anomaly
        if type == 'activity_pir':
            zp_anomaly_lst= activity_pir_anomaly(random_timestamp,col_len,id)   
        if type == 'ambient_temperature':
            zp_anomaly_lst= ambient_temp_anomaly(random_timestamp,col_len,id)  
        if type == 'appliance_use':
            zp_anomaly_lst= appliance_use_anomaly(random_timestamp,col_len,id)   
        if type == 'blood_pressure':
            zp_anomaly_lst= blood_pressure_anomaly(random_timestamp,col_len,id) 
        if type == 'body_mass_index':
            zp_anomaly_lst= body_mass_index_anomaly(random_timestamp,col_len,id) 
        if type == 'body_temperature':
            zp_anomaly_lst= body_temperature_anomaly(random_timestamp,col_len,id)      
        if type == 'body_weight':
            zp_anomaly_lst= body_weight_anomaly(random_timestamp,col_len,id) 
        if type == 'door_sensor':
            zp_anomaly_lst= door_sensor_anomaly(random_timestamp,col_len,id) 
        if type == 'heart_rate':
            zp_anomaly_lst= heart_rate_anomaly(random_timestamp,col_len,id) 
        if type == 'light':
            zp_anomaly_lst= light_anomaly(random_timestamp,col_len,id)          
        if type == 'oxygen_saturation':
            zp_anomaly_lst= oxygen_saturation_anomaly(random_timestamp,col_len,id)          
        if type == 'skin_temperature':
            zp_anomaly_lst= skin_temperature_anomaly(random_timestamp,col_len,id) 
        if type == 'sleep_event':
            zp_anomaly_lst= sleep_event_anomaly(random_timestamp,col_len,value) 
        if type == 'sleep_mat_heart_rate':
            zp_anomaly_lst= sleep_mat_heart_rate_anomaly(random_timestamp,col_len,id)    
        if type == 'sleep_mat_respiratory_rate':
            zp_anomaly_lst= sleep_mat_respiratory_rate_anomaly(random_timestamp,col_len,id)  
        if type == 'sleep_mat_snoring':
            zp_anomaly_lst= sleep_mat_snoring_rate_anomaly(random_timestamp,col_len,value) 
        if type == 'sleep_mat_state':
            zp_anomaly_lst= sleep_mat_state_anomaly(random_timestamp,col_len,value)                  
        anomaly_lst.append(zp_anomaly_lst)
    anomaly_df = pd.DataFrame(anomaly_lst,columns=col_name)
    concat_df = pd.concat([dataframe,anomaly_df],ignore_index=True)
    concat_df = concat_df.reset_index(drop=True)
    return  concat_df,anomaly_lst
  