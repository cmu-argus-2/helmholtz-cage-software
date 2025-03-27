from ulab import numpy as np

class Orbit:

    def __init__(self, start_time : int, initial_state: np.ndarray):
        
        self.position = initial_state[0:3]
        self.velocity = initial_state[3:6]
        self.time = start_time


    def get_eci_position(self, current_time: int) -> np.ndarray:

        # Propagate orbit
        position_norm = np.linalg.norm(self.position)
        velocity_norm = np.linalg.norm(self.velocity)

        # Calculate omega (angular velocity) vector
        omega = np.cross(self.position, self.velocity) / position_norm**2

        # Calculate rotation angle about omega
        theta = np.linalg.norm(omega) * (current_time - self.time)

        # Rotate position about omega by angle theta
        self.position = position_norm * (
            self.position * np.cos(theta) / position_norm
            + self.velocity * np.sin(theta) / velocity_norm
        )

        # Compute velocity using (v = omega x r)
        self.velocity = np.cross(omega, self.position)

        # Update time
        self.time = current_time

        return self.position

        