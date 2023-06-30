
pkg_pip = {}

for pkg, config in node.metadata.get('python', {}).get('packages', {}).items():
    if pkg not in pkg_pip.keys():
        # TODO: add dependency for update apt_cache
        pkg_pip[pkg] = config

if node.os == 'debian':
    # starting debian 12 /usr/bin/pip is python3
    if node.os_version[0] < 12:
        symlinks = {
            '/usr/bin/pip': {
                "target": '/usr/bin/pip3',
                "group": "root",
                "owner": "root",
            }
        }
