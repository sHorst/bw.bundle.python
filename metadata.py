defaults = {}

if node.has_bundle("apt"):
    defaults['apt'] = {
        'packages': {
            'python3': {'installed': True},
            'python3-dev': {'installed': True},
            'python3-pip': {'installed': True},
            'python3-setuptools': {'installed': True},
        }
    }
