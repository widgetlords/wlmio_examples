# vpe6050 Analog Output 4-20 mA Module 4 Channel
# Demo Program sources outputs:
# 4 ma on Channel 1
# 8 ma on Channel 2
# 12 ma on Channel 3
# 20 ma on Channel 4

import asyncio
from pywlmio import *

NodeID = 3  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

async def main():
  init()

  ao = VPE6050(NodeID)
  
  try:
    await asyncio.gather(
      ao.ch1.configure(0),   # Configure as current output source
      ao.ch2.configure(0),   # Configure as current output source 
      ao.ch3.configure(0),   # Configure as current output source
      ao.ch4.configure(0)    # Configure as current output source
    )

  except WlmioWrongNodeError:
    print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
  except WlmioInternalError:
    print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

  while True:
    try:
      await asyncio.gather(
        ao.ch1.write(4000),  # Values written as uA (4 mA)
        ao.ch2.write(8000),  # Values written as uA (8 mA)
        ao.ch3.write(12000), # Values written as uA (12 mA)
        ao.ch4.write(20000)  # Values written as uA (20 mA)
      )

    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

    await asyncio.sleep(1)

asyncio.run(main(), debug=True)