def color_chase(self):
    def run_effect():
        colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]  # RGB
        while getattr(self, "chase_running", False):
            for color in colors:
                for head in range(4):  # 4 cabezas como ejemplo
                    start = head * 14  # 14 canales por cabeza
                    self.dmx.set_channel(start + 1, color[0])  # R
                    self.dmx.set_channel(start + 2, color[1])  # G
                    self.dmx.set_channel(start + 3, color[2])  # B
                time.sleep(0.5)
    self.chase_running = True
    threading.Thread(target=run_effect).start()

def stop_chase(self):
    self.chase_running = False