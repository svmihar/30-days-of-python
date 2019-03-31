# Deploy to internet (VPS)

[digital ocean documentation](https://www.digitalocean.com/community/tutorials/how-to-set-up-django-with-postgres-nginx-and-gunicorn-on-ubuntu-16-04)

## three tier architecture
### Gunicorn
- this creates the *.wsgi files
- "serves" the app 
- sock file (references the code inside wsgi project)
### nginx
- "gateway" untuk connect dengan sock file 
- 
### why nginx + gunicorn?
gunicorn + nginx hanyalah untuk handle request dari user. python isn't that good at handling all types of request. in isesuai dengan "aturan" serving static assets: three tier architecture. 

nginx: serves static/media files. 
gunicorn: "gateway" for nginx to communicate with the django deployment.    

The outside world <-> Nginx <-> The socket <-> Gunicorn

## domain 
use [google domain](domains.google.com)