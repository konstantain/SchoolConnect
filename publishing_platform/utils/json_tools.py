from typing import Optional, Callable, Any

import orjson

__all__ = [
    "retrieve_array_from_json",
    "orjson_dumps",
    "orjson_dumps_bytes",
    "orjson_loads",
]


def retrieve_array_from_json(input_json: dict):
    for key, value in input_json.items():
        if isinstance(value, list):
            return value
    return [input_json]


def orjson_dumps(
    __obj: Any, default: Optional[Callable[[Any], Any]] = None, option: Optional[int] = orjson.OPT_NON_STR_KEYS  # noqa
) -> str:
    """orjson.dumps returns bytes, to match standard json.dumps we need to decode;
    option orjson.OPT_NON_STR_KEYS is enabled by default, to disable set option=None"""

    return orjson.dumps(__obj, default=default, option=option).decode()  # noqa


orjson_dumps = orjson_dumps  # FROM py objects TO str
orjson_dumps_bytes = orjson.dumps  # FROM py objects TO bytes
orjson_loads = orjson.loads  # FROM str/bytes  TO py objects
