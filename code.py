def walkFile(file):
    rootdir = Path(file)
    return list(rootdir.glob('**/*.nfo'))
