import unittest
import lab4


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(lab4.junk_mail(), 'yes')
