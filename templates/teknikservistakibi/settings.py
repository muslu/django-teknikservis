# -*- coding: utf-8 -*-
import os

# Projenin bulunduğu klasöre ulaşmak için değişken
BASE_DIR                        = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Hataların ekrana yansıtılması
DEBUG                           = True

#Çalışılacak domain isimler listesi
ALLOWED_HOSTS                       = ['192.168.2.168', '127.0.0.1']

# Veritabanı seçimi, ayarları
DATABASES                           = {
                                        'default': {
                                            'ENGINE': 'django.db.backends.sqlite3',
                                            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                                        }
                                    }


#Kurulu uygulamalar. Yazdığımız uygulamaların listesi. Öncelik sırası var.
INSTALLED_APPS              = [
                                    'django.contrib.admin',
                                    'django.contrib.auth',
                                    'django.contrib.contenttypes',
                                    'django.contrib.sessions',
                                    'django.contrib.messages',
                                    'django.contrib.staticfiles',
                                    'servisformu'
                                ]

# Tüm projede geçerli olacak kodlar. Sıralamaya göre öncelik middleware lerdedi.
MIDDLEWARE_CLASSES              = [
                                        'django.middleware.security.SecurityMiddleware',
                                        'django.contrib.sessions.middleware.SessionMiddleware',
                                        'django.middleware.common.CommonMiddleware',
                                        'django.middleware.csrf.CsrfViewMiddleware',
                                        'django.contrib.auth.middleware.AuthenticationMiddleware',
                                        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
                                        'django.contrib.messages.middleware.MessageMiddleware',
                                        'django.middleware.clickjacking.XFrameOptionsMiddleware',
                                    ]

# urls.py dosyası
ROOT_URLCONF                    = 'teknikservistakibi.urls'

# Html dosyaları içinde gönderilecek veriler, ayarlar vs..
TEMPLATES                       = [
                                    {
                                        'BACKEND': 'django.template.backends.django.DjangoTemplates',
                                        'DIRS': [os.path.join(BASE_DIR, 'templates')],
                                        'APP_DIRS': True,
                                        'OPTIONS': {
                                            'context_processors': [
                                                'django.template.context_processors.debug',
                                                'django.template.context_processors.request',
                                                'django.contrib.auth.context_processors.auth',
                                                'django.contrib.messages.context_processors.messages',
                                            ],
                                        },
                                    },
                                ]

# Http serverlar için wsgi dosya adı ve uygulaması
WSGI_APPLICATION                = 'teknikservistakibi.wsgi.application'




# Yetkilerde geçerli olan şifreleme yöntemleri
AUTH_PASSWORD_VALIDATORS        = [
                                {
                                    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
                                },
                                {
                                    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
                                },
                                # {
                                #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
                                # },
                                # {
                                #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
                                # },
                            ]


# Uluslararasılaşma
# https://docs.djangoproject.com/en/1.9/topics/i18n/
LANGUAGE_CODE               = 'tr_TR'
TIME_ZONE                   = 'Europe/Istanbul'
USE_I18N                    = True
USE_L10N                    = True
USE_TZ                      = True


# Statik dosyaları (CSS, JavaScript, Resimler)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
MEDIA_ROOT                                      =       BASE_DIR + '/media/'
MEDIA_URL                                       =       '/media/'

STATIC_ROOT                                     =       BASE_DIR + "/static/"
STATIC_URL                                      =       '/static/'


# Gizli kod. İleride gerekecek.
SECRET_KEY                  = '9f5$6e&r&x3*_a%j1ocv*p3aftgkl1y5n&)+^jehhc@&z%@@8p'


