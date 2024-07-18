    """ Animation function 

    Generates an animation based on the exoplanetary system input 

    Args: 
        a_s (array): semimajor axes (AU) 
        pers (array): periods of planets 
        rs (array): planetary radii (R_jup)
        rstar (float): stellar radius (R_sun)
        norbs (int): number of orbits desired in animation 
        es (array): eccentricities of planets 
        tstar (float): temperature of star (K)
        system (string): system to make the animation of 
        dir (string): directory in which to save animation (default current directory)

        Note: units are not important, as all quantities will be scaled relative to each other. 
        As long as all values use the same units, any unit system works. 

    Returns: 
        Saved animation file (.gif)
        
    """


    """ Query function 

    Queries NASA Exoplanet archive and obtains system parameters for desired system 

    Args: 
        system_name (string): system to query parameters for 

    Returns: 
        planet_radius (array): radii of planets in system 
        orbital_period (array): orbital periods of planets in system 
        semi_major_axis (array): semimajor axes of planets in system 
        planet_mass (array): masses of planets in system
        eccentricity (array): eccentricities of planets in system 
        stellar_radius (float): radius of star in system 
        stellar_temp (float): temperature of star in system
        number_of_planets (int): number of planets in system 
        
    """

    """ Sun color selector 

    Selects a color for plotting the star based on its temperature 

    Args: 
        teff (float): stellar temperature (K)

    Returns: 
        color (string): color in which to plot star 
        
    """

    """ Calls query and animation function 

    Queries exoplanet database to generate an animation based on the exoplanetary system input 

    Args: 
        system (string): system to make the animation of 
        norbs (int): number of orbits desired in animation 
        dir (string): directory in which to save animation (default current directory)

    Returns: 
        Saved animation file (.gif)
        
    """