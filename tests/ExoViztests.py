#!/usr/bin/env python
# coding: utf-8

# In[1]:


from astropy import units as u
from parameterquery import query_parameters
import anim_function
from anim_function import animator


# In[16]:


def animator_test():
    
    """
    
    Testing animation function to make sure it's animating the right number of planets
    
    """
    
    planet_parameters = query_parameters('KELT-9')
    
    rs_test = planet_parameters[0]
    pers_test = planet_parameters[1]
    a_s_test = planet_parameters[2]
    m_s_test = planet_parameters[3]
    es_test = planet_parameters[4]
    rstar_test = planet_parameters[5]
    tstar_test = planet_parameters[6]
    number_of_planets_test = planet_parameters[7]
    
    assert number_of_planets_test == len(a_s_test)


# In[17]:


animator_test()


# In[ ]:




