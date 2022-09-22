import os
from pathlib import Path
from django.conf.global_settings import LANGUAGES as DJANGO_LANGUAGES




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd516ocd%_@th3#f!ykw6^$aj7us8fbaek+2^x0fei^_noo1vs$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'admin_interface',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Tatoo',
    'rest_framework',
    'colorfield',
]

X_FRAME_OPTIONS = "SAMEORIGIN"

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'StyleTatto.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'StyleTatto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'styletattopython',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


# MODIFICACIONES DEL ADMIN *IMPORTANTE*

JAZZMIN_SETTINGS = {   

    # título de la ventana (Se establecerá de forma predeterminada en 
    # current_admin_site.site_title si está ausente o Ninguno)
    "site_title": "STYLE TATTO Admin",

    # Título en la pantalla de inicio de sesión (19 caracteres como máximo) 
    # (predeterminado en current_admin_site.site_header si está ausente o Ninguno)
    "site_header": "STYLE TATTO",
    
    "site_brand": "STYLE TATTO",

    #IMG LOGO
    "site_logo":"img/logoStyle.jpg" ,

    # Ruta relativa a un favicon para su sitio, por defecto será site_logo 
    # está ausente (idealmente 32x32 px)
    "site_icon": None,

    # Texto de bienvenida en la pantalla de inicio de sesión
    "welcome_sign": "Bienvenido a STYLE TATTO",

    # Copyright on the footer
    "copyright": "STYLE TATTO",

    # El administrador del modelo para buscar desde la barra de búsqueda, 
    # la barra de búsqueda se omite si se excluye
    "search_model": "auth.User",

    # Nombre de campo en el modelo de usuario que contiene avatar 
    # ImageField/URLField/Charfield o un invocable que recibe al usuario
    "user_avatar": None,

    ############
    # Top Menu #
    ############

    # Enlaces para poner a lo largo del menú superior
    "topmenu_links": [
        
        {"name": "Home Admin",  "url": "admin:index", "permissions": ["auth.view_user"]},

        {"name": "Style Tatto", "url": "http://127.0.0.1:8000/", "new_window": True},

        {"model": "auth.User"},

        {"app": "books"},
    ],


    #############
    # Side Menu #
    #############
    # Ya sea para mostrar el menú lateral
    "show_sidebar": True,

    # Ya sea para aut expandir el menú
    "navigation_expanded": True,

    # Ocultar estas aplicaciones al generar el menú lateral, por ejemplo (autorización)
    "hide_apps": [],

    # Oculte estos modelos al generar el menú lateral (por ejemplo, auth.user)
    "hide_models": [],

    # Lista de aplicaciones (y/o modelos) para el pedido del menú lateral base 
    # (no es necesario que contenga todas las aplicaciones/modelos)
    "order_with_respect_to": ["auth", "books", "books.author", "books.book"],

    # Íconos personalizados para aplicaciones/modelos del menú lateral 
    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.Group": "fas fa-users",
    },
    
    # Iconos que se usan cuando uno no se especifica manualmente
    "default_icon_parents": "fas fa-chevron-circle-right",
    "default_icon_children": "fas fa-circle",

    #################
    # Related Modal #
    #################
    # Use modales en lugar de ventanas emergentes
    "related_modal_active": False,

    #############   
    # UI Tweaks #
    #############
    
    # Si mostrar el personalizador de IU en la barra lateral
    "show_ui_builder": False,

    "changeform_format": "horizontal_tabs",
    # anular los formularios de cambio según el administrador del modelo
    "changeform_format_overrides": {
        "auth.user": "collapsible", 
        "auth.group": "vertical_tabs"
        },

    # Rutas relativas a scripts CSS/JS personalizados 
    "custom_css": "./css/style.css",

    # (deben estar presentes en archivos estáticos) "custom_css": None,
    "custom_js": None,
}    




BASE_DIR = Path(__file__).resolve().parent.parent

# IMPORTANCION DE LA IMG
STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]

