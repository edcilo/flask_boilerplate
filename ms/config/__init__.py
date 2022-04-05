from dotenv import load_dotenv
from ms import app
from .appConfig import app_config
from .dbConfig import db_config


load_dotenv()


app.config.update(**app_config)
app.config.update(**db_config)
