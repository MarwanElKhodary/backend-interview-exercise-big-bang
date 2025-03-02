import sys
import os
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

if os.path.exists(os.path.join(os.path.dirname(__file__), '..', 'src')):
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))