import interfaz
import efectos
import sensores
import escenas
import leds
import Max
import scrip

if __name__ == "__main__":
    # Iniciar la interfaz gráfica, por ejemplo
    app = interfaz.iniciar_gui()
    # Configurar otros componentes
    sensores.iniciar_lectura()
    efectos.aplicar_efecto()
    # ... etc.