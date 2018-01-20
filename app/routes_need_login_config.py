"""
The file is used to configure the routes that user need to be logged.
Format:
(route rule, (list of methods that need login))
"""

routes = [
    ('/auth/user/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/auth/user/', ('GET')),
    ('/auth/login/', ('DELETE')),
    ('/event/', ('POST')),
    ('/event/<int:id>', ('PUT', 'DELETE')),
    ('/event/type/', ('POST', 'GET')),
    ('/event/type/<int:id>', ('GET', 'PUT', 'DELETE')),
    ('/auth/user/resetpassword/', ('PUT'))
]
