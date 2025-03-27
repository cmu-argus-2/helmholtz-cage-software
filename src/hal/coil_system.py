from ulab import numpy as np

# Field generated in T vs % of throttle applied
FIELD_THROTTLE_X = 1.0
FIELD_THROTTLE_Y = 1.0
FIELD_THROTTLE_Z = 1.0

SYSID_KEY_MAP = {'X': FIELD_THROTTLE_X, 'Y':FIELD_THROTTLE_Y, 'Z':FIELD_THROTTLE_Z}

def compute_throttle(required_field, coil_dir: str = None):

    if isinstance(required_field, np.ndarray):
        if len(required_field) == 3:
            throttle = [0]*3
            throttle[0] = max(-1.0, min(required_field[0]/SYSID_KEY_MAP['X'], 1.0))
            throttle[1] = max(-1.0, min(required_field[1]/SYSID_KEY_MAP['Y'], 1.0))
            throttle[2] = max(-1.0, min(required_field[2]/SYSID_KEY_MAP['Z'], 1.0))

            return throttle
        else:
            raise Exception("TF?")
    else:
        field_per_throttle = SYSID_KEY_MAP[coil_dir]
        required_throttle = max(-1.0, min(required_field/field_per_throttle, 1.0))

    return required_throttle
