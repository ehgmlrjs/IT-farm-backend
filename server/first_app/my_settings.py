#mysettings.py
DATABASES = DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'it_farm',
        'USER': 'admin',
        'PASSWORD': 'mysql123',
        'HOST': 'it-farm.ctfayt3kdbdx.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}

SECRET_KEY = "django-insecure-z112d1h4)cot408pe433pv8x!a#frygjsxslh)ik21a(6qmok@"