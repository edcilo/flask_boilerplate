import json
from redis import Redis
from ms import app
from ms.helpers.time import epoch_now


class Cache:
    def __init__(self):
        self.config = app.config.get("REDIS", dict())
        self.conn = self.connection()

    def connection(self):
        return Redis(
            host=self.config.get("HOST"),
            port=self.config.get("PORT"),
            username=self.config.get("USERNAME"),
            password=self.config.get("PASSWORD"),
            db=self.config.get("DATABASE")
        )

    def set(self, key, value):
        data = json.dumps({
            "data": value,
            "key": key,
            "created_at": epoch_now()
        })
        return self.conn.set(key, data)

    def get(self, key):
        data = self.get_raw(key)
        return data.get("data")

    def get_raw(self, key):
        data = self.conn.get(key)
        data = json.loads(data)
        return data

    def exists(self, key):
        return self.conn.exists(key)