import os
from box.exceptions import BoxValueError
import yaml
from textSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import any

@ensure_annotations
def read_yaml(path_to_yaml:Path) -> ConfigBox:
    """ reads yaml file and returns
    Args:
        path_to_yaml(str):path like input
    Raises:
        ConfigBox: ConfigBox type
    """
try:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
        logger.info(f'yaml_file: {path_to_yaml} loaded successfully')
        return ConfigBox(content)
except BoxValueError:
    raise ValueError("yaml file is empty")
except exception as e:
    raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True)
    """Create list of directories 
    Args: path_to_directories (list): list of path to directories
    ignore_log (bool, optional): ignore if multiple directories are created.  Default to False.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at {path}")

@nsure_annotations
def get_size(path:Path)->str:
    """get size in KBs
    Args:(path) of the file
    returns:
        str: size in KBs
    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f" ~ {size_in_kb} KB"
    




