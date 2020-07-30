import statistics
import math

_sqrt2 = math.sqrt(2)

def cdf(z, mu=0.0, sigma=1.0):
    root2_sigma = sigma * _sqrt2
    return (statistics.erf((z-mu)/root2_sigma)+1)/2.0

def callPrice(s, x, r, sigma, t):
    a = (math.log(s/x) + (r + sigma * sigma/2.0) * t) / \
        (sigma * math.sqrt(t))
    b = a - sigma * math.sqrt(t)
    return s * cdf(a) - x * math.exp(-r * t) * cdf(b)
