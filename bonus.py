import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

score_df = pd.read_csv('data.csv')
score_df.head()
score_df.describe()