def update_object(obj, dictio):
    """ Update a object based on a dictionary  """
    for attr, value in dictio.items():
        setattr(obj, str(attr), value)
