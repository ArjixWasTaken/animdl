import importlib
import pathlib

EXEMPT = [
    '__init__.py',
    '__pycache__'
]

try:
    __this_path__ = pathlib.Path(__path__[0])
except:
    __this_path__ = pathlib.Path()

def iter_extractors(*, exempt=EXEMPT):
    for path in __this_path__.glob('*/'):
        if path.name not in exempt:
            yield importlib.import_module('.{.name}'.format(path), package=__name__), path.name
