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
import EveMarketData

ExitFlag = 0

class CalcThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
    def run(self):
        print("#-Starting " + self.name + "-#\n\n")
        print_time(self.name, 5, self.counter)
        print("Exiting " + self.name)

def print_time(threadName, counter, delay):
    while counter:
		
        if ExitFlag:
            threadName.exit()
            
        time.sleep(delay)
        EveMineralPrice.UpdateMineralMetaData()
        time.sleep(1)
        EveMarketData.UpdateJitaMaxSell()
        time.sleep(1)
        EveLpCalc.ItemUpdate()
        
        print("\n\n%s: %s\n\n" % (threadName, time.ctime()))
        
        counter -= 1

#Create new threads
Calc1 = CalcThread(1,'Eve LP server',60)

#Start new Thread
Calc1.start()

print("#-Main thread created-#\n")









