L = []


my_labels = list(set(labels))

#Get the labels for each clustering
for j in my_labels:
    #For each row of my array
    for i in range(data.shape[0]):
        if labels[i] == my_labels[j]:
            newDistance = euclidean(centroids[j,:],data[i,:])
            L.append(newDistance)
        

sum(L)
