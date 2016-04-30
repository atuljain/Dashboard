DEBUG = True

TEMPLATE_DEBUG = True


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',  # Database Name
        'USER': '',  # Database server username
        'PASSWORD': '',  # Database server password
        'HOST': 'localhost',
        'PORT': '5432',
        'OPTIONS': {
            'autocommit': True,
        }
    }
}

