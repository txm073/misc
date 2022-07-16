import json


class Config:
    
    _data = {}

    def __init__(self, **kwargs):
        self._data.update(**kwargs)

    def __getattribute__(self, attr):
        # if attr in self._data:
        #     return self._data[attr]
        return object.__getattribute__(self, attr)

    def __getitem__(self, attr):
        return self.data[attr]

    def __setitem__(self, attr, value):
        self.data[attr] = value

    def save(self):
        with open("data.json", "w") as f:
            json.dump(self.__dict__, f, encoding="utf-8", indent=4)


c = Config()
c.setup_complete = True
c.save()