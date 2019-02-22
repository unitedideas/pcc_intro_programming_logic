import lab4
import unittest



class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(lab4.junk_mail(), 'yes')
