import random
import math
import matplotlib.pyplot as plt

class Participants:
    # default contructor
    def __init__(self):
        self.price = round(random.uniform(1, 7), 2)
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.isCovered = False
        self.isUsed = False

       

# create 100 participants
participants = [Participants() for _ in range(100)]

# extract x, y, and price values from participants
x = [p.x for p in participants]
y = [p.y for p in participants]
prices = [p.price for p in participants]
fig, ax = plt.subplots()
ax.scatter(x, y)

# while loop
budget=100


bestparticipant=None
while (budget>0):
    for p in participants:
        p1count=0
        bestparticipantcount=0
        for i in participants:
            if(i.isCovered==False) & (p.isUsed==False):
                if((((p.x-i.x)**2+(p.y-i.y)**2)**0.5)<=30) & (i.isCovered==False):
                    p1count=p1count+1
                if(bestparticipant == None):
                    bestparticipant=p
                if((((bestparticipant.x-i.x)**2+(bestparticipant.y-i.y)**2)**0.5)<=30) & (i.isCovered==False):
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
    circle = plt.Circle((bestparticipant.x, bestparticipant.y), 30 ,fill = False)
    ax.add_artist(circle)
    for e in participants:
        if((((e.x-bestparticipant.x)**2+(e.y-bestparticipant.y)**2)**0.5)<=30):
            e.isCovered=True
    #print(budget)
    print(bestparticipant.price)
    
        
# plot participants on a scatter plot and show prices

for i, price in enumerate(prices):
    ax.annotate(str(price), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()