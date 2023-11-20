import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

dataset = pd.read_csv('./files/output.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

y = y.reshape(-1,1)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
X = imputer.fit_transform(X)

sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

regressor = RandomForestRegressor(n_estimators = 100, random_state = 42, max_depth=35, max_features=1.0, n_jobs=-1)
regressor.fit(X_train, y_train.ravel())

# 모델 저장
import joblib
joblib.dump(regressor, './files/output_model.joblib')
joblib.dump(sc_X, './files/sc_X.joblib')
joblib.dump(sc_y, './files/sc_y.joblib')