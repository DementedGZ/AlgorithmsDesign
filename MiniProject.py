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

    for x in range(MAXSIZE):
        name = 'OBJECT_' + str(x)
        phones.append(phone(0,0,0,name))

    algo = random.randint(0,2)

    def overlap(phones, x, y, i):
        for i in range(100):
            if getattr(phones[i], phone.x) == x and getattr(phones[i], phone.y) == y:
                return i - 1
            else:
                return i

    for i in range(5):
        setattr(phones[i], phone.x, random.randint(0,1))
        setattr(phones[i], phone.y, random.randint(0,1))
        print("x: " + getattr(phones[i], phones[i].x) + "\ny: " + getattr(phones[i], phones[i].y) + "\n\n")
        print(overlap(phones[0], phones[i].x, phones[i].y), i)
        
    if algo == 0:
        print("Uniform")
        # uniform algo goes here
    elif algo == 1:
        print("Cluster")
        # cluster algo goes here
    elif algo == 2:
        print("Distributed")
        #distributed algo goes here
    else:
        print("ERROR")

    
