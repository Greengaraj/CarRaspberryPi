import RPi.GPIO as GPIO
import time

TRIG_PIN = 11
ECHO_PIN = 12

def getdistance():    
    GPIO.output(TRIG_PIN,GPIO.HIGH)
    time.sleep(0.000015)
    GPIO.output(TRIG_PIN,GPIO.LOW)
    while not GPIO.input(ECHO_PIN):
        pass
       
    t1 = time.time()
    while GPIO.input(ECHO_PIN):
        pass

    t2 = time.time()
    return (t2-t1) * 340 / 2

def loop():
    while True:
        print("Distance:" + str(getdistance()) + "m")
        time.sleep(0.5)

if __name__ == "__main__":
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        # 11 Needle, GPIO17
        GPIO.setup(TRIG_PIN,GPIO.OUT,initial=GPIO.LOW)
        # 12 Needle, GPIO18
        GPIO.setup(ECHO_PIN,GPIO.IN)
        time.sleep(1)
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()