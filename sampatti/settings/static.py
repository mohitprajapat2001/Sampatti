from utils.constants import Settings
from settings.conf import BASE_DIR
from os.path import join

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
# -------------------------------------------------
STATIC_URL = Settings.STATIC_URL
STATICFILES_DIRS = [join(BASE_DIR, Settings.STATIC_FILES_DIRS)]
STATIC_ROOT = join(BASE_DIR, Settings.STATIC_ROOT)

# Media files (Models File)
# -------------------------------------------------
MEDIA_URL = Settings.MEDIA_URL
MEDIA_ROOT = join(BASE_DIR, Settings.MEDIA_ROOT)
