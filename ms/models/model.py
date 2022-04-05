from flask_sqlalchemy import Model as BaseModel


class Model(BaseModel):
    _fillable = list()

    def setAttrs(self, data):
        for attr, value in data.items():
            if attr in self._fillable:
                setattr(self, attr, value)

    def udpate(self, data):
        self.setAttrs(data)
