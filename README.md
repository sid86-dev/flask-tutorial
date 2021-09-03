# A complete Flask tutorial for beginners

> ### Flask is an API of Python that allows us to build up web-applications. It was developed by Armin Ronacher. Flask's framework is more explicit than Django's framework and is also easier to learn because it has less base code to implement a simple web-Application.
> ### Get started with Installation and then get an overview with the Quickstart. This Tutorial will shows how to create a small but complete application with Flask.

## Table of Content
<hr>

- [Minimal app](#minimal-app)
* #### [Routing](/routing)
* #### [Url Variables](/url_variable)
* #### [Rendering Templates](/render_template)
* #### [Debug Mode](/debug_mode)
<hr>

## Installation

## `pip install flask`

<hr>
<!-- 
First Header | Second Header
------------ | -------------
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column -->

## Docs

> ### [Fask Docs](https://flask.palletsprojects.com/en/2.0.x/)
> ### [Jinja Docs](https://jinja.palletsprojects.com/en/3.0.x/)

<hr>

## Why to choose Flask

List of companies using Flask framework - who is using Flask?

### Companies using Flask

- [Red Hat](http://redhat.com) , [Rackspace](http://rackspace.com), [Airbnb](http://airbnb.com), [Netflix](https://medium.com/netflix-techblog/automation-as-a-service-introducing-scriptflask-17a8e4ad954b), [PythonAnywhere](https://www.pythonanywhere.com/), [Lyft](https://stackshare.io/lyft/lyft), [Reddit](https://stackshare.io/reddit/reddit), [Mailgun](https://stackshare.io/mailgun/mailgun), [MIT](https://stackshare.io/mit/mit), [Mozilla](https://www.mozilla.org), [Balrog (Application Update Service)](https://github.com/mozilla/balrog), [Release Engineering Services](https://github.com/mozilla-releng/services), [Hotjar](https://stackshare.io/hotjar/hotjar), [Patreon](https://stackshare.io/patreon/patreon), [Teradata](https://stackshare.io/teradata/teradata), [Uber](https://stackshare.io/uber/partners-uber-com), [Samsung](https://stackshare.io/engel80/apkg), [Nginx](https://stackshare.io/nginx-inc/nginx-amplify), +1.5k more companies in [https://stackshare.io/flask/](https://stackshare.io/flask/)

## Minimal app

[Code Here](/minimal_app)

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

if __name__=="__main__":
    app.run()

```
### So what did that code do?

1. First we imported the Flask class. An instance of this class will be our WSGI application.

2. Next we create an instance of this class. The first argument is the name of the application’s module or package. __name__ is a convenient shortcut for this that is appropriate   for most cases. This is needed so that Flask knows where to look for resources such as templates and static files.

3. We then use the route() decorator to tell Flask what URL should trigger our function.

4. The function returns the message we want to display in the user’s browser. The default content type is HTML, so HTML in the string will be rendered by the browser.
