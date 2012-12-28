# Pinterest Jr.

This is a super simple Django app that uses the embedly API to replicated Pinterest.

Admin user/pass is `admin` / `admin`

## Requirements

If you're using `pip` you can pull in the reqs with a `pip install -r requirements.txt`

If not, here's what's in there:

```
Django==1.4.3
Embedly==0.4.3
httplib2==0.7.7
wsgiref==0.1.2
```

I recommend you use the wonderful `virtualenv` and `virtualenvwrapper` tools for your development environment.

## Static file handling

Static files are JavaScript, CSS, or image files that accompany each app. Every application module in the django project has its own `/static` directory which contains the static files for that module.

There is a global `/static` directory located at the project root (the contents of which are ignored by git) where all of these static files will be collected upon running the `python manage.py collectstatic` command, which refers to the `STATIC_ROOT`, `STATIC_URL`, `STATICFILES_DIRS`, and `STATICFILES_FINDERS` vars in your `settings.py`.

## TODO

* style form
* error handling code
* tests
* pinboard creation & organization
