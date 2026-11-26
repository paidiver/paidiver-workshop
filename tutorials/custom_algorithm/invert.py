"""Custom Paidiverpy algorithm that inverts an image."""

import numpy as np
from paidiverpy.custom_layer import CustomLayer
from paidiverpy.models.custom_params import CustomParams


class InvertColour(CustomLayer):
    """Invert the intensity of every pixel in an image."""

    @staticmethod
    def invert(image_data: np.ndarray, params: CustomParams | None = None, **_kwargs: dict) -> np.ndarray:
        """Return an intensity-inverted copy of ``image_data``."""
        del params
        max_value = np.iinfo(image_data.dtype).max
        return max_value - image_data
