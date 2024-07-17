from astropy import units as u
from parameterquery import query_parameters
import anim_function
from anim_function import animator

#example to use query to get planet_radius, orbital_period, semi_major_axis, planet_mass, eccentricity,
# stellar_radius, stellar_temp
def main(system, norbs):

    planets = query_parameters(system)
    
    rs = planets[0]
    pers = planets[1]
    a_s = planets[2]
    m_s = planets[3]
    es = planets[4]
    rstar = planets[5]
    tstar = planets[6]
    
    animator(a_s,pers,rs,rstar,norbs,es,tstar,system)
    


main('KELT-9', 4)
