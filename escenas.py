import json
def save_scene(self, filename="scene.json"):
    with open(filename, "w") as f:
        json.dump(self.dmx.dmx_data, f)

def load_scene(self, filename="scene.json"):
    with open(filename, "r") as f:
        self.dmx.dmx_data = json.load(f)