# vpe6080 Analog Input Thermistor Module 8 Channel
# Demo Program reads 8 channels
# Thermistor 10K Ohm 3380 Beta installed in Channel 1 to read room temperature

import asyncio
from pywlmio import *

NodeID = 7  #NodeID location is the Bacplane ID (Jumpers) and Power Supply Slot location

async def main():
  init()

  th = VPE6080(NodeID)

  try:
    await asyncio.gather(
      th.ch1.configure(1),  # Channel Enabled, default 3380 Beta, 25°C Room Value
      th.ch2.configure(0),  # Channel Disabled
      th.ch3.configure(0),  # Channel Disabled
      th.ch4.configure(0),  # Channel Disabled
      th.ch5.configure(0),  # Channel Disabled
      th.ch6.configure(0),  # Channel Disabled
      th.ch7.configure(0),  # Channel Disabled
      th.ch8.configure(0)   # Channel Disabled
    )
    
  except WlmioWrongNodeError:
    print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
  except WlmioInternalError:
    print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed

  while True:
    try:
      a = await asyncio.gather(
        th.ch1.read(),      # Read Channel 1
        th.ch2.read(),      # Read Channel 2
        th.ch3.read(),      # Read Channel 3
        th.ch4.read(),      # Read Channel 4
        th.ch5.read(),      # Read Channel 5
        th.ch6.read(),      # Read Channel 6
        th.ch7.read(),      # Read Channel 7
        th.ch8.read()       # Read Channel 8
      )

      print("Module VPE6080 NodeID = %d" % NodeID)
      print("Reading Array = ", a)  # Array holds all input channel readings 
                          
      # Readings scaled x10 and are in °Kelvin, add 273.15 to convert to °C  
      print("Channel 1 Thermistor = %0.1f Deg C" % (a[0] / 10 - 273.15))   # Print channel 1
      print("")

    except WlmioWrongNodeError:
      print("Error NodeID = %d Wrong module installed" % NodeID)  # Error Check if wrong type of module installed
    except WlmioInternalError:
      print("Error NodeID = %d Timed out" % NodeID)               # Error Check - Typically module not installed
      
    await asyncio.sleep(1)
 
asyncio.run(main(), debug=True)