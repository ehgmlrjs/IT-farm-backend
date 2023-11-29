import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from tensorflow import keras
from keras.models import Sequential
from keras.layers import LSTM, Dense, Dropout
from keras.optimizers import Adam

import pandas as pd

import joblib

data = pd.read_csv('./files/1.csv')
data.fillna(data.median(), inplace=True)

X = data.drop(['all_product'], axis=1)
y = data['all_product']

scaler_X = MinMaxScaler()
scaler_y = MinMaxScaler()

X_scaled = scaler_X.fit_transform(X)
y_scaled = scaler_y.fit_transform(y.values.reshape(-1, 1))

# 훈련 데이터와 테스트 데이터 분리
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_scaled, test_size=0.2, random_state=42)

# LSTM에 입력하기 위한 차원 변경
X_train = X_train.reshape((X_train.shape[0], 1, X_train.shape[1]))
X_test = X_test.reshape((X_test.shape[0], 1, X_test.shape[1]))

model = Sequential()
model.add(LSTM(50, return_sequences=True, input_shape=(X_train.shape[1], X_train.shape[2])))
model.add(Dropout(0.01))
model.add(LSTM(50, return_sequences=True))  # LSTM 층 추가 (return_sequences=True로 설정)
model.add(Dropout(0.01))
model.add(LSTM(50, return_sequences=False))  # LSTM 층 추가 (return_sequences=False로 설정)
model.add(Dropout(0.01))
model.add(Dense(64))  # Dense 층 추가
model.add(Dense(1))  # 추가한 Dense 층

# 모델 컴파일
model.compile(optimizer=Adam(learning_rate=0.001), loss='mean_squared_error')

# 모델 학습
history = model.fit(X_train, y_train, epochs=20, batch_size=10, validation_data=(X_test, y_test), verbose=1)

# joblib.dump(model, './files/output_model.joblib')
model.save('./files/output_model.h5')
joblib.dump(scaler_X, './files/scaler_X.joblib')
joblib.dump(scaler_y, './files/scaler_y.joblib')