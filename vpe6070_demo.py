# vpe6070 Analog Output 0-10 VDC Module 4 Channel
# Demo Program sources outputs:
# 1 VDC on Channel 1
# 2 VDC on Channel 2
# 5 VDC on Channel 3
# 10 VDC on Channel 4

import asyncio
from pywlmio import *

NodeID = 4  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

async def main():
  init()

  vo = VPE6070(NodeID)

  while True:
    try:
      await asyncio.gather(
        vo.ch1.write(1000),  # Values written in mV (1 VDC)
        vo.ch2.write(2000),  # Values written in mV (2 VDC)
        vo.ch3.write(5000),  # Values written in mV (5 VDC)
        vo.ch4.write(8000)   # Values written in mV (10 VDC)
      )

    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

    await asyncio.sleep(1)

asyncio.run(main(), debug=True)