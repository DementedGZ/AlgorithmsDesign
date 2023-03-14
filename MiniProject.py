import random
import math
import matplotlib.pyplot as plt

point1x = (random.randint(200, 800))
point1y = (random.randint(200, 800))
distance = 0
distance1 = 0
distance2 = 0
while distance < 400:
    point2x = (random.randint(200, 800))
    point2y = (random.randint(200, 800))
    distance = ((point2x - point1x)**2 + (point2y - point1y)**2)**0.5
while (distance1 < 400) | (distance2 < 400):
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
        self.isCovered = False
        self.isUsed = False
        
        if self.price < 3:
            self.x = random.randint(0, 1000)
            self.y = random.randint(0, 1000)
            while (((self.x - point1x)**2 + (self.y - point1y)**2)**0.5) > self.radius1:
                self.x = random.randint(0, 1000)
                self.y = random.randint(0, 1000)
        elif self.price >= 3 and self.price < 5:
            self.x = random.randint(0, 1000)
            self.y = random.randint(0, 1000)
            while (((self.x - point2x)**2 + (self.y - point2y)**2)**0.5) > self.radius2:
                self.x = random.randint(0, 1000)
                self.y = random.randint(0, 1000)
        else:
            self.x = random.randint(0, 1000)
            self.y = random.randint(0, 1000)
            while (((self.x - point3x)**2 + (self.y - point3y)**2)**0.5) > self.radius3:
                self.x = random.randint(0, 1000)
                self.y = random.randint(0, 1000)

def reset_participants(participants):
    for participant in participants:
        participant.isUsed = False
        participant.isCovered = False
        
def plot_coverage(cls, ax):
    budget = 50
    bestparticipant = None
    participants = cls
    while budget > 0:
        for p in participants:
            p1count = 0
            bestparticipantcount = 0
            for i in participants:
                if (not i.isCovered) and (not p.isUsed) and (p.price < budget):
                    dist = ((p.x - i.x) ** 2 + (p.y - i.y) ** 2) ** 0.5
                    if dist <= 100 and not i.isCovered:
                        p1count += 1
                    if bestparticipant is None:
                        bestparticipant = p
                    dist_to_i = ((bestparticipant.x - i.x) ** 2 + (bestparticipant.y - i.y) ** 2) ** 0.5
                    if dist_to_i <= 100 and not i.isCovered:
                        bestparticipantcount += 1
            if not bestparticipant.isCovered:
                bestparticipantcount += 1
            if not p.isCovered:
                p1count += 1
                if p1count / p.price >= bestparticipantcount / bestparticipant.price:
                    bestparticipant = p
        if budget - bestparticipant.price <= 0:
            break
        budget -= bestparticipant.price
        bestparticipant.isUsed = True
        bestparticipant.isCovered = True  
        circle = plt.Circle((bestparticipant.x, bestparticipant.y), 100 ,fill=False)
        ax.add_artist(circle)
        for e in participants:
            dist_to_best = ((e.x - bestparticipant.x) ** 2 + (e.y - bestparticipant.y) ** 2) ** 0.5
            if dist_to_best <= 100:
                e.isCovered = True


def create_circles(participants, ax):
    budget = 50
    for participant in participants:
        if (participant.isUsed == False) & (budget > participant.price):
            random_participant = random.choice(participants)
            circle = plt.Circle((random_participant.x, random_participant.y), 100, fill=False)
            ax.add_artist(circle)
            budget=budget-random_participant.price
            if budget < 0:
                break
            
# create 100 participants
participants = [Participants() for _ in range(100)]
participants2 = [Participants2() for _ in range(100)]

# extract x, y, and price values from participants
x = [p.x for p in participants]
y = [p.y for p in participants]
prices = [p.price for p in participants]
x1 = [a.x for a in participants2]
y1 = [a.y for a in participants2]
prices1 = [a.price for a in participants2]

# colors points on the first graph
colors = []
for price in prices:
    if 1 <= price < 3:
        colors.append('red')
    elif 3 <= price < 5:
        colors.append('blue')
    else:
        colors.append('green')
colors1 = []
for price in prices1:
    if 1 <= price < 3:
        colors1.append('red')
    elif 3 <= price < 5:
        colors1.append('blue')
    else:
        colors1.append('green')
fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
# fig, (ax3, ax4) = plt.subplots(nrows=1, ncols=2, figsize=(10, 10))
# fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(10, 10))



    
plot_coverage(participants,ax1)
plot_coverage(participants2,ax2)
# reset_participants(participants)
# reset_participants(participants2)
# create_circles(participants, ax3)
# create_circles(participants2, ax4)

ax1.scatter(x, y, c=colors)
ax2.scatter(x1, y1, c=colors1)
# ax3.scatter(x, y, c=colors)
# ax4.scatter(x1, y1, c=colors1)

ax1.set_title("Distributed")
ax2.set_title("Cluster")
for i, price in enumerate(prices):
    ax1.annotate(str(price), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
for i, price1 in enumerate(prices1):
    ax2.annotate(str(price1), (x1[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center')
# for i, price in enumerate(prices):
#     ax3.annotate(str(price), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
# for i, price1 in enumerate(prices1):
#     ax4.annotate(str(price1), (x1[i], y1[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()
