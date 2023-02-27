import random
class phone:
    def __init__(self,x,y,bidprice,name):
         self.name = name
         self.bidPrice = bidprice
         self.x = x
         self.y = y

class MainBoard:
    MAXSIZE = 100
    RADIUS = 5
    phones = [MAXSIZE]
    for x in phones:
        name = 'OBJECT_' + x
        phones[x] = phone(0,0,0,name)
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
         

    