#!/Users/edelsonc/miniconda3/bin/python
"""

author: edelsonc
created: 04/20/2017
"""
import numpy
from scipy.stats import poisson
from functools import lru_cache


if __name__ == "__main__":
    d = HurricaneDist(12)
    print(d.posterior(10))
    d.update(33)
    print(d.posterior(10))
    