import functools
import json


def jsonify(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return json.dumps(func(*args, **kwargs))

    return wrapper


@jsonify
def make_user(id, live, options):
    return {"id": id, "live": live, "options": options}


print(make_user(4, False, None))
