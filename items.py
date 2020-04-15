
pkg_pip = {}

for pkg, config in node.metadata.get('python', {}).get('packages', {}).items():
    if pkg not in pkg_pip.keys():
        # TODO: add dependency for update apt_cache
        pkg_pip[pkg] = config

symlinks = {
    '/usr/bin/pip': {
        "target": '/usr/bin/pip3',
        "group": "root",
        "owner": "root",
    }
}
