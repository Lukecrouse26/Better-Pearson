import sys
import shutil
from pathlib import Path

SUPPORTED_FORMATS = ['jpg', 'jpeg', 'png']

def upload_image(source_path: str, dest_dir: str = "uploads") -> Path:
    source = Path(source_path)
    if not source.exists():
        raise FileNotFoundError(f"The file {source} does not exist.")
    
    if source.suffix[1:].lower() not in SUPPORTED_FORMATS:
        raise ValueError(f"Unsupported file format: {source.suffix}. Supported formats are: {SUPPORTED_FORMATS}")
    
    dest_directory = Path(dest_dir)
    dest_directory.mkdir(parents=True, exist_ok=True)
    
    dest_path = dest_directory / source.name
    shutil.copy(source, dest_path)
    
    return dest_path