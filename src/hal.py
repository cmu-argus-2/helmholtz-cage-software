from h_bridge_controller import define_motor, define_pwm_pin

class CoilDriver:
    
    COIL_X_PIN_PLUS = 0 # GPIO1
    COIL_X_PIN_MINUS = 2 # GPIO3

    COIL_Y_PIN_PLUS = 3 # GPIO5
    COIL_Y_PIN_MINUS = 7 # GPIO7

    COIL_Z_PIN_PLUS = 4 # GPIO9
    COIL_Z_PIN_MINUS = 5 # GPIO11

    # Define PWM Pins
    # Coil X
    PWM_XP = define_pwm_pin(COIL_X_PIN_PLUS)
    PWM_XM = define_pwm_pin(COIL_X_PIN_MINUS)

    # Coil Y
    PWM_YP = define_pwm_pin(COIL_Y_PIN_PLUS)
    PWM_YM = define_pwm_pin(COIL_Y_PIN_MINUS)

    # # Coil Z
    PWM_ZP = define_pwm_pin(COIL_Z_PIN_PLUS)
    PWM_ZM = define_pwm_pin(COIL_Z_PIN_MINUS)

    # Define Motors
    COIL_X = define_motor(PWM_XP, PWM_XM)
    COIL_Y = define_motor(PWM_YP, PWM_YM)
    COIL_Z = define_motor(PWM_ZP, PWM_ZM)

    @classmethod
    def get_dirs(cls):
        return ['X', 'Y', 'Z']
    
    @classmethod
    def set_throttle(cls, throttle: float, dir: str):

        coil = getattr(cls, 'COIL_' + dir)
        coil.throttle = max(-1.0, min(1.0, throttle))
