import os


app_config = {
    "APP_NAME": os.getenv("APP_NAME", "ms"),
    "APP_VERSION": os.getenv("APP_VERSION", "0.0.0")
}
