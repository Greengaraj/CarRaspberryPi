import RPi.GPIO as GPIO
import time

def getdistance():

    #        
    GPIO.output(11,GPIO.HIGH)
    # Keep 10US or more
    time.sleep(0.000015)
    GPIO.output(11,GPIO.LOW)
    while not GPIO.input(12):
        pass
    #          
    t1 = time.time()
    while GPIO.input(12):
        pass
    # High level end stop counting
    t2 = time.time()
    #, Unit is rice
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
        GPIO.setup(11,GPIO.OUT,initial=GPIO.LOW)
        # 12 Needle, GPIO18
        GPIO.setup(12,GPIO.IN)
        time.sleep(1)
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()