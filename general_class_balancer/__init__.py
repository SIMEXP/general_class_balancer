__packagename__ = "general_class_balancer"
__copyright__ = "2024, mleming"

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "unknown"
finally:
    del version, PackageNotFoundError

__all__ = [
    "__copyright__",
    "__packagename__",
    "__version__",
]
