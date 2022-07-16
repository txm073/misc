from dataclasses import dataclass
from typing import Tuple, Optional, List
from collections.abc import Iterable
from pprint import pprint


@dataclass
class Url:
    protocol: str
    server: str
    path: str


@dataclass
class User:
    username: str
    uid: str
    url: Url
    friends: Tuple


_default_attribute = type("DefaultAttribute", (), {})

def as_json(obj, fields=None, rlevel=0):
    # Special types
    if isinstance(obj, (set, tuple)):
        obj = list(obj)
    if isinstance(obj, dict):
        for key, value in obj.items():
            obj[key] = as_json(value, fields=fields if not rlevel else None, rlevel=rlevel + 1)    
    elif isinstance(obj, list):
        for i in range(len(obj)):
            obj[i] = as_json(obj[i], fields=fields if not rlevel else None, rlevel=rlevel + 1)
    if not hasattr(obj, "__dict__"):
        return obj

    result = {}
    if fields is None:
        fields = obj.__dict__.items()
    else:
        values = []
        for f in fields:
            val = getattr(obj, f, _default_attribute())
            if isinstance(val, _default_attribute): # attribute does not exist
                continue
            values.append(val)
        fields = zip(fields, values)
    for key, val in fields:
        if key.startswith("_") or callable(val):
            continue
        result[key] = as_json(val, rlevel=rlevel + 1)
    return result


bob = User("bob123", "130818", Url("https", "google", "/"), ())
alice = User("alice123", "123123", Url("https", "youtube", "/c"), (bob))
result = [alice, bob]
d = as_json(result, fields=["uid", "username"])
pprint(d)
#d = as_json(alice, ["friends", "uid", "invalid_field"])

def fn() -> List[str, List[int]]:
    pass