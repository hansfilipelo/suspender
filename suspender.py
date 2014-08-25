#!/usr/bin/python

#  suspender.py
#
#  Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host.
#
#  Created by hansfilipelo & tobyndax, 2014-08-25.
#

import sys, getopt

if len(sys.argv) != 3:
    print ""
    print "Multi-threaded suspender for VMware ESXi virtual machines. Suspends all machines on a given host. "
    print ""
    print "Created by: hansfilipelo & tobyndax"
    print ""
    print "Usage: "
    print "    python suspender.py esxiHostname nrOfSimoultaniousSuspends"
    sys.exit
else:
    print "You gave two args. "