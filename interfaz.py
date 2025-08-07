from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout, QSlider, QPushButton
import sys

class DMXController(QWidget):
    def __init__(self):
        super().__init__()
        self.dmx = DMXSender()
        self.init_ui()
        self.dmx.start()

    def init_ui(self):
        self.setWindowTitle("Controlador DMX Avanzado")
        layout = QVBoxLayout()
        tabs = QTabWidget()

        # Pestaña Control Manual
        self.manual_tab = QWidget()
        self.setup_manual_tab()
        tabs.addTab(self.manual_tab, "Control Manual")

        # Pestaña Colores (implementar similarmente)
        # Pestaña Efectos (implementar similarmente)
        # Pestaña Vista/Sensor (implementar similarmente)
        # Pestaña Configuración (implementar similarmente)

        layout.addWidget(tabs)
        self.setLayout(layout)

    def setup_manual_tab(self):
        layout = QVBoxLayout()
        self.sliders = []
        for i in range(14):  # Ejemplo para 14 canales
            slider = QSlider()
            slider.setRange(0, 255)
            slider.valueChanged.connect(lambda v, ch=i: self.dmx.set_channel(ch, v))
            self.sliders.append(slider)
            layout.addWidget(slider)
        self.manual_tab.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = DMXController()
    window.show()
    sys.exit(app.exec_())
    