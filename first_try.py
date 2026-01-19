from machine import Pin, PWM
import time

# ------------------- Setup -------------------
# Speaker
speaker = PWM(Pin(15)) 
speaker.duty_u16(0)

# Buttons
btn_coin = Pin(16, Pin.IN, Pin.PULL_UP)
btn_laser = Pin(17, Pin.IN, Pin.PULL_UP)
btn_explo = Pin(18, Pin.IN, Pin.PULL_UP)

# LEDs 
led_coin = Pin(22, Pin.OUT)
led_laser = Pin(26, Pin.OUT)
led_explo = Pin(27, Pin.OUT)

# ------------------- Sound Effects -------------------
def coin_sound():
    led_coin.on()
    speaker.duty_u16(30000)
    for f in range(800, 1200, 20):
        speaker.freq(f)
        time.sleep(0.01)
    speaker.duty_u16(0)
    led_coin.off()

def laser_sound():
    led_laser.on()
    speaker.duty_u16(30000)
    for f in range(1500, 400, -40):
        speaker.freq(f)
        time.sleep(0.005)
    speaker.duty_u16(0)
    led_laser.off()

def explosion_sound():
    led_explo.on()
    speaker.duty_u16(30000)
    for _ in range(3):
        for f in range(300, 80, -10):
            speaker.freq(f)
            time.sleep(0.01)
    speaker.duty_u16(0)
    led_explo.off()

# ------------------- Button Edge Detection -------------------
prev_coin = 1
prev_laser = 1
prev_explo = 1

# ------------------- Main Loop -------------------
while True:
    # Coin button
    cur = btn_coin.value()
    if prev_coin == 1 and cur == 0:
        coin_sound()
    prev_coin = cur

    # Laser button
    cur = btn_laser.value()
    if prev_laser == 1 and cur == 0:
        laser_sound()
    prev_laser = cur

    # Explosion button
    cur = btn_explo.value()
    if prev_explo == 1 and cur == 0:
        explosion_sound()
    prev_explo = cur

    time.sleep(0.01)
