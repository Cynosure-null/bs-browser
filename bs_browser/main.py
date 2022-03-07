#! bin/python

import fsmgr
import log_

c_fs = fsmgr.FileUtils()
c_log = LOG.Logger()

try:
    c_fs.isFirstRun()
except:
    c_fs.firstRun()
    c_log.new("WARN", "Bepis")