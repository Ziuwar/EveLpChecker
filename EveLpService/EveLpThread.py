###########################################
# Company: 		AS-Engineering
# File: 		EveLpThread.py	
# Name: 		Andreas Schroeder
# Date: 		23.12.2017
#
# Description: 	Thread generation for the different tasks
# Revision: 	R00 - Not tested
###########################################

# The mighty OS thread generator station

import threading, time
import EveDataMath
import EveMineralPrice
import EveLpCalc

ExitFlag = 0

class CalcThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("Starting " + self.name)
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
        if ExitFlag:
            threadName.exit()
        time.sleep(delay)
        EveMineralPrice.UpdateMineralMetaData()
        time.sleep(0.1)
        EveLpCalc.Calculator()
        print("\n\n%s: %s\n\n" % (threadName, time.ctime()))
        counter -= 1

#Create new threads
Calc1 = CalcThread(1,'CalcOne',10)

#Start new Thread
Calc1.start()

print("Exiting Main Thread")









