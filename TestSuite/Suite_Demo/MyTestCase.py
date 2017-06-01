from . import LoadModule
from BaseFactor.CommonLib import *

class TestCase(BaseTest):
    """Docstring for TestCase"""

    def testSomeTime(sefl):
        """Docstring for testSomeThing"""
        sefl.assertTrue(True)
        print("My testSomeTime")

    def testSomeThing(sefl):
        """Docstring for testSomeThing"""
        sefl.assertTrue(False)
        print("My testSomeThing")