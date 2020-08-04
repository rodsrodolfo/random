import matplotlib.pyplot as plt
import math
from numpy import pi as pi
from numpy import random as rn

while 1:

    n = int(input('GP: '))
    
    xd = []
    yd = []
    
    xr = []
    yr = []
    
    #Define Points
    
    for set in range(9):
            
            #Phi Defined
    
            xd.append([0])
            yd.append([0])
            
            for i in range(n):
                phi0 = math.atan2(yd[-1][i]-yd[-1][i-1], xd[-1][i]-xd[-1][i-1])
                phi = rn.choice([0.61522856, -0.61522856]) + phi0
                xd[-1].append(xd[-1][i]+1.54*math.cos(phi))
                yd[-1].append(yd[-1][i]+1.54*math.sin(phi))
                
                
            #Random Phi            
            
            xr.append([0])
            yr.append([0])
            
            for i in range(n):
                phi0 = math.atan2(yr[-1][i]-yr[-1][i-1], xr[-1][i]-xr[-1][i-1])
                phi = rn.uniform(0,2*pi)
                xr[-1].append(xr[-1][i]+1.54*math.cos(phi))
                yr[-1].append(yr[-1][i]+1.54*math.sin(phi))


    #Define Borders    

    xm = 0
    ym = 0
    
    for set in range(9):
        for value in range(n+1):
            if max(xd[set][value],xr[set][value]) > xm:
                xm = int(max(xd[set][value],xr[set][value]))+1
                
    for set in range(9):
        for value in range(n+1):
            if max(yd[set][value],yr[set][value]) > ym:
                ym = int(max(yd[set][value],yr[set][value]))+1
                
    m = max(xm, ym)
    
    #Plots
    
    fig, axs = plt.subplots(3, 3)
    plot = 0
    
    for row in range(3):
        for col in range(3):
            
            axs[row, col].plot(xd[plot],yd[plot],'k-')
            axs[row, col].plot(xr[plot],yr[plot],'b-')
            axs[row, col].plot([xr[plot][-1], 0, xd[plot][-1]], [yr[plot][-1], 0, yd[plot][-1]], 'go-')
            #axs[row, col].set_aspect('equal')
            #axs[row, col].axis([-m, m, -m, m])
            axs[row, col].axis('equal')
            
            
            plot += 1
            
    plt.show()
