import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_estimate(self) : 
       for j in range(10) : 
           nvars = j*100
           mean, bar = np.pi/4, np.sqrt( (np.pi/4)*(1-(np.pi/4)) / nvars )*st.norm.ppf( (0.99 + 1) / 2 )
           self.assertTrue( np.abs(circle_estimate(nvars) - mean)<bar ) 
