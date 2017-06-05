from flask_restplus import abort


def fill_object(obj, dictio):
    """ Update a object based on a dictionary
    :param obj: object
    :param dictio: dict
    """
    for attr, value in dictio.items():
        setattr(obj, str(attr), value)


def abort_if_none(item, code, msg):
    """ Abort if item is none
    :param item: object
    :param code: int
    :param msg: str
    """
    if item is None:
        abort(code, msg)


def msg(text, key='messsage'):
    """ Returns a Json message with text
    :param text: str
    :param key: str
    """
    return {key: text}
