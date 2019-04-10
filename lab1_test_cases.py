import unittest
from lab1 import *

 # A few test cases.  Add more!!!
class TestLab1(unittest.TestCase):

    def test_max_list_iter(self):
        """add description here"""
        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            max_list_iter(tlist)

        list1 = [1,2,3,4,5,6,7,8]
        self.assertEqual(max_list_iter(list1), 8)
        list2 = [-1,-2,-3,-4,-5,-6,-7,-8]
        self.assertEqual(max_list_iter(list2), -1)
        list3 = [1.1,2.2,3.3,4.3,5.3,6.2,7.4,8.1]
        self.assertEqual(max_list_iter(list3), 8.1)
        list4 = [2,2,2,2,5,6,5,8]
        self.assertEqual(max_list_iter(list4), 8)
        list5 = [32,2355,53252,523523,25352,235523,52523,800000]
        self.assertEqual(max_list_iter(list5), 800000)
        list6 = [1,2,3,4,8,8,8,8]
        self.assertEqual(max_list_iter(list6), 8)
        list7 = [0,0,0,0,0,0,0,0,0]
        self.assertEqual(max_list_iter(list7),0)


    def test_reverse_rec(self):
        self.assertEqual(reverse_rec([1,2,3]),[3,2,1])
        self.assertEqual(reverse_rec([1,2,3,1]),[1,3,2,1])
        self.assertEqual(reverse_rec([1,2,3,2,1]),[1,2,3,2,1])
        self.assertEqual(reverse_rec([-1,-2,-3]),[-3,-2,-1])
        self.assertEqual(reverse_rec([]),[])


        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            reverse_rec(tlist)

    def test_bin_search(self):
        list_val =[0,1,2,3,4,7,8,9,10]
        low = 0
        high = len(list_val)-1
        self.assertEqual(bin_search(4, 0, len(list_val)-1, list_val), 4 )
        l2 = [-5,-4,-3,-2,-1]
        self.assertEqual(bin_search(-4, low, len(l2)-1, l2), 1)
        l3 = [1,2,3,4,5,7]
        self.assertEqual(bin_search(6, low, len(l3)-1,l3), None)
        l4 = [1,1,1,1,1,1]
        self.assertEqual(bin_search(1, low, len(l4)-1,l4), 2)
        l5 = [4,40,400,4000,40000,400000]
        self.assertEqual(bin_search(400, low, len(l5)-1,l5), 2)
        


        tlist = None
        with self.assertRaises(ValueError):  # used to check for exception
            bin_search(6, low, 10, tlist)

if __name__ == "__main__":
        unittest.main()

    
