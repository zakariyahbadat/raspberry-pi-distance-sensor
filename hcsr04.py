import RPi.GPIO as GPIO
import time

# Pin numbers
TRIG = 23
ECHO = 24
BUZZER = 18  # This is Pi Pin 12 (GPIO 18)

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)
GPIO.setup(BUZZER, GPIO.OUT)

def get_distance():
    GPIO.output(TRIG, False)
    time.sleep(0.03)  # Super fast sensor refresh

    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    pulse_start = time.time()
    pulse_end = time.time()

    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    return round(distance, 2)

try:
    print("Rapid Alarm active! Move closer to hear it speed up.")
    while True:
        dist = get_distance()
        print(f"Distance: {dist} cm")

        # Start beeping if something is closer than 50 cm
        if dist < 50:
            # MAP DISTANCE TO BEEP SPEED:
            # If dist is 50cm, delay is about 0.3 seconds (slow beep)
            # If dist is 5cm, delay drops to 0.01 seconds (insanely fast beep!)
            beep_delay = max(0.01, min(0.3, dist / 150.0))
            
            # The beep itself is now ultra-short (0.02 seconds)
            GPIO.output(BUZZER, True)
            time.sleep(0.02)
            GPIO.output(BUZZER, False)
            
            # Wait for the calculated delay time
            time.sleep(beep_delay)
        else:
            # If nothing is close, check quietly every 0.1 seconds
            time.sleep(0.1)

except KeyboardInterrupt:
    print("\nStopping alarm...")
    GPIO.cleanup()
