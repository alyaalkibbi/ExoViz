import matplotlib.pyplot as plt
#from matplotlib.animation import FuncAnimation
import matplotlib.animation as an
import numpy as np

def ellipse(phi,a,e):
    b = np.sqrt(1-e**2) * a 
    return np.array([a*np.cos(phi), b*np.sin(phi)])

def suncolor(teff):
    if teff < 3500:
        return 'red'

    if teff >= 3500 & teff < 5000:
        return 'orange'
    
    if teff >= 5000 & teff < 8000:
        return 'yellow'
    
    if teff >= 8000 & teff < 15000:
        return 'white'
    
    if teff >= 15000:
        return 'blue'

def circle(phi,r):
    return np.array([r*np.cos(phi), r*np.sin(phi)])

def animator(a_s,pers,rs,rstar,norbs,es,tstar,system):

    #rs = rs * u.R_jupiter
    #pers = pers * u.day
    #a_s = a_s * u.au
    #mp = kelt9b_array[3] * u.M_jupiter
    #rstar = rstar * u.R_sun
    #tstar = tstar * u.K

    rsun = 7.e10
    rstar = rstar/rsun

    nplanets = len(a_s)

    a_plot = np.max(a_s)

    norma = np.min(a_s)
    normper = np.min(pers)

    rearth = 6.37e8
    normr = rearth

    fig, ax = plt.subplots()
    ax.set_aspect("equal")
    ax.axis([-2*a_plot,2*a_plot,-2*a_plot,2*a_plot])
    sun = ax.plot(0,0, marker="o",markersize = 5*rstar,color=suncolor(tstar)) 

    if nplanets == 1: 
        
        a1 = a_s[0]/norma
        per1 = pers[0]/normper
        r1 = rs[0]/normr

        p1, = ax.plot(0,a1, marker="o",markersize = r1)

        def update(phi):
            x1,y1 = ellipse(phi/per1,a1,es[0])
            p1.set_data([x1],[y1])
            return p1,

        ani = an.FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))
        ani.save(str(system)+'.gif')

        from IPython.display import HTML
        HTML(ani.to_jshtml())
 
    if nplanets == 2: 

        a1 = a_s[0]/norma
        per1 = pers[0]/normper
        r1 = rs[0]/normr
        a2 = a_s[1]/norma
        per2 = pers[1]/normper
        r2 = rs[1]/normr
        
        p1, = ax.plot(0,a1, marker="o",markersize = r1)
        p2, = ax.plot(0,a2, marker="o",markersize = r2)

        def update(phi):
            x1,y1 = ellipse(phi/per1,a1,es[0])
            x2,y2 = ellipse(phi/per2,a2,es[1])
            p1.set_data([x1],[y1])
            p2.set_data([x2],[y2])
            return p1,p2,

        ani = an.FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))
        ani.save(str(system)+'.gif')

        from IPython.display import HTML
        HTML(ani.to_jshtml())

    if nplanets == 3: 

        a1 = a_s[0]/norma
        a2 = a_s[1]/norma
        a3 = a_s[2]/norma
        per1 = pers[0]/normper
        per2 = pers[1]/normper
        per3 = pers[2]/normper
        r1 = rs[0]/normr
        r2 = rs[1]/normr
        r3 = rs[2]/normr
        
        p1, = ax.plot(0,a1, marker="o",markersize = r1)
        p2, = ax.plot(0,a2, marker="o",markersize = r2)
        p3, = ax.plot(0,a3, marker="o",markersize = r3)

        def update(phi):
            x1,y1 = ellipse(phi/per1,a1,es[0])
            x2,y2 = ellipse(phi/per2,a2,es[1])
            x3,y3 = ellipse(phi/per3,a3,es[2])
            p1.set_data([x1],[y1])
            p2.set_data([x2],[y2])
            p3.set_data([x3],[y3])
            return p1,p2,p3,

        ani = an.FuncAnimation(fig, update, interval=10, blit=True, repeat=True,
                        frames=np.linspace(0,norbs*2*np.pi,360, endpoint=False))
        ani.save(str(system)+'.gif')

        from IPython.display import HTML
        HTML(ani.to_jshtml())
