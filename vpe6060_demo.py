# vpe6060 Digital Input 4 Channel Demo Program
# Configure Channels as Discrete ON/OFF Inputs

import asyncio
from pywlmio import *

NodeID = 6  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

async def main():
  init()

  di = VPE6060(NodeID)

  try:
    await asyncio.gather(
      di.ch1.configure(0,0,0),   # mode = 0, polarity = 0, bias = 0
      di.ch2.configure(0,0,0),   # mode = 0, polarity = 0, bias = 0
      di.ch3.configure(0,0,0),   # mode = 0, polarity = 0, bias = 0
      di.ch4.configure(0,0,0)    # mode = 0, polarity = 0, bias = 0
   )

  except WlmioWrongNodeError:
    print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
  except WlmioInternalError:
    print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed
  
  while True:
    try: 
      a = await asyncio.gather(
        di.ch1.read(),
        di.ch2.read(),
        di.ch3.read(),
        di.ch4.read()
      )

      print("Module VPE6060 NodeID = %d" % NodeID)
      print("Reading Array = ", a)  # Array holds all input channel readings 
      print("DI Input 1 = " , a[0], " 1=ON, 0=OFF")
      print("DI Input 2 = " , a[1], " 1=ON, 0=OFF")
      print("DI Input 3 = " , a[2], " 1=ON, 0=OFF")
      print("DI Input 4 = " , a[3], " 1=ON, 0=OFF")
      print("")
    
    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed
   
    await asyncio.sleep(1)

asyncio.run(main(), debug=True)