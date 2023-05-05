import unittest
from testcase.tooltestclass import tests

def all_test_case():
    discover = unittest.defaultTestLoader.discover(start_dir= './testcase/', pattern='test_login.py')
    return discover


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(all_test_case())