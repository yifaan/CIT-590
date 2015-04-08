from Racko import *

import unittest


class test_Racho(unittest.TestCase):

    def test_check_racho(self):
        result = check_racko([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertTrue(result, "testasserttrue")


unittest.main()
