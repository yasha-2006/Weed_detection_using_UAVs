"""Root entry point for AgriSight AI Weed Detection Dashboard.
Allows running `python app.py` directly from the repository root directory.
"""
import os
import sys
import runpy
from pathlib import Path

INNER_DIR = Path(__file__).resolve().parent / "weed_detection-main"
if not INNER_DIR.is_dir():
    raise RuntimeError(f"Inner project directory not found at {INNER_DIR}")

# Change working directory and add to sys.path
os.chdir(INNER_DIR)
if str(INNER_DIR) not in sys.path:
    sys.path.insert(0, str(INNER_DIR))

# Execute the inner app.py as __main__
app_script = INNER_DIR / "app.py"
runpy.run_path(str(app_script), run_name="__main__")
