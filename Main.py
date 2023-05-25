def Main(time_h,time_m,val_h,val_m,pat):
    anomalies,train_loss,valid_loss,Sensor_ID,n,size_mat,inf_t = Train_AD(time_h,time_m,val_h,val_m,pat)
    counter = 0
    if len(anomalies) == 0:
        counter = 0
    else:
        for i in range(len(anomalies)):
            x = anomalies[i].numpy()
            if x[0][size_mat-1]==anomaly_delta_t: # the anomalies are created with a time difference that can be used to detect them.
                counter = counter+1
    correct = counter
    fake_positive = len(anomalies) - correct
    correct = correct/n
    accuracy = ((correct*n)+(n-fake_positive))/(n*2)
    print('')
    print(str(Sensor_ID)+', For training window: ' +str(time_h)+ ':'+str(time_m)+', For validation window: '+str(val_h)+':'+str(val_m))
    print('Correctly Identified Anomalies (fraction) : ' + str(correct))
    print('Fake Positives: '+ str(fake_positive))
    print('Accuracy: '+str(accuracy))
    print('Average Inference time: '+ str(inf_t))

    return Sensor_ID,accuracy,inf_t


train_time = [[24,0],[12,0],[3,0],[0,45],[0,30],[0,15]]# time window format: [hours,minutes]
valid_time= [[24,0],[12,0],[3,0],[0,45],[0,30],[0,15]]
sensors_lst = []
periods_lst = []
correct_lst = []
false_lst = []
total_results = []
repetitions = 100
#this loop is for all patients for all combinations of train and validation time. 
for patient in range(len(patient_ID)):
    try:
        for sensor in range(22):
            global sensor_num
            sensor_num = sensor
            try:
                for c in range(len(valid_time)):
                    for i in range(len(train_time)):
                        count_r = 0
                        for b in range(repetitions):
                            print('repetition: '+ str(b))
                            try:
                                Sensor_ID,accuracy,inf_t = Main(train_time[i][0],train_time[i][1],valid_time[c][0],valid_time[c][1],patient)
                                count_r = count_r +1
                                total_results.append([Sensor_ID,train_time[i][0],train_time[i][1],valid_time[c][0],valid_time[c][1],accuracy,inf_t])
                            except: pass
            except: pass
    except: pass

print(total_results)
