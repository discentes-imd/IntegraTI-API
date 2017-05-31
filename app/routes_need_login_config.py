routes = [
    ('/auth/user/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/auth/user/', ('GET', 'POST')),
    ('/auth/login/', ('DELETE'))
]

