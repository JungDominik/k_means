def distance(p_xy, q_xy):                   #Helper method: Euclidean distance (only 2-dimensional)
    from math import sqrt

    x_p, y_p = p_xy[0], p_xy[1]
    x_q, y_q = q_xy[0], q_xy[1]
    
    d = sqrt((x_p - x_q )**2  + (y_p - y_q)**2)
    return d
    

def k_means (points_x, points_y, k):
    from random import random
    
    #Check formats, sanity check etc
    if len(points_x) != len(points_y): 
        raise Exception("X-coordinates and y-coordinates do not match.")
    else: length = len(points_x)

    #Initialize
    centroids = []
    point_centroid_allocation = []

    for i in range(k):
        centroids.append([random(),random()])
    
    print(centroids)


    #1. For each point, find nearest centroid, set into p-c-allocation list
    for i in range(length): #For each point
        index_nearest = 0
        # For each centroid: Check if 'nearest' needs to be updated
        for j in range (k):
            point = [points_x[i], points_y[i]]
            if distance(point, centroids[j]) < distance(point, centroids[index_nearest]):
                index_nearest = j
        
        print ("Point is " + str(points_x[i]) + " , " + str(points_y[i]) + "Variable 'indexNearest' is " + str(index_nearest))
        
        point_centroid_allocation.append(index_nearest)
    
    
    print ("Variable 'centroids' is " + str(centroids))
    print ("Variable 'point_centroid_allocation' is " + str(point_centroid_allocation))


    #2. Reposition the centroids based on their allocated points
    print ("Starting process to reposition centroids.")
    centroid_sum_x = [0] * k
    centroid_sum_y = [0] * k
    centroid_avg_x = [0] * k
    centroid_avg_y = [0] * k

    for i in range(length): #Go through all points and add their x and y values to the list of sums for the centroid repositioning
        assigned_centroid = point_centroid_allocation[i]
        centroid_sum_x[assigned_centroid] += points_x[i]
        centroid_sum_y[assigned_centroid] += points_y[i]

    for i in range (k):
        centroid_avg_x[i] = centroid_sum_x[i]/k
        centroid_avg_y[i] = centroid_sum_y[i]/k


    print (centroid_avg_x)
    print (centroid_avg_y)
    pass # TODO






testdata_x = [3,2,5,1,5,1,3,6,2,7,8,5,2,-8,5]
testdata_y = [1,9,5,4,8,9,6,8,8,6,5,8,9,-7,4]