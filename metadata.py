@metadata_processor
def add_apt_packages(metadata):
    # TODO: add support for other package managers as well
    if node.has_bundle("apt"):
        metadata.setdefault('apt', {})
        metadata['apt'].setdefault('packages', {})

        for package in ['python3', 'python3-dev', 'python3-pip', 'python3-setuptools']:
            metadata['apt']['packages'][package] = {'installed': True}

    return metadata, DONE
