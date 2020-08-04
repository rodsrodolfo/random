import numpy as np
import matplotlib.pyplot as plt

al=50
lg=50

a=np.random.randint(2, size=(al,lg))

p=plt.imshow(a, cmap='gray', interpolation='None')

while True:
    x = np.pad(a, 1, mode='wrap')
    y=np.zeros((al,lg), dtype=np.int)
    for c in range(1,al+1):
        for d in range(1,lg+1):
            v=sum(map(sum,x[c-1:c+2,d-1:d+2]))-x[c,d]
            if x[c][d]==1:
                if v==3 or v==2:
                    y[c-1][d-1]=1
                else:
                    y[c-1][d-1]=0
            if x[c][d]==0:
                if v!=3:
                    y[c-1][d-1]=0
                else:
                    y[c-1][d-1]=1
        
    a=y
    p.set_data(a)
    plt.pause(.00000000000000001)
