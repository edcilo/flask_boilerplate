import os
from pathlib import Path


configuration = {
    "default": os.getenv("DB_CONNECTION", "sqlite"),

    "connections": {

        "sqlite": {
            "database": os.path.join(Path(__file__).parents[2], os.getenv("DB_DATABASE", "database.sqlite"))
        },

        "psql": {
            "host": os.getenv('DB_HOST'),
            "port": os.getenv('DB_PORT'),
            "database": os.getenv('DB_DATABASE'),
            "username": os.getenv('DB_USER'),
            "password": os.getenv('DB_PASSWORD')
        }

    }
}


def db_connection(db_config):
    engine = db_config.get("default")

    if not engine in db_config.get("connections", {}):
        raise Exception("The database engine does not exist")

    config = db_config.get("connections", {}).get(engine, {})
    connection = None

    if engine == "sqlite":
        connection = f"sqlite:///{config['database']}"
    elif engine == "psql":
        connection = f"postgresql://{config['username']}:{config['password']}@{config['host']}:{config['port']}/{config['database']}"

    return {
        "SQLALCHEMY_DATABASE_URI": connection,
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    }


db_config = db_connection(configuration)
