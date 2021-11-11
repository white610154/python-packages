import json
from service.Config import Config


if __name__ == "__main__":
    with open("config.json", "r") as fin:
        config: Config = Config.from_json(json.load(fin))
        print(config)