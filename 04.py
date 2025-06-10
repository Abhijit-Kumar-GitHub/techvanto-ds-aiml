# 9/6/25

"""

You work in XYZ Company as a Python developer. The company officials want
you to build a Python program.

Tasks To Be Performed:

1. Write a function that takes start and end of a range returns a pandas series
object containing numbers within that range.
In case the user does not pass start or end or both they should default to 1
and 10 respectively. E.g:
-> range_series() -> Should Return a pandas series from 1 to 10
range_series(5) -> Should Return a pandas series from 5 to
"""

import numpy as np
import pandas as pd

#creating a dummy dataset of pandas series having 25 elements


data = pd.Series(np.random.randint(1, 100, size=25), name='Random Numbers')

def range_series(start=1, end=10):
    if start is None:
        start = 1
    if end is None:
        end = 10
    return pd.Series(np.arange(start, end + 1), name='Range Series')

def main():
    
    





