import time

from ulab import numpy as np

from hal.coil_system import compute_throttle
from hal.hal import CoilDriver
from orbit.igrf import igrf_eci
from orbit.orbital_state import Orbit

# Setup HAL
coil_directions = CoilDriver.get_dirs()

# Compute Earth Field Compensation
EARTH_LOCAL_FIELD = np.array([-0.7, -6.8, -24.7]) * 1e-6  # TODO: update and maybe use magneto in loop
EARTH_FIELD_COMPENSATION = compute_throttle(-EARTH_LOCAL_FIELD)

# Setup Orbit
INITAL_STATE = [146816.531, -4609452.33, -5075051 / 24, -991.33, 3176.59, -2892.11]
orbit_prop = Orbit(int(time.time()), np.array(INITAL_STATE))

while True:
    # Compute Current position
    current_time = int(time.time())
    eci_position = orbit_prop.get_eci_position(current_time)

    # Compute Magnetic field in ECI and required throttles to acheive it
    mag_field = igrf_eci(current_time, eci_position)
    throttles = compute_throttle(mag_field)

    # Excite coils
    CoilDriver.set_throttles(throttles + EARTH_FIELD_COMPENSATION)

    time.sleep(0.1)
