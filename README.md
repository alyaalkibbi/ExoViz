![Logo](https://media.discordapp.net/attachments/1261078446423937065/1263348861930307666/K2-138.gif?ex=669a9190&is=66994010&hm=a534f56aba85ac0a9aff424ff30e484c5df6b6f00bc3c9df7ba7e8534262e897&=&width=1248&height=936)

# ExoViz

[![DOI](https://zenodo.org/badge/829092140.svg)](https://zenodo.org/doi/10.5281/zenodo.12760958)

An exoplanet visualization code that queries the NASA Exoplanet Archive and creates simple animations of exoplanetary systems.

Installation
------------
To install the released version, type

    $ pip install ExoViz

which automatically installs the following dependencies if not present:

- `numpy`
- `matplotlib`
- `pandas`
- `datetime`
- `astropy`
- `Collections`

Example usage
-------------
```
from parameterquery import query_parameters
import anim_function
from anim_function import animator
from main import main

# Animate the KELT-9 system

example_planet = main(system = 'KELT-9', norbs = 3, dir = 'C:/Users/username/Downloads/')
```

Note to always put `/` at the end of the directory pathway in order to download the animation.
