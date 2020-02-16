PROJECT_DIR  = "C:\\Users\\Sahana Upadhya\\TreeHacks\\Treehacks\\mysite\treehacks"

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(PROJECT_DIR,'static')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(PROJECT_DIR,'media')


STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(PROJECT_DIR, 'static')

)