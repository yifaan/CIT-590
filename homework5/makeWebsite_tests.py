from makeWebsite import *
import unittest


class makeWebtestcase(unittest.TestCase):

    def setUp(self):
        self.resume = 'resume.txt'
        self.newresume = 'resume_unittest.txt'

    def testGetName(self):
        self.assertEqual(GetName(self.resume), 'Yifan Yang')
        self.assertRaises(NameError, GetName, self.newresume)

    def testGetEmail(self):
        self.assertEqual(GetEmail(self.resume), 'Yifany@seas.upenn.edu')
        self.assertRaises(NameError, GetEmail, self.newresume)

    def testGetCourse(self):
        course = ['Programming Languages and Techniques',
                  'Feedback Control', 'Advanced Robotics']
        self.assertEqual(GetCourse(self.resume), course)

    def testGetProjects(self):
        projects = [
            'Robockey - A robot hockey competition of MEAM 510 Mechatronics class']
        self.assertEqual(GetProjects(self.resume), projects)

    def testGetEducation(self):
        Education = ['University of Pennsylvania, Philadelphia, PA, USA  -  Master of Science in Robotics',
                     'University of Birmingham, Birmingham, UK - Bachelor of Engineering in Mechanical Engineering',
                     'Huazhong University of Science and Technology, Wuhan, China  -  Bachelor of Engineering in Mechanical Engineering']

        self.assertEqual(GetEducation(self.resume), Education)

    def testIntro(self):
        self.assertEqual(intro('Yifan Yang', 'yifany@seas.upenn.edu'),
                         '<h1 >\nYifan Yang\n</h1>\n<p>\nyifany@seas.upenn.edu\n</p>')

    def testeduhtml(self):
        self.assertEqual(Eduhtml(['University']),'<h2>Education</h2>\n<ul>\n<li>\nUniversity\n</li>\n</ul>')

    def testProjecthtml(self):
        self.assertEqual(Projecthtml(['Proj']),'<h2>\nProjects\n</h2>\n<ul>\n<li>\n<p>\nProj\n</p>\n</li>\n</ul>')

    def testCoursehtml(self):
        self.assertEqual(Courseshtml(['a','b']),'<h3>\nCourses\n</h3>\n<span>\na, b\n</span>')

unittest.main()
