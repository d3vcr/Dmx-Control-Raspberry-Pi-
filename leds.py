import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)  # LED Rojo
GPIO.setup(6, GPIO.OUT)  # LED Verde
GPIO.setup(13, GPIO.OUT) # LED Azul
GPIO.setup(16, GPIO.IN)  # Receptor IR

def set_status_led(self, status):
    GPIO.output(5, status == "error")
    GPIO.output(6, status == "ok")
    GPIO.output(13, status == "effect")

def check_ir(self):
    if GPIO.input(16):
        self.color_chase()  # Ejemplo de acción