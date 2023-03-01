import random
import math
import matplotlib.pyplot as plt

point1x = (random.randint(200, 800))
point1y = (random.randint(200, 800))
distance = 0
distance1 = 0
distance2 = 0
while distance < 100:
    point2x = (random.randint(200, 800))
    point2y = (random.randint(200, 800))
    distance = ((point2x - point1x)**2 + (point2y - point1y)**2)**0.5
while (distance1 < 100) | (distance2 < 100):
    point3x = (random.randint(200, 800))
    point3y = (random.randint(200, 800))
    distance1 = ((point3x - point1x)**2 + (point3y - point1y)**2)**0.5
    distance2 = ((point3x - point2x)**2 + (point3y - point2y)**2)**0.5

class Participants:
    def __init__(self):
        self.price = round(random.uniform(1, 7), 2)
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.isCovered = False
        self.isUsed = False
class Participants2:
    def __init__(self):
        self.radius1 = random.randint(100, 300)
        self.radius2 = random.randint(100, 300)
        self.radius3 = random.randint(100, 300)
        self.price = round(random.uniform(1, 7), 2)
        self.isCovered1 = False
        self.isUsed1 = False
        
        # Place point in appropriate radius based on price
        if self.price < 3:
            # Place point in radius1 of point1
            self.x1 = random.randint(0, 1000)
            self.y1 = random.randint(0, 1000)
            while (((self.x1 - point1x)**2 + (self.y1 - point1y)**2)**0.5) > self.radius1:
                self.x1 = random.randint(0, 1000)
                self.y1 = random.randint(0, 1000)
        elif self.price >= 3 and self.price < 5:
            # Place point in radius2 of point2
            self.x1 = random.randint(0, 1000)
            self.y1 = random.randint(0, 1000)
            while (((self.x1 - point2x)**2 + (self.y1 - point2y)**2)**0.5) > self.radius2:
                self.x1 = random.randint(0, 1000)
                self.y1 = random.randint(0, 1000)
        else:
            # Place point in radius3 of point3
            self.x1 = random.randint(0, 1000)
            self.y1 = random.randint(0, 1000)
            while (((self.x1 - point3x)**2 + (self.y1 - point3y)**2)**0.5) > self.radius3:
                self.x1 = random.randint(0, 1000)
                self.y1 = random.randint(0, 1000)
        
# create 100 participants
participants = [Participants() for _ in range(100)]
participants2 = [Participants2() for _ in range(100)]

# extract x, y, and price values from participants
x = [p.x for p in participants]
y = [p.y for p in participants]
prices = [p.price for p in participants]
x1 = [a.x1 for a in participants2]
y1 = [a.y1 for a in participants2]
prices1 = [a.price for a in participants2]

# colors points on the first graph
colors = []
for price in prices:
    if 1 <= price <= 3:
        colors.append('red')
    elif 3 < price <= 5:
        colors.append('blue')
    else:
        colors.append('green')
colors1 = []
for price in prices1:
    if 1 <= price <= 3:
        colors1.append('red')
    elif 3 < price <= 5:
        colors1.append('blue')
    else:
        colors1.append('green')
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))


# circles the best point with the lowest cost per participant covered for the completely random graph
budget=50
#Covered=0
bestparticipant=None
while (budget>0):
    for p in participants2:
        p1count=0
        bestparticipantcount=0
        for i in participants2:
            if(i.isCovered1==False) & (p.isUsed1==False) & (p.price<budget):
                if((((p.x1-i.x1)**2+(p.y1-i.y1)**2)**0.5)<=50) & (i.isCovered1==False):
                    p1count=p1count+1
                if(bestparticipant == None):
                    bestparticipant=p
                if((((bestparticipant.x1-i.x1)**2+(bestparticipant.y1-i.y1)**2)**0.5)<=50) & (i.isCovered1==False):
                    bestparticipantcount=bestparticipantcount+1
        if(bestparticipant.isCovered1==False):
            bestparticipantcount=bestparticipantcount+1
        if(p.isCovered1==False):
            p1count=p1count+1
            if ((p1count/p.price) >= (bestparticipantcount/bestparticipant.price)):
                bestparticipant=p                          
    if(budget-bestparticipant.price<=0):
        break
    budget=budget-bestparticipant.price
    bestparticipant.isUsed1=True
    bestparticipant.isCovered1=True
    print(budget)
    circle = plt.Circle((bestparticipant.x1, bestparticipant.y1), 50 ,fill = False)
    ax2.add_artist(circle)
    for e in participants:
        if((((e.x-bestparticipant.x1)**2+(e.y-bestparticipant.y1)**2)**0.5)<=50):
            e.isCovered=True
            
budget=50
#Covered=0
bestparticipant=None
while (budget>0):
    for p in participants:
        p1count=0
        bestparticipantcount=0
        for i in participants:
            if(i.isCovered==False) & (p.isUsed==False) & (p.price<budget):
                if((((p.x-i.x)**2+(p.y-i.y)**2)**0.5)<=50) & (i.isCovered==False):
                    p1count=p1count+1
                if(bestparticipant == None):
                    bestparticipant=p
                if((((bestparticipant.x-i.x)**2+(bestparticipant.y-i.y)**2)**0.5)<=50) & (i.isCovered==False):
                    bestparticipantcount=bestparticipantcount+1
        if(bestparticipant.isCovered==False):
            bestparticipantcount=bestparticipantcount+1
        if(p.isCovered==False):
            p1count=p1count+1
            if ((p1count/p.price) >= (bestparticipantcount/bestparticipant.price)):
                bestparticipant=p                          
    if(budget-bestparticipant.price<=0):
        break
    budget=budget-bestparticipant.price
    bestparticipant.isUsed=True
    bestparticipant.isCovered=True  
    circle = plt.Circle((bestparticipant.x, bestparticipant.y), 50 ,fill = False)
    ax1.add_artist(circle)
    for e in participants:
        if((((e.x-bestparticipant.x)**2+(e.y-bestparticipant.y)**2)**0.5)<=50):
            e.isCovered=True
    
    
        
# plot participants on a scatter plot and show prices
ax1.scatter(x, y, c=colors)
ax2.scatter(x1, y1, c=colors1)
for i, price in enumerate(prices):
    ax1.annotate(str(price), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, price1 in enumerate(prices1):
    ax2.annotate(str(price1), (x1[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()
