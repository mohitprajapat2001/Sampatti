from settings.base import *  # noqa
from settings.conf import INSTALLED_APPS, MIDDLEWARE, env


INSTALLED_APPS += ["storages", "whitenoise.runserver_nostatic"]
MIDDLEWARE += ["whitenoise.middleware.WhiteNoiseMiddleware"]
DEBUG = True
ALLOWED_HOSTS = [
    "52.66.181.105",
    "halydeals.com",
    "www.halydeals.com",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://192.168.0.31:3000",
    "https://meri-rail-web.vercel.app",
    "https://meri-rail-web-git-develop-mohit-trootechs-projects.vercel.app",
]
CORS_ALLOW_CREDENTIALS = True

# AWS S3 Configurations
STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3.S3Storage",
    },
    "staticfiles": {
        "BACKEND": "meri_rail.settings.storage.StaticStorage",
        "OPTIONS": {
            "location": "static",
            "file_overwrite": False,
        },
    },
    "media": {
        "BACKEND": "meri_rail.settings.storage.MediaStorage",
        "OPTIONS": {
            "location": "media",
            "file_overwrite": False,
        },
    },
}
AWS_ACCESS_KEY_ID = env.get("AWS_S3_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = env.get("AWS_S3_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "merirail"
AWS_S3_SIGNATURE_VERSION = "s3v4"
AWS_S3_SIGNATURE_NAME = "s3v4"
AWS_S3_REGION_NAME = "ap-south-1"
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_VERIFY = True
AWS_S3_ADDRESSING_STYLE = "auto"

AWS_S3_CUSTOM_DOMAIN = f"{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com"

STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/static/"
MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}/media/"
AWS_S3_SECURE_URLS = True
