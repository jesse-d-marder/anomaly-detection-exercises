import numpy as np
import pandas as pd

def get_lower_and_upper_bounds(x, k = 1.5):
    """Returns lower and upper bounds of series x using IQR range rule with multiplier k"""
    q1 = x.quantile(0.25)
    q3 = x.quantile(0.75)
    iqr = q3-q1
    upper = q3 + k * iqr
    lower = q1 - k * iqr
    
    return upper, lower