"""
Makes the fabulous icons from Bootstrap available in to Rio.

See the README for a usage example.
"""

from pathlib import Path
import rio

MODULE_DIR = Path(__file__).parent

rio.Icon.register_icon_set(
    set_name="bootstrap",
    set_archive_path=MODULE_DIR / "bootstrap.tar.xz",
)
