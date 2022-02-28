#! bin/python

import fsmgr
import LOG

c_fs = fsmgr.FileUtils()
c_log = LOG.Logger()
if c_fs.isFirstRun():
    c_fs.firstRun()
else:
    c_log.new("WARN", "Bepis")