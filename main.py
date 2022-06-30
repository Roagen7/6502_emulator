import json
from Bus import Bus
from time import time, sleep


config_file = "config.json"


with open(config_file, 'r') as f:
    config = json.loads(f.read())

bus = Bus(debug=config["debug"])

bus.load_file("a.out")

while 1:
    start = time()
    bus.cpu.tick()
    end = time()
    elapsed = end - start

    assert elapsed < 1/config["tps"]

    sleep(1/config["tps"] - elapsed)
