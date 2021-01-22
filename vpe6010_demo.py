#vpe6010 Power Supply Module Health Readings

import asyncio
from pywlmio import *

async def main():
  init()

  NodeID = 0  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location
    
  psu1 = VPE6010(NodeID)
 
  while True:
    try:
      a = await (psu1.ch1.read())
    
      #a array
      #a[0] = 5 VDC Bus Current in mA
      #a[1] = 5 VDC Bus Voltage in mVDC
      #a[2] = +V1 Input in mV
      #a[3] = +V2 Input in mV
      #a[4] = +V Output through Auctioneering Diode to Backplane in mV
      #a[5] = +V Output Current to Backplane in mA
 
      print("Power Supply VPE6010 Node %d" % NodeID)
      print("Power Supply Read Register Array = " , a)
      print("+5 VDC V Output = %.02f VDC" % (a[1]/1000))
      print("+5 VDC I Output = %.02f A" % (a[0]/1000))
      print("V1 VDC V Input  = %.02f VDC" % (a[2]/1000))
      print("V2 VDC V Input  = %.02f VDC" % (a[3]/1000))         
      print("Field V         = %.02f VDC" % (a[4]/1000))
      print("Field I         = %.03f A" % (a[5]/1000))
      print("")

    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

    await asyncio.sleep(1)

asyncio.run(main(), debug=True)