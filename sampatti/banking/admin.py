from utils.utils import get_model
from utils.constants import AppModel
from django.contrib import admin


admin.site.register(get_model(**AppModel.BANK))
admin.site.register(get_model(**AppModel.BRANCH))
