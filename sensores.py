import Adafruit_DHT
def read_sensor(self):
    sensor = Adafruit_DHT.DHT22
    pin = 4  # GPIO4 como ejemplo
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    # Mostrar en la GUI