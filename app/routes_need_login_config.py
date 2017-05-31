routes = [
    ('/auth/user/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/auth/user/', ('GET')),
    ('/auth/login/', ('DELETE')),
    ('/event/', ('POST', 'GET')),
    ('/event/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/event/type/', ('POST', 'GET')),
    ('/event/type/<int:id>', ('GET', 'PUT', 'DELETE')),
]

