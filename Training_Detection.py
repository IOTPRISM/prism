class Net(nn.Module):
    global size_mat
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(size_mat, 512)
        self.fc2 = nn.Linear(512, 512)
        self.fc3 = nn.Linear(512, 512)        
        self.fc4 = nn.Linear(512, 2)

    def forward(self, x):
        x = torch.flatten(x, 1) # flatten all dimensions except batch
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = F.relu(self.fc3(x))
        x = self.fc4(x)
        return x

def Train_AD(time_h,time_m,val_h,val_m,pat):
    X_train,Y_train,X_val,Y_val,train_data,valid_data,anom_lst,Sensor_ID,n = Data_Preprocessing(time_h,time_m,val_h,val_m,pat)
    global size_mat
    size_mat = len(X_train[0])
    model = Net()
    optimizer = torch.optim.SGD(model.parameters(), lr = 3e-5)
    criterion = nn.L1Loss()
    batch_size = 1
    n_epochs = 10
    permutation_train = torch.randperm(X_train.size()[0])
    permutation_val = torch.randperm(X_val.size()[0])
    anomalies = []
    valid_loss = []
    train_loss = []
    inference_time = []
    for epoch in range(n_epochs):
        train_loss = []
        for i in range(0,len(train_data), batch_size):
            optimizer.zero_grad()
            indices = permutation_train[i:i+batch_size]
            batch_x, batch_y = X_train[indices], Y_train[indices]
            outputs = model.forward(batch_x)
            loss = criterion(outputs,batch_y)
            train_loss.append(loss.item())
            loss.backward()
            optimizer.step()
        threshold = mean(train_loss)

    for a in range(0,X_val.size()[0], batch_size):
        start_time = time.time() 
        indicesV = permutation_val[a:a+batch_size]
        batch_x_val, batch_y_val = X_val[indicesV], Y_val[indicesV]
        output = model.forward(batch_x_val)
        pred = torch.max(output,1)[1]
        loss = criterion(output,batch_y_val)
        valid_loss.append(loss.item())
        if loss.item() >= threshold:
            anomalies.append(batch_x_val)
        time_elapsed = time.time() - start_time
        inference_time.append(1000*time_elapsed)   
    return anomalies,train_loss,valid_loss,Sensor_ID,n,size_mat,mean(inference_time)

