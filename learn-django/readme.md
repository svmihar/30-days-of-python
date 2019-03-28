# django from The ultimate web development bootcamp 


## chapter 1: python refresher 
- nothing special about self, bisa dinamakan apapun tapi perlu karena menjadi pointer dari def-nya 

## chapter 2: wordcout
### starting django
- **django-admin**: ini buat seluruh command yang ada tinggal tambah `--help`
- **create new project**: django-admin startproject {INSERT_NAME_HERE}
    ```python 
    {INSERT_NAME_HERE}/
        manage.py
        {INSERT_NAME_HERE}/
            __init__.py
            settings.py
            urls.py
            wsgi.py
    ```
    - The outer mysite/ root directory is just a container for your project. Its name doesn’t matter to Django; you can rename it to anything you like.
    - manage.py: A command-line utility that lets you interact with this Django project in various ways. You can read all the details about manage.py in django-admin and manage.py.
    - The inner mysite/ directory is the actual Python package for your project. Its name is the Python package name you’ll need to use to import anything inside it (e.g. mysite.urls).
    - mysite/__init__.py: An empty file that tells Python that this directory should be considered a Python package. If you’re a Python beginner, read more about packages in the official Python docs.
    - mysite/settings.py: Settings/configuration for this Django project. Django settings will tell you all about how settings work.
    - mysite/urls.py: The URL declarations for this Django project; a “table of contents” of your Django-powered site. You can read more about URLs in URL dispatcher.
    - mysite/wsgi.py: An entry-point for WSGI-compatible web servers to serve your project. See How to deploy with WSGI for more details. MASIH BINGUNG DENGAN WSGI
- **hosting a local server**: `python manage.py runserver`

### django project structure 
> semua ini sudah ada dari ringkasan di docs di atas
- `python manage.py help` 
    - list semua args yang bisa dipake di manage.py
    - do edit manage.py except if you know what you're doing. *haha*
- *startapp vs startproject apa bedanya? *
- `db.sqlite3` --> auto generated database
    - dipake di project selanjutnya
- `settings.py`
    - setting up base directory 
    - secret_key
    - debug_mode
    - allowed_host (?)
- `urls.py`

### urls
- ganti list urlpatterns buat bikin backlink, pake `path('nama/', admin.site.urls)` berarti bikin backlink ke admin. 
- `python('nama', nama_views.function_1.nama_url)`
    -  return http response di fungsi dalam nama_views nya. 
        `from django.http import HttpResponse`
    - disini ngereturn html code nya. tapi gak bisa pake file. harus return codingan langsung. 

### using html files to backlink
- masukin template dir di settings.py
- `from django.shortcuts import render`, buat display htmlnya
- point the html in urls.py

### using forms in html files: 
- PENTING UNTUK MEMAKAI NAMA/, '/' penting untuk menunjuk ke action nya 
- dengan memakai argument names di `path(count/, views.count, *name*='NAMA_NAME')` gak perlu ribet dengan nama backlinknya karena setiap action bakal ngerefer ke names nya
    - di html nya jangan lupa di kasih `{% url 'NAMA_NAME'%}` buat hyperlink/action referrer nya
- using parameter dengan request dari def nya 

### cheatsheet: 
- django-admin startproject **projectname**
- python manage.py startapp **appanme**
- python manage.py runserver
- python manage.py makemigrations
- python manage.py createsuperuser 
- python manage.py manage.py collectstatic