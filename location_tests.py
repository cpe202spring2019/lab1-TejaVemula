import unittest
from location import *

class TestLab1(unittest.TestCase):

    def test_repr(self):
        loc = Location("SLO", 35.3, -120.7)
        self.assertEqual(repr(loc),"Location('SLO', 35.3, -120.7)")
        loc2 = Location("OSOS", 17.38, -9231.0000000000000000000000000000000000000000000000000000000000000000000000001)
        self.assertEqual(repr(loc2),"Location('OSOS', 17.38, -9231.0)")
    
    def test_eq(self):
        base = Location("SLO", 35.7, -120.7)

        loc1 = Location("SLO", 35.7,-120.7)
        self.assertEqual(loc1,base)
        loc2 = Location("SLO", 45.3,-120.7)
        self.assertNotEqual(loc2,base)
        loc3 = Location("slo", 35.3,-120.7)
        self.assertNotEqual(loc3,base)
        loc4 = Location("SLO", 35.3,-120.3)
        self.assertNotEqual(loc4,base)
        loc5 = Location("SLO", 35.3,-130.7)
        self.assertNotEqual(loc5,base)
        loc6 = Location("SLO", 35.3, 120.7)
        self.assertNotEqual(loc6,base)
        loc7 = Location("OSOS", 35.3,-120.7)
        self.assertNotEqual(loc7,base)
        loc8 = Location("SLO", -35.3,-120.7)
        self.assertNotEqual(loc8,base)

        base2 = Location("SLO", 36, 120)
        loc9 = Location("SLO", 36, 120)
        self.assertEqual(loc9,base2)




    
    # Add more tests!

if __name__ == "__main__":
        unittest.main()
