#!/usr/bin/env python
# -*- encoding: UTF8 -*-

# Author: Philipp Klaus, philipp.l.klaus AT web.de


#   This file is part of avrnetio.
#
#   avrnetio is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   avrnetio is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with avrnetio.  If not, see <http://www.gnu.org/licenses/>.



# example how to use the avrnetio class

## import the avrnetio class:
import avrnetio
## for debugging (set debug mark with pdb.set_trace() )
import pdb
## for sys.exit(1)
import sys
## for NTC calculations
import electronics


host = "192.168.102.3"
refVoltage = 5

def main():
    try:
        netio = avrnetio.Avrnetio(host)
        netio.set_ref_ep(refVoltage)
    except StandardError:
        print("could not connect")
        sys.exit(1)
    ntc_voltage = netio.get_adcs_as_volts()[4]
    
    netio = None
    
    
    temperature = electronics.Ntc(4700.0,25.0+273,3580.0)
    temperature.Uvcc = refVoltage
    
    # print response
    print "\n--------- successfully queried the AVR-NET-IO with ethersex commands ---------"
    print "NTC voltage: %.3f V" % (ntc_voltage)
    print "temperature: %.1f °C" % (temperature.ntc_potential_to_temp(ntc_voltage)-273)
    print "---------------------------------------------------------------- \n"
    

if __name__ == '__main__':
    main()


