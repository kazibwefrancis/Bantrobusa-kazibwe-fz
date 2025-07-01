"""
Utility functions for the X Posting Agent
"""

import logging
import json
from datetime import datetime
from typing import Dict, Any, List, Optional


def setup_logging(config: Dict[str, Any]) -> None:
    """Setup logging configuration"""
    logging.basicConfig(
        level=getattr(logging, config.get('level', 'INFO')),
        format=config.get('format', '%(asctime)s - %(levelname)s - %(message)s'),
        handlers=[
            logging.FileHandler(config.get('filename', 'app.log')),
            logging.StreamHandler()
        ]
    )


def validate_tweet_content(content: str, max_length: int = 280) -> bool:
    """
    Validate tweet content
    
    Args:
        content: Tweet content to validate
        max_length: Maximum allowed length
        
    Returns:
        bool: True if valid, False otherwise
    """
    if not content or not isinstance(content, str):
        return False
    
    if len(content.strip()) == 0:
        return False
    
    if len(content) > max_length:
        return False
    
    return True


def truncate_content(content: str, max_length: int = 280, suffix: str = "...") -> str:
    """
    Truncate content to fit within character limit
    
    Args:
        content: Content to truncate
        max_length: Maximum allowed length
        suffix: Suffix to add when truncating
        
    Returns:
        str: Truncated content
    """
    if len(content) <= max_length:
        return content
    
    # Account for suffix length
    max_content_length = max_length - len(suffix)
    
    # Truncate at word boundary if possible
    truncated = content[:max_content_length]
    last_space = truncated.rfind(' ')
    
    if last_space > max_content_length * 0.8:  # If we can keep 80% of content
        truncated = truncated[:last_space]
    
    return truncated + suffix


def load_content_from_file(file_path: str) -> List[str]:
    """
    Load content from a text file (one item per line)
    
    Args:
        file_path: Path to the content file
        
    Returns:
        List[str]: List of content items
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = [line.strip() for line in f.readlines() if line.strip()]
        return content
    except FileNotFoundError:
        logging.error(f"Content file not found: {file_path}")
        return []
    except Exception as e:
        logging.error(f"Error loading content from file: {str(e)}")
        return []


def save_content_to_file(content: List[str], file_path: str) -> bool:
    """
    Save content to a text file (one item per line)
    
    Args:
        content: List of content items
        file_path: Path to save the content
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            for item in content:
                f.write(f"{item}\n")
        return True
    except Exception as e:
        logging.error(f"Error saving content to file: {str(e)}")
        return False


def format_timestamp(dt: Optional[datetime] = None) -> str:
    """
    Format timestamp for logging
    
    Args:
        dt: Datetime object, uses current time if None
        
    Returns:
        str: Formatted timestamp
    """
    if dt is None:
        dt = datetime.now()
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def load_json_config(file_path: str) -> Dict[str, Any]:
    """
    Load configuration from JSON file
    
    Args:
        file_path: Path to JSON config file
        
    Returns:
        Dict[str, Any]: Configuration dictionary
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error(f"Config file not found: {file_path}")
        return {}
    except json.JSONDecodeError as e:
        logging.error(f"Invalid JSON in config file: {str(e)}")
        return {}
    except Exception as e:
        logging.error(f"Error loading config file: {str(e)}")
        return {}


def save_json_config(config: Dict[str, Any], file_path: str) -> bool:
    """
    Save configuration to JSON file
    
    Args:
        config: Configuration dictionary
        file_path: Path to save the config
        
    Returns:
        bool: True if successful, False otherwise
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, default=str)
        return True
    except Exception as e:
        logging.error(f"Error saving config file: {str(e)}")
        return False


def sanitize_filename(filename: str) -> str:
    """
    Sanitize filename by removing invalid characters
    
    Args:
        filename: Original filename
        
    Returns:
        str: Sanitized filename
    """
    import re
    # Remove invalid characters for Windows/Unix filenames
    sanitized = re.sub(r'[<>:"/\\|?*]', '_', filename)
    return sanitized.strip()


def get_file_extension(filename: str) -> str:
    """
    Get file extension from filename
    
    Args:
        filename: Filename with or without path
        
    Returns:
        str: File extension (without dot)
    """
    import os
    return os.path.splitext(filename)[1].lstrip('.')


def is_image_file(filename: str) -> bool:
    """
    Check if file is an image based on extension
    
    Args:
        filename: Filename to check
        
    Returns:
        bool: True if image file, False otherwise
    """
    image_extensions = {'jpg', 'jpeg', 'png', 'gif', 'webp', 'bmp'}
    extension = get_file_extension(filename).lower()
    return extension in image_extensions


def is_video_file(filename: str) -> bool:
    """
    Check if file is a video based on extension
    
    Args:
        filename: Filename to check
        
    Returns:
        bool: True if video file, False otherwise
    """
    video_extensions = {'mp4', 'avi', 'mov', 'wmv', 'flv', 'webm', 'mkv'}
    extension = get_file_extension(filename).lower()
    return extension in video_extensions
