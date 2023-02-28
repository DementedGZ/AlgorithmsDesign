import random
import math
import matplotlib.pyplot as plt

class Participants:
    def __init__(self):
        self.price = round(random.uniform(1, 7), 2)
        self.x = random.randint(0, 1000)
        self.y = random.randint(0, 1000)
        self.isCovered = False
        self.isUsed = False
        
        
def makeCovered(participants):
    participants.isCovered = True
        
def makeUsed(participants):
    participants.isUsed = True
        
def createCircle(participants):
    circle = plt.Circle((participants.x, participants.y), 5 ,fill = False)
    ax.add_artist(circle)

# create 100 participants
participants = [Participants() for _ in range(100)]

# extract x, y, and price values from participants
x = [p.x for p in participants]
y = [p.y for p in participants]
prices = [p.price for p in participants]

# plot participants on a scatter plot and show prices
fig, ax = plt.subplots()
ax.scatter(x, y)
p=participants[1]
createCircle(p)
for i, price in enumerate(prices):
    ax.annotate(str(price), (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
plt.show()
