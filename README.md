# Portfolio Website

## PythonAnywhere deployment

1. Create a **Manual configuration** web app and a virtual environment using the same Python version.
2. Clone/upload this repository, activate the virtual environment, then run:

   ```bash
   pip install -r requirement.txt
   cd ~/portfolio_website
   python manage.py migrate
   python manage.py collectstatic --noinput
   ```

3. In the WSGI file linked from PythonAnywhere's **Web** tab, set your project path and the environment variables below. Replace every placeholder before saving:

   ```python
   import os
   import sys

   project_path = '/home/YOUR_USERNAME/portfolio_website'
   if project_path not in sys.path:
       sys.path.insert(0, project_path)

   os.environ['DJANGO_SETTINGS_MODULE'] = 'portfolio.settings'
   os.environ['DJANGO_DEBUG'] = 'False'
   os.environ['DJANGO_SECRET_KEY'] = 'GENERATE_A_LONG_RANDOM_SECRET'
   os.environ['DJANGO_ALLOWED_HOSTS'] = 'YOUR_USERNAME.pythonanywhere.com'
   os.environ['DJANGO_CSRF_TRUSTED_ORIGINS'] = 'https://YOUR_USERNAME.pythonanywhere.com'

   from django.core.wsgi import get_wsgi_application
   application = get_wsgi_application()
   ```

4. In the **Web** tab's Static files section, map `/static/` to:

   ```text
   /home/YOUR_USERNAME/portfolio_website/staticfiles
   ```

5. Reload the web app. Whenever static files change, rerun `collectstatic --noinput` and reload.
