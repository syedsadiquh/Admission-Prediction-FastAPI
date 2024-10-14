import os
from functools import lru_cache

from keras.api.models import load_model
import numpy as np
from sklearn.preprocessing import MinMaxScaler

class UseModel:
    @lru_cache
    def __init__(self):
        # Loading Saved ml_model
        self.model = load_model('./ml_model/admission_prediction_model.h5')
        # Fitting the MinMaxScaler with the correct min and max values
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.scaler.fit([[290, 92, 1, 1.0, 1.0, 6.8, 0],
                    [340, 120, 5, 5.0, 5.0, 9.92, 1]])

    def predict(self, gre, toefl, university_rating, sop, lor, cgpa, research):
        # Combine inputs into a single array
        user_input = np.array([[gre, toefl, university_rating, sop, lor, cgpa, int(research)]])
        # Scale the input data using the same scaler used during training
        user_input_scaled = self.scaler.transform(user_input)
        prediction = self.model.predict(user_input_scaled)
        return prediction[0][0]
