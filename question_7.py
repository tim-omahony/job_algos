# Given a list of points on the 2-D plane and an integer K. The task is to find K closest points to the origin and print them.
# Note: The distance between two points on a plane is the Euclidean distance.
# E.G. Input : point = [[3, 3], [5, -1], [-2, 4]], K = 2
# Output : [[3, 3], [-2, 4]] √{(x2-x1)2 + (y2-y1)2}
from math import sqrt

def k_closest(points, K):
 
    points.sort(key = lambda blah: blah[0]**2 + blah[1]**2)
 
    return points[:K]
 
# Driver program
points = [[3, 3], [5, -1], [-2, 4]]
 
K = 2

print(k_closest(points, K))


import heapq as hq
# Function to find the K closest points
def kClosestPoints(x, y, n, k):
    # Create a priority queue
    pq=[]
 
    # Pushing all the points
    # in the queue
    for i in range(n):
        hq.heappush(pq, (x[i]**2+y[i]**2,x[i],y[i]))
     
    # Print the first K elements
    # of the queue
    for i in range(k) :
 
        # Store the top of the queue
        # in a temporary pair
        p = hq.heappop(pq)
 
        # Print the first (x)
        # and second (y) of pair
        print("{} {}".format(p[1],p[2]))  
 
 
# Driver code
if __name__ == '__main__':
    # x coordinate of points
    x = [1, -2]
 
    # y coordinate of points
    y = [3, 2]
    K = 1
 
    n=len(x)
 
    kClosestPoints(x, y, n, K)
    