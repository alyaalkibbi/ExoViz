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
