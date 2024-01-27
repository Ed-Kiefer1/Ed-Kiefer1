import RPi.GPIO as GPIO
import time

# Motor 1 configuration
motor1_dir_pin1 = 22  # GPIO pin for direction control 1
motor1_dir_pin2 = 27  # GPIO pin for direction control 2
motor1_pwm_pin = 12   # PWM pin for motor 1

# Motor 2 configuration
motor2_dir_pin1 = 22  # GPIO pin for direction control 1
motor2_dir_pin2 = 24  # GPIO pin for direction control 2
motor2_pwm_pin = 13  # PWM pin for motor 2

# Set up GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup([motor1_dir_pin1, motor1_dir_pin2, motor1_pwm_pin,
            motor2_dir_pin1, motor2_dir_pin2, motor2_pwm_pin], GPIO.OUT)

# Initialize PWM
motor1_pwm = GPIO.PWM(motor1_pwm_pin, 800)  # Initialize PWM with a frequency of 8000 Hz
motor2_pwm = GPIO.PWM(motor2_pwm_pin, 800)

# Start PWM
motor1_pwm.start(0)  # Start PWM with a duty cycle of 0 (off)
motor2_pwm.start(0)

def set_motor_speed(pwm, speed):
    pwm.ChangeDutyCycle(speed)

def set_motor_direction(dir_pin1, dir_pin2, direction):
    GPIO.output(dir_pin1, direction)
    GPIO.output(dir_pin2, not direction)

def stop_motors():
    motor1_pwm.ChangeDutyCycle(0)
    motor2_pwm.ChangeDutyCycle(0)

# Example: Move forward for 2 seconds
try:
    set_motor_direction(motor1_dir_pin1, motor1_dir_pin2, GPIO.HIGH)  # Set direction for motor 1
    set_motor_direction(motor2_dir_pin1, motor2_dir_pin2, GPIO.HIGH)  # Set direction for motor 2

    set_motor_speed(motor1_pwm, 50)  # Set speed for motor 1 (0-100)
    set_motor_speed(motor2_pwm, 50)  # Set speed for motor 2 (0-100)

    time.sleep(2)  # Move forward for 2 seconds

finally:
    stop_motors()  # Stop motors when done

    # Clean up GPIO
    GPIO.cleanup()
