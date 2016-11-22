"""
Settings for Eve API
"""

XML=False
RESOURCE_METHODS = ['GET', 'POST']
ITEM_METHODS = ['GET', 'DELETE', 'PATCH']
URL_PREFIX = "api"
SERVER_NAME = None

DOMAIN = {
    'users': {
        'schema': {
            'username': {
                'type': 'string',
                'minlength': 4,
                'maxlength': 15,
                'required': True,
                'unique': True
            },
            'role': {
                'type': 'list',
                'allowed': ["viewer", "creator"]
            }
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'username'
        }
    },
    'clients': {
        'schema': {
            'name': {
                'type': 'string',
                'minlength': 5,
                'maxlength': 15,
                'required': True
            }
        },
        'additional_lookup': {
            'url': 'regex("[\w\s]+")',
            'field': 'name'
        }
    },
    'products': {
        'schema': {
            'name': {
                'type': 'string',
                'maxlength': 15
            }
        },
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'name'
        }
    },
    'requests': {
        'schema': {
            'title': {
                'type': 'string',
                'required': True
            },
            'description': {
                'type': 'string',
                'required': True
            },
            'client': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'clients',
                    'embeddable': True
                }
            },
            'priority': {
                'type': 'integer'
            },
            'open_date': {
                'type': 'datetime'
            },
            'target_date': {
                'type': 'datetime'
            },
            'request_url': {
                'type': 'string'
            },
            'status': {
                'type': 'list',
                'allowed': ["open", "closed"]
            },
            'product_areas': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'products',
                    'embeddable': True
                }
            }
        }
    }
}
