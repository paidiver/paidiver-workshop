"""This is an example of a custom algorithm that scales the image data using MinMaxScaler from sklearn.preprocessing."""

import numpy as np
from paidiverpy.custom_layer.base_custom_algorithm import BaseCustomAlgorithm


class InvertColour(BaseCustomAlgorithm):
    def process(self):
        max_value = np.iinfo(self.image_data.dtype).max
        inverted_array = max_value - self.image_data

        return inverted_array
