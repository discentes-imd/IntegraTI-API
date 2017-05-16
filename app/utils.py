from flask_restplus import abort


def update_object(obj, dictio):
    """ Update a object based on a dictionary  """
    for attr, value in dictio.items():
        setattr(obj, str(attr), value)


def abort_if_none(item, code, msg):
    """ Abort if item is none """
    if item is None:
        abort(code, msg)


def msg(text, key='msg'):
    """ Returns a Json message with text"""
    return {key: text}
