from json import load
from LogFile import LogFile


class Config:
    def __init__(self, config_path):
        with open(config_path) as config_file:
            config = load(config_file)
            self.config = map(lambda x: LogFile(x), config)


