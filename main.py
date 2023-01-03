import threading
import time

swetha_Height = 1 #her height from the ground is 1m
binu_Height = 7 #her height from the ground is 7m
swetha_Velocity = 1 #speed in which she goes is 1m/s
binu_Velocity = 1.5 #speed in which she goes is 1.5m/s

increase = threading.Semaphore() #default : Semaphore(1)
#number of Threads allowed to access simultaneously
decrease = threading.Semaphore(0)

#going up function
def goingUp():
    global swetha_Height
    global binu_Height
    global swetha_Velocity
    global binu_Velocity
    for i in range(1):
        while swetha_Height < 7:
            increase.acquire()
            # to decrease the count of the semaphore by 1 in case the count is greater than zero.
            swetha_Height += swetha_Velocity
            print ("swetha is going up, her height currently from the ground is: ", swetha_Height)
            time.sleep(1)
            decrease.release()
            #to increase the count of the semaphore by 1 in case the count is zero.
        while binu_Height < 7:
            increase.acquire()
            binu_Height += binu_Velocity
            print ("binu is going up, her height currently from the ground is: ", binu_Height)
            time.sleep(1)
            decrease.release()
            
#going down function
def goingDown():
    global swetha_Height
    global binu_Height
    global swetha_Velocity
    global binu_Velocity
    for i in range(1):
        while binu_Height > 1:
            decrease.acquire()
            #to increase the count of the semaphore by 1 in case the count is zero.
            binu_Height -= swetha_Velocity
            print ("binu is going down, her height currently from the ground is: ", binu_Height, "\n")
            time.sleep(1)
            increase.release()
        while swetha_Height > 1:
            decrease.acquire()
            swetha_Height -= binu_Velocity
            print ("swetha is going down, her height  currently from the ground is: ", swetha_Height, "\n")
            time.sleep(1)
            increase.release()
            
if __name__ == '__main__':
    t1 = threading.Thread(target=goingUp)
    #calling the function goingup() using threads
    t1.start()
    #Thread activity t1 is started by calling the start() method
    t2 = threading.Thread(target=goingDown)
    #calling the function goingup() using threads
    t2.start()
    #Thread activity t2 is started by calling the start() method
    t1.join()
    t2.join()
