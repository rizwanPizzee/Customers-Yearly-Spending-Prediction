import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle

df = pd.read_csv('ecommerce.csv')

X = df[['Avg. Session Length', 'Time on App','Time on Website','Length of Membership']]
y = df['Yearly Amount Spent']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=30, random_state=42)

lm = LinearRegression()
lm.fit(X_train, y_train)


pickle.dump(lm, open('model.pkl', 'wb'))