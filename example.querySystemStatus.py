#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.l.klaus AT web.de


#   This file is part of netio230a.
#
#   netio230a is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   netio230a is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with netio230a.  If not, see <http://www.gnu.org/licenses/>.



# example how to use the netio230a class

## import the netio230a class:
import avrnetio
## for debugging (set debug mark with pdb.set_trace() )
import pdb
## for sys.exit(1)
import sys


host = "192.168.100.3"


def main():
    try:
        netio = avrnetio.avrnetio(host)
    except StandardError:
        print("could not connect")
        sys.exit(1)
    systemTime = netio.getSystemTime()
    
    netio = None
    
    # print response
    print "\n--------- successfully queried the Koukaam NETIO 230A ---------"
    print "system time: %s" % (systemTime)
    print "---------------------------------------------------------------- \n"
    

if __name__ == '__main__':
    main()


