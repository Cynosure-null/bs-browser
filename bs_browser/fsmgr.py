#! bin/python3

import os
import datetime
import LOG
# Each utility has a file that has a class

class FileUtils:
    def __init__(self, dir = "./"):
        self.dir = dir
        self.firstRunPath = "{}.config/firstRun"
        self.firstRunPath = self.firstRunPath.format(self.dir)

        # TODO: stuff

    def isFirstRun(self):
        try:
            open(self.firstRunPath)
        except:
            return True
        else:
            return False

    def workingDir(self):
        return self.dir

    def firstRun(self):
        if self.isFirstRun() ==  True:
            firstRunWriteOp = open(self.firstRunPath, "w")
            firstRunString = "FIRST RUN AT: {}"
            firstRunString = firstRunString.format(datetime.datetime.now())
            firstRunWriteOp.write(firstRunString)
            firstRunWriteOp.close()

            logWriteOp = open(self.firstRunPath, "w")
            logWriteOp.write("---START LOG---")
            logWriteOp.close()
        else:
            LOG.Logger.new("DEBUG","fsmgr.FileUtils.firstRun ran but not needed")




