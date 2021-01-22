# vpe6030 Relay Module 4 Channel
# Demo Program Alternates Relays ON and OFF every 1 Second

import asyncio
from pywlmio import *

async def main():
  init()

  NodeID = 5  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

  kout = VPE6030(NodeID)

  while True:
    try:
      await asyncio.gather(
        kout.ch1.write(1),     # write relay K1 ON
        kout.ch2.write(0),     # write relay K2 OFF
        kout.ch3.write(1),     # write relay K3 ON
        kout.ch4.write(0)      # write relay K4 OFF
      )
    
      a = await asyncio.gather(
        kout.ch1.read(),
        kout.ch2.read(),
        kout.ch3.read(),
        kout.ch4.read()
      )
      
      print("Module VPE6030 NodeID = %d" % NodeID)
      print("Reading Array = ", a)   # Array holds all input channel readings 
      print("Relay K1 = " , a[0])
      print("Relay K2 = " , a[1])
      print("Relay K3 = " , a[2])
      print("Relay K4 = " , a[3])
      print("")
    
    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed
  
    await asyncio.sleep(1)

    try:
      await asyncio.gather(
        kout.ch1.write(0), # write relay K1 OFF
        kout.ch2.write(1), # write relay K2 ON
        kout.ch3.write(0), # write relay K3 OFF
        kout.ch4.write(1)  # write relay K4 ON
      )
    
      a = await asyncio.gather(
        kout.ch1.read(),
        kout.ch2.read(),
        kout.ch3.read(),
        kout.ch4.read()
      )
    
      print("Module VPE6030 NodeID = %d" % NodeID)
      print("Reading Array = ", a)   # Array holds all input channel readings 
      print("Relay K1 = " , a[0])
      print("Relay K2 = " , a[1])
      print("Relay K3 = " , a[2])
      print("Relay K4 = " , a[3])
      print("")
 
    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed
 
    await asyncio.sleep(1)

asyncio.run(main(), debug=True)