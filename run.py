import numpy as np
import statistics

from server import server
from model import *
#Data Collection
while True:
    server_launch= input("Do you want to launch the server? (Y/N):")
    if server_launch == 'Y':
        server.launch()
        break
    # Results = {}
    elif server_launch == 'N':
        homophily_happiness =[]
        for homophily in [2,4,6]:
            happy_agents=[]
            for _ in range(5):
                model = Schelling(100, 100, 0.8, 0.2, homophily)
                # for i in range(100):
                model.step()
                print(model.happy)
                happy_agents.append(model.happy)
            homophily_happiness.append(sum(happy_agents)/len(happy_agents))
        print(homophily_happiness)
        density_happiness =[]
        for density in [0.6,0.7,0.8]:
            happy_agents=[]
            for _ in range(10):
                model = Schelling(100, 100, density, 0.2, 3)
                # for _ in range(100):
                model.step()
                print(model.happy)
                happy_agents.append(model.happy)
            density_happiness.append(sum(happy_agents)/len(happy_agents))
        print(density_happiness)
        break
    else:
        continue
