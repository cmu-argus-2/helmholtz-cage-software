from adafruit_motor import motor
from adafruit_motor.motor import DCMotor
from pwmio import PWMOut
import board


def define_motor(IN1: PWMOut, IN2:PWMOut) -> DCMotor:

    # Define DCMotor
    coil = DCMotor(IN1, IN2)

    # Set fast decay on
    coil.decay_mode = motor.FAST_DECAY

    return coil

def define_pwm_pin(pin_number: int) -> PWMOut:
    '''
        Defines a Pin for H-bridge Control
        Input: an Integer GPIO pin
        Output: an instance of pwmio.PWMOut linked to the specified GPIO pin
    '''
    pin_name = 'GP' + str(pin_number)

    try:
        pin = PWMOut(getattr(board, pin_name), frequency=100000)
    except Exception as e:
        print(e)
        # raise Exception(f"Board does not have an attribute {pin_name}")
    
    return pin
