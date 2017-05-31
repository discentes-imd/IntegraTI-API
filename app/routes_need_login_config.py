routes = [
    ('/auth/user/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/auth/user/', ('GET')),
    ('/auth/login/', ('DELETE')),
    ('/event/', ('POST', 'GET'))
]

