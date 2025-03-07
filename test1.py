from pathlib import Path
import rtds.case
import rtds.rscadfx
import rtds.constants as rc

import time
import struct

import rtds.rtx
import rtds.case


app = rtds.rscadfx.remote_connection()
#windSpeed = rtds.rtx.Runtime.get_object(,13731)

try:
    app.connect()
    # connect/launch RSCAD

    # disconnect from RSCAD and close application
    weak=app.open_case("C:\\Users\\cenli\\Documents\\RSCAD\\model\\weak grid model.rtfx")
    wind= weak.get_object_by_name("WindSPD","slider")
    #weak.run()  # Start the simulation

    print("Simulation started. Updating WindSPD dynamically...")

    start_time = time.time()  # Record start time

    # ✅ Update WindSPD continuously for 2 seconds
    while time.time() - start_time < 10:  
        new_value = 5 + (time.time() - start_time) * 2  # Example: Gradual increase
        wind.value=new_value  # ✅ Update slider
        time.sleep(0.2)  # Update every 200ms
        print(time.time())
finally:
    print(wind.value)
  