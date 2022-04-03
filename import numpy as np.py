from random import random
import numpy as np

def min_max_dist(*vectors):

    
    #dist_array = []
    
    #np.dist_array.remove(0.0)
    distance_array = []
    
    #distance_array = []
    
    for i in vectors:
 
        for j in vectors:
            if i is j:
                continue
            else:
                current_dist = np.linalg.norm(i - j)
                #dist_array.append(current_dist)
                distance_array.append(current_dist)
                print(distance_array)
            
    distance_array = np.array(distance_array)
    
        
    
    return (distance_array.min(), distance_array.max())
    
    
    
    
    
vec1 = np.array([1,2,3])
vec2 = np.array([4,5,6])
vec3 = np.array([7, 8, 9])
 
print(min_max_dist(vec1, vec2, vec3))
