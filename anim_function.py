import matplotlib.pyplot as plt
import matplotlib.animation
import numpy as np


def circle(phi,r):
    return np.array([r*np.cos(phi), r*np.sin(phi)])

def animator(rs,pers,norbs):

    nplanets = len(rs)

    if nplanets == 1: 

        r1 = rs[0]
        per1 = pers[0]/pers[0]

        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        sun = ax.plot(0,0, marker="o")
        
        p1, = ax.plot(0,1, marker="o")

        def update(phi):
            x1,y1 = circle(phi,r1)
            p1.set_data([x1],[y1])
            return p1,

        ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))

        from IPython.display import HTML
        HTML(ani.to_jshtml())
 
    if nplanets == 2: 

        r1 = rs[0]
        r2 = rs[1]
        per1 = pers[0]/pers[0]
        per2 = pers[1]/pers[0]

        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        sun = ax.plot(0,0, marker="o")
        
        p1, = ax.plot(0,1, marker="o")
        p2, = ax.plot(0,1, marker="o")

        def update(phi):
            x1,y1 = circle(phi,r1)
            x2,y2 = circle(phi/per2,r2)
            p1.set_data([x1],[y1])
            p2.set_data([x2],[y2])
            return p1,p2,

        ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))

        from IPython.display import HTML
        HTML(ani.to_jshtml())

    if nplanets == 3: 

        r1 = rs[0]/rs[0]
        r2 = rs[1]/r1
        r3 = rs[2]/r1
        per1 = pers[0]/pers[0]
        per2 = pers[1]/per1
        per3 = pers[2]/per1

        fig, ax = plt.subplots()
        ax.set_aspect("equal")
        sun = ax.plot(0,0, marker="o")
        
        p1, = ax.plot(0,r1, marker="o")
        p2, = ax.plot(0,r2, marker="o")
        p3, = ax.plot(0,r3, marker="o")

        def update(phi):
            x1,y1 = circle(phi,r1)
            x2,y2 = circle(phi/per2,r2)
            x3,y3 = circle(phi/per3,r3)
            p1.set_data([x1],[y1])
            p2.set_data([x2],[y2])
            p3.set_data([x3],[y3])
            return p1,p2,p3,

        ani = FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))

        from IPython.display import HTML
        HTML(ani.to_jshtml())


animator([1,3,4],[2,6,7],2)