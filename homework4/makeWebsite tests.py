from makeWebsite import *
import unittest


class Testmakeweb(unittest.TestCase):

    def setUp(self):
        self.resume = resume.txt

    def TestGetName(self):
        self.assertEqual(GetName(self.resume), 'I.M. Student')
        self.assertRaises(ValueError, GetName('123'))

unittest.main()
