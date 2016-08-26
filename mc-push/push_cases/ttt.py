import unittest
import HTMLTestRunner

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    report_title = u'E'
    desc = u'tRunner'
    filename = 'D:\\ExampleReport.html'
    testsuite = unittest.TestSuite()
    testsuite.addTest(TestStringMethods("test_isupper"))
    testsuite.addTest(TestStringMethods("test_split"))
    fp=file(filename,'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title='Report_title',description='Report_description')  
    runner.run(testsuite) 