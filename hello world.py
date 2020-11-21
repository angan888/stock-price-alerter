import time as time
import matplotlib.pyplot as plt

import datetime
import pandas as pd
import numpy as np

data = pd.read_csv("wayfair-price-history.csv")

print(data.columns)
print(data.describe)

print(data['CAN-PICO-DESC'])
