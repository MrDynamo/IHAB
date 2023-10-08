# Build directories

from pathlib import Path

class AppDirectories:
    
    def __init_(self, data_dir: Path) -> None:
        self.DATA_DIR = data_dir
