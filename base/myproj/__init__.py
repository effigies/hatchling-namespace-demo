__path__ = __import__("pkgutil").extend_path(__path__, __name__)
try:
    from ._version import __version__
except ImportError:
    __version__ = "0+unknown"
