import random
class MainBoard:
    MAXSIZE = 100
    phones = [MAXSIZE]
    algo = random.randint(0,2)
    if algo == 0:
        print("Uniform")
        # uniform algo goes here
    elif algo == 1:
        print("Cluster")
        # cluster algo goes here
    else:
        print("Distributed")
        #distributed algo goes here
        

class phone:
    def __init__(self, radius, bitPrice, x, y):
         self.radius = 0
         self.bitPrice = 0
         self.x = 0
         self.y = 0
         

    