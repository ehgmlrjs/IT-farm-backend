import re
import pandas as pd
from konlpy.tag import Okt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

import os
import django
import sys
from pathlib import Path

current_path = Path(__file__).resolve()
project_root =current_path.parent.parent

sys.path.append(str(project_root))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "first_app.settings")
os.environ["DJANGO_ALLOWS_ASYNC_UNSAFE"] = "true"
django.setup()

from order.models import Review

okt = Okt()

# 텍스트를 형태소 단위로 나눔
def tokenize(text):
    return okt.morphs(text)

# 한글과 공백을 제외하고 모두 제거
def preprocess_text(text):
    text = re.sub("[^가-힣\s]", "", text)
    return text

# 데이터 로드
data = pd.read_csv('./files/train_data.csv')
target = data['label']
feature = data['content']

# 데이터 전처리
feature_preprocessed = feature.apply(preprocess_text)

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(feature_preprocessed, target, test_size=0.3, random_state=42)

# 모델 학습
optimized_pipeline = Pipeline([
    ('tfidf_vect', TfidfVectorizer(ngram_range=(1, 2))),
    ('lr_clf', LogisticRegression(C=100, penalty='l2'))
])

optimized_pipeline.fit(X_train, y_train)

# 모델 저장
import joblib

joblib.dump(optimized_pipeline, './files/review_model.joblib')