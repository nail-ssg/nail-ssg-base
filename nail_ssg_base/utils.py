from os.path import join, isdir, dirname, abspath, isabs, normpath


def absolute_path(start: str, path: str) -> str:
    if isabs(path):
        return path
    if not isdir(start):
        start = dirname(start)
    return join(abspath(start), normpath(path))
