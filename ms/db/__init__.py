from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy, Model as BaseModel
from ms import app


class Model(BaseModel):
    _fillable = list()

    def setAttrs(self, data):
        for attr, value in data.items():
            if attr in self._fillable:
                setattr(self, attr, value)

    def udpate(self, data):
        self.setAttrs(data)


db = SQLAlchemy(app, model_class=Model)
migrate = Migrate(app, db)
