import numpy as np
import pandas as pd

def image_statistics(img: np.ndarray):
    """Calculate basic statistics of the image."""
    flat = img.flatten()
    series = pd.Series(flat)
    
    stats = {
        'mean': np.mean(img),
        'std': np.std(img),
        'min': np.min(img),
        'max': np.max(img),
        'median': np.median(img)
    }
    return stats