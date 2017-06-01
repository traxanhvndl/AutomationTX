import unittest
import os
import sys
import shutil
import glob
import re
import time

class BaseTest(unittest.TestCase):
    """Docstring for BaseTest"""

    def setUp(self):
        """Docstring for setUp"""
        print("Setup")

    def tearDown(self):
        """Docstring for tearDown"""
        print("Teardown")

    def run(self, result=None):
        """Docstring for run"""
        try:
            self.origTestMethodName = self._testMethodName
            self._testMethodName = "_testRetryWrapper"
            super(BaseTest, self).run(result)
            self._testMethodName = self.origTestMethodName
        except Exception as e:
            raise e

    def _testRetryWrapper(self, a,b,c):
        """Docstring for _testRetryWrapper"""
        testMethod = getattr(self, self.origTestMethodName)
        retryAttemptsLeft = 0
        while True:
            global test_method
            test_method = self.origTestMethodName
            try:
                testMethod()
                break
            except KeyboardInterrupt as err:
                print(sys.exc_info()[:2])
                print("[User cancelled]", 31, 0, 0, 0)
                raise
            except:
                if retryAttemptsLeft == 0:
                    self._testMethodName = self.origTestMethodName
                    raise
                else:
                    print("Reexecution failed test " + self.origTestMethodName + ", " + str(retryAttemptsLeft) + " times left!")
                    retryAttemptsLeft = retryAttemptsLeft - 1
                    self.fu

    def functionName(a, b):
        """Docstring for functionName"""
