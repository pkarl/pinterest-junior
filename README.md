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

## TODO

* JS to lay results out in mulitple columns
* refine form template to use input[type=text] instead of textarea
* style form
* error handling code
* tests