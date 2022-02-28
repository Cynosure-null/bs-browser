#! bin/python

import datetime
import fsmgr

class Logger:
    def __init__(self):
        bullshitVar0 = None

    def new(self, priority, message):
        self.priority = priority
        self.message = message
        if self.priority == "DEBUG":
            prefix = "[INFO]: "
            colorCode = ""
            # White

        if self.priority == "WARN":
            prefix = "[WARNING]: "
            colorCode = ""
            # Yellow

        if self.priority == "ERROR":
            prefix = "[ERROR]: "
            colorCode = ""
            # Red
        # Format
        if fsmgr.FileUtils.isFirstRun() == False:
            logDir = str(fsmgr.FileUtils.workingDir())
            logDir = logDir + "log.txt"
            logWriteOp = open(logDir, "w")
            currentTime = str(datetime.datetime.now())
            currentTime = "(" + currentTime + ")"
            logWriteStr = colorCode + prefix + self.message + currentTime
            logWriteOp.write(logWriteStr, "a")
            logWriteOp.close()

            if self.priority == "WARN" or self.priority == "ERROR":
                print(logWriteStr)

            # Do main thing
        else:
            fsmgr.FileUtils.firstRun()
            logDir = str(fsmgr.FileUtils.workingDir())
            logDir = logDir + "log.txt"
            logWriteOp = open(logDir, "w")
            currentTime = str(datetime.datetime.now())
            currentTime = "(" + currentTime + ")"
            logWriteStr = colorCode + prefix + self.message + currentTime
            logWriteOp.write(logWriteStr, "a")
            logWriteOp.close()

            if self.priority == "WARN" or self.priority == "ERROR":
                print(logWriteStr)



