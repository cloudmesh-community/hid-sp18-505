"""
Domain models.
"""

raingages = {
    'schema': {
        'code': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'latitude': {

        },
        'longitude': {

        }
    }
}

precip_events = {
    'schema': {
    }
}

DOMAIN = {
    'raingages': raingages,
    'precip_events': precip_events,
}