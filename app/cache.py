current_user = None # null user, need exist on database
blacklisted_tokens = []

def get_current_user():
    return current_user