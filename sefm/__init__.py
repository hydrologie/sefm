from .database.models import create_db
from .database import datascraper

# A hardcoded __all__ variable is necessary to appease
# `mypy --strict` running in projects that import xarray.
__all__ = (
    # Top-level functions
    "create_db",
)
