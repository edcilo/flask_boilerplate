from ms.helpers import time
from ms.serializers import Serializer


class <CLASSNAME>(Serializer):
    response = {
        "id": str,
        "created_at": time.datetime_to_epoch,
    }
