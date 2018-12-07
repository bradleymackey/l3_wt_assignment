"""
manages the handling of the dataset, including auto-updating
"""

DATASET_LOCATION = "http://files.grouplens.org/datasets/movielens/ml-latest-small.zip"

import pandas as pd
import numpy as np
import requests
import zipfile
import io
import time

def update_dataset():
    """
    updates the dataset files
    """
    r = requests.get(DATASET_LOCATION, stream=True)
    if r.ok:
        z = zipfile.ZipFile(io.BytesIO(r.content))
        z.extractall()
        print("dataset updated at: {:.1f}".format(time.time()))
    else:
        print("network error - could not update dataset")


update_dataset()

# ratings_data = pd.read_csv("ml-latest-small/ratings.csv")
# data_top = ratings_data.head(450)
# print(data_top)