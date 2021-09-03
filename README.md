# A complete Flask tutorial for beginners

> ### Flask is an API of Python that allows us to build up web-applications. It was developed by Armin Ronacher. 
> 
> ### Get started with Installation and then get an overview with the Quickstart. This Tutorial will shows how to create a small but complete application with Flask.

## Table of Content
<hr>

- [Minimal app](#minimal-app)
- [Routing](#routing)
- [Url Variables](#url-variables)
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
> Flask's framework is more explicit than Django's framework and is also easier to learn because it has less base code to implement a simple web-Application.
List of companies using Flask framework - who is using Flask?

### Companies using Flask

- [Red Hat](http://redhat.com) , [Rackspace](http://rackspace.com), [Airbnb](http://airbnb.com), [Netflix](https://medium.com/netflix-techblog/automation-as-a-service-introducing-scriptflask-17a8e4ad954b), [PythonAnywhere](https://www.pythonanywhere.com/), [Lyft](https://stackshare.io/lyft/lyft), [Reddit](https://stackshare.io/reddit/reddit), [Mailgun](https://stackshare.io/mailgun/mailgun), [MIT](https://stackshare.io/mit/mit), [Mozilla](https://www.mozilla.org), [Balrog (Application Update Service)](https://github.com/mozilla/balrog), [Release Engineering Services](https://github.com/mozilla-releng/services), [Hotjar](https://stackshare.io/hotjar/hotjar), [Patreon](https://stackshare.io/patreon/patreon), [Teradata](https://stackshare.io/teradata/teradata), [Uber](https://stackshare.io/uber/partners-uber-com), [Samsung](https://stackshare.io/engel80/apkg), [Nginx](https://stackshare.io/nginx-inc/nginx-amplify), +1.5k more companies in [https://stackshare.io/flask/](https://stackshare.io/flask/)

## Minimal app

[Code Here ⚙️](/minimal_app)

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

<hr>

## Routing

[Code Here ⚙️](/routing)

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is Index Page'

@app.route('/login')
def login():
    return 'This is Login Page'

@app.route('/hello')
def hello():
    return 'Hello, World'

if __name__=="__main__":
    app.run(debug=True)

```

> Modern web applications use meaningful URLs to help users. Users are more likely to like a page and come back if the page uses a meaningful URL they can remember and use to   directly visit a page.

> Use the route() decorator to bind a function to a URL.

<hr>

## Url Variables

[Code Here ⚙️](/url_variables)


```python
  
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# string
@app.route('/string/<string:value>')
def string(value):
    return f"<p>Hi this is a string value {value}</p>"

# int
@app.route('/int/<int:value>')
def int(value):
    return f"<p>Hi this is a int value {value}</p>"

# float
@app.route('/float/<float:value>')
def float(value):
    return f"<p>Hi this is a float value {value}</p>"

# path
@app.route('/path/<path:value>')
def path(value):
    return f"<p>Hi this is a path value {value}</p>"

# uuid
@app.route('/uuid/<uuid:value>')
def uuid(value):
    return f"<p>Hi this is a uuid value {value}</p>"



if __name__=="__main__":
    app.run(debug=True)
    
```

> You can add variable sections to a URL by marking sections with `<variable_name>`. Your function then receives the `<variable_name>` as a keyword argument. Optionally, you can use a  converter to specify the type of the argument like <converter:variable_name>.

