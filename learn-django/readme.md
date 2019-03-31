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


## personal portofolio 
- virtualenv *lebih enak pake conda env. jadi i don't really follow this*
  - jangan taro di dalem project folder
- databases/postgress and models
- admin interface
- work with static files
- allowing users to upload files 
- using bootstrap 

### django apps
- you can create apps inside a django projects
  - semacam mini sections, yang punya views nya sendiri...
- `python manage.py startapp nama_appnya` 
- jangan lupa ditambah ke urlpatterns nya
  <!-- - import nama_.views -->
  - di views.py dalam nama, harus ada method buat render html/return html codenya.
  - dalam urlpatterns ditambah import nama_.views, 
    - tambahin di path('', nama_.views.home), kalo buat homepage
  - kasih name='home' biar gampang di refer di tempat lain. 
### django models
- you can dynamically edit the "content" of the jobs with database
  - jadi berubah sesuai dengan data yang ada di database nya. 
    ```python: 
    class Job(models.Model):
    pass
    ```
- choose any database you want, tapi pake models.Model sebagai argumen untuk menunjuk database nya.  
- untuk liat setiap field yang bisa di edit di database bisa di lihat [di model reference documentation nya django](https://docs.djangoproject.com/en/2.1/topics/db/models/)
- tiap file yang di save di model harus dalam satu central folder buat medianya. biasanya dinamakan `media/`, atau `images/`
- jangan lupa ditambah di `settings.py` di folder projectnya
  - tambah apps confignya di `INSTALLED_APPS`
- tambah media di `settings.py` buat ngeset folder dimana gambar/asset tertentu akan di save
    - untuk setiap gambar pasti pake PILLOW buat manajemen file nya
        - manajemen yang dimaksud adalah tipe filenya. 

### django migrate
- buat update modelsnya
- auth, session, sudah ada di cache, jadi harus di update dalam modelsnya 
- MIGRATION = SETUP DATABASE
- setiap update pada directory, `settings.py`, harus makemigrations biar ke update `class Migration` nya

### django admin 
- jangan lupa buat username dan password 
    - `python manage.py createsuperuser` 
- harus migrate dulu biar keupdate modelnya, dan biar ada nama dulu tablenya bukan ada tablenya baru ada namanya. 
    - `python manage.py migrate` 
- buat ngedit 'database' yang ada di admin panel harus edit dulu `admin.py` nya di tiap app-nya
        ```python 
        from django.contrib import admin

        # Register your models here.
        from .models import Job     def __str__(self): 
        return self.title 

        admin.site.register(Job)
        ```
- dengan django admin ini gak perlu nyentuh database secara langsung tapi bisa bikin script sendiri buat ngedit tablenya di database. ***this is gold***
- buat images atau asset yang ada di dalam database harus ditambah dalam `urlpattern` nya dengan: 
    ```python 
    from django.conf import settings
    from django.conf.urls.static import static
    urlpatterns = [] + static(tambah image url yang ada di settings.py, document_root=media_root)
    ```

### database: postgresql 
- connect: 
    - `sudo su - postgres`
    - `psql` 
- running server: 
    - jangan lupa install `pip install psycopg2` 
- ini agak ribet buat setupnya sepertinya harus terpisah buat catetannya. 
- buat make isi database tinggal import: 
  - `from .models import {nama_app}`
- import nya akan mengimport database model dari models.py 

### handling static asset: image, css, js, etc
- bisa pake cdn (agak lama)
- locally stored 

### INCLUDE URLCONF (semacam backlink)
1. Import the include() function: from django.urls import include, path
2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
- ini membuat otomatis apapun yang ke save (*dibuat dulu*) `urls.py` ke dalam app nya. 
- jangan lupa buat ditambah di modelsnya. 

### function inside models.py within class
- contohnya disini bikin "summary" (just a truncated version of the long text tho.) dari apa yang ada di dalam body (`models.TextField()`)
- **making dates pretty.**
    ```python 
    def dates(self): 
            return pub_date.strftime('%b %e %Y')
    ```
- pake *strftime*.

### make django admin, not showing "objects", but the title of the post. 
```python 
    def __str__(self): 
        return self.title 
```

### cheatsheet: 
- django-admin startproject **projectname**
- python manage.py startapp **appanme**
- python manage.py runserver
- python manage.py makemigrations
- python manage.py createsuperuser 
- python manage.py manage.py collectstatic