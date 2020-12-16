import unittest
import scipy.stats
from main import *

class UnitTests(unittest.TestCase) :
    def test_estimate(self) : 
       for j in range(1,10) : 
           nvars = j*100
           mean, bar = np.pi/4, np.sqrt( (np.pi/4)*(1-(np.pi/4)) / nvars )*scipy.stats.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.abs(circle_estimate(nvars) - mean)<bar ) 
