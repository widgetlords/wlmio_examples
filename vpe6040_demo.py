# vpe6040 Analog Input SDAFE 4 Channel Demo Program
# Configure Channels as 0 to 20 mA, 0 to 5 VDC or 0 to 10 VDC
# configure = 0 for 0 to 5 VDC input
# configure = 1 for 0 to 20 mA input
# configure = 2 for 0 to 10 VDC input

import asyncio
from pywlmio import *

NodeID = 2  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

async def main():
  init()

  ai = VPE6040(NodeID)

  try:  
    await asyncio.gather(
      ai.ch1.configure(1),   # 1 = 0 to 20 mA input
      ai.ch2.configure(1),   # 1 = 0 to 20 mA input
      ai.ch3.configure(0),   # 0 = 0 to 5 VDC input
      ai.ch4.configure(2)    # 2 = 0 to 10 VDC input
    )
    
  except WlmioWrongNodeError:
    print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
  except WlmioInternalError:
    print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

  while True:
    try:  
      a = await asyncio.gather(
        ai.ch1.read(),       # Reading in uA 
        ai.ch2.read(),       # Reading in uA 
        ai.ch3.read(),       # Reading in mV 
        ai.ch4.read()        # Reading in mV 
      )

      print("Module VPE6040 NodeID = %d" % NodeID)
      print("Reading Array = ", a)               # Array holds all input channel readings 
      print("AI 1 = %5.03f mA" % (a[0]/1000))
      print("AI 2 = %5.03f mA" % (a[1]/1000))
      print("AI 3 = %5.03f VDC" % (a[2]/1000))
      print("AI 4 = %5.03f VDC" % (a[3]/1000))
      print("")

    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed     

    await asyncio.sleep(1)
 
asyncio.run(main(), debug=True)