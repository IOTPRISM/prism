model = sklearn.neighbors.NearestNeighbors(n_neighbors = n)
detections = []
distancelst = []
def Train_AD(alpha,sensor_num):
    for i in range(len(X_train)):
        model.fit(X_train[i])
        def_distances, def_indexes = model.kneighbors(X_train[i].reshape(1, -1))
        distancelst.append(float(def_distances)
    
    threshold = mean(distancelst)
    for i in range(len(X_val)):
        test_d, test_i = model.kneighbors(X_val[i].reshape(1, -1))
        if float(float(def_distances[0])>threshold:
            detections.append(X_val[i])

    return detections,Sensor_ID,n


def Main(alpha,sensor_num):
    detections,Sensor_ID,n = Train_AD(alpha,sensor_num)
    global size_mat
    size_mat = int(len(detections[0]))
    print(size_mat)
    counter = 0
    anomalies = detections
    if len(anomalies) == 0:
        counter = 0
    else:
        for i in range(len(anomalies)):
            x = anomalies[i].numpy()
            if x[size_mat-1]==delta_t: # the anomalies are created with a time difference that can be used to detect them.
                counter = counter+1
    correct = counter
    fake_positive = len(anomalies) - correct
    correct = correct/n
    accuracy = ((correct*n)+(n-fake_positive))/(n*2)

    print('Correctly Identified Anomalies (fraction) : ' + str(correct))
    print('Fake Positives: '+ str(fake_positive))
    print('Accuracy: '+str(accuracy))
    # print('Average Inference time: '+ str(inf_t))
    return Sensor_ID,accuracy
total_lst = []
for a in range(x):
    global sensor_num
    sensor_num=a     
    for b in range(10):
        try:
            print('repetition: '+ str(b))
            Sensor_ID,accuracy = Main(1,a)
            if accuracy==0:
                pass
            else:
                total_lst.append([Sensor_ID,accuracy])
        except:pass