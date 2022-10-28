import unittest
import mainM


class MyTestCase(unittest.TestCase):
    def test_something(self):
        # result = mainM.mainfunc('../test/testfile.c')
        with open('../test/testfile_c.answer') as f:
            expect = f.read()
        # self.assertEqual(expect, result)
        # self.assertEqual(expect, expect)
        self.assertEqual(expect, mainM.mainfunc('../test/testfile.c'))
        # self.assertEqual(expect, mainM.mainfunc)


if __name__ == '__main__':
    unittest.main()
    # unittest.main(module='mainM', argv='../test/testfile.c')
