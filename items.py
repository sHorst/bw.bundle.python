
pkg_apt = {
    'python3': {
        "installed": True,
    },
    'python3-dev': {
        "installed": True,
    },
    'python3-pip': {
        "installed": True,
    },
}

symlinks = {
    '/usr/bin/pip': {
        "target": '/usr/bin/pip3',
        "group": "root",
        "owner": "root",
    }
}
