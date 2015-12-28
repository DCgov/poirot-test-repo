#!/usr/bin/env python

import subprocess
import sys

COMMAND = "uname -a"

ssh = subprocess.Popen(["ssh", "192.168.178.05", COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
result = ssh.stdout.readlines()  # lots of frabjous information
if result == []:
    error = ssh.stderr.readlines()
    print >>sys.stderr, "ERROR: %s" % error
else:
    print result
