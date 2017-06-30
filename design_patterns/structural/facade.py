# -*- encoding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
import time

SLEEP = 0.1


class TC1:

    def run(self):
        print("##### In Test 1 #####")
        time.sleep(SLEEP)
        print("setting up")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC2:

    def run(self):
        print("##### In Test 2 #####")
        time.sleep(SLEEP)
        print("setting up")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TC3:

    def run(self):
        print("##### In Test 2 #####")
        time.sleep(SLEEP)
        print("setting up")
        time.sleep(SLEEP)
        print("Tearing down")
        time.sleep(SLEEP)
        print("Test Finished\n")


class TestRunner:

    def __init__(self):
        self.tc1 = TC1()
        self.tc2 = TC2()
        self.tc3 = TC3()
        self.tests = [self.tc1, self.tc2, self.tc3]

    def runAll(self):
        [i.run() for i in self.tests]


if __name__ == '__main__':
    testrunner = TestRunner()
    testrunner.runAll()
