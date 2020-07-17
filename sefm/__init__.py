from sefm.backends.database import scraper

# A hardcoded __all__ variable is necessary to appease
# `mypy --strict` running in projects that import xarray.
__all__ = (
    # Top-level functions
    "create_db",
)
