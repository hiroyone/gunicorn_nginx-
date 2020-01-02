from flask import Flask, escape, request
import datetime

app = Flask(__name__)

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    # language = request.args["language"] # Returns 400 error if not exists
    return f'''<h1>Hello, {escape(name)}!</h1> <br>
    <img src="https://picsum.photos/200/300" alt="Italian Trulli">
    <li><a href="/query-example?language=japanese&framework=Flask&name=Ania">/query-example?language=japanese&framework=Flask&name=Ania</a> </li>
    <li><a href="/form-example">/form-example</a> </li>
    '''

# About request
# https://scotch.io/bar-talk/processing-incoming-request-data-in-flask
@app.route('/query-example', methods=['GET']) # allow only GET request
def query_example():
    language = request.args.get('language') # if key doesn't exist, return None
    framework = request.args['framework'] # if key doesn't exist, return a 400, bad request error
    name = request.args.get('name')
    return '''
    The language of your request is {} <br>
    This website is rendered by <b>{}</b> <br>
    You are logged as {}
    '''.format(escape(language), escape(framework), escape(name))

@app.route('/form-example', methods=['GET', 'POST']) # allow both GET and POST request
def form_example():
    if request.method == 'POST': #this block is only entered when the form is submitted
        language = request.form.get('language')
        framework = request.form['framework']
        return '''
        <h1> The langauge of your request is  {} <br></h1>
        This website is rendered by <b>{}</b> <br>
        '''.format(escape(language), escape(framework))

    return '''
    <form method="POST">
        Language: <input type="text" name="language"> <br>
        Framework: <input type="text" name="framework"> <br>
        <input type="submit" value="Submit"><br>
    </form>
    '''

@app.route('/json-example', methods=['POST']) #GET requests will be blocked
def json_example():
    # The following is an expected Json format
    # {
    #     "langauge":"English",
    #     "framework":"Flask",
    #     "name":"Anonymous",
    #     "access_date":{
    #         "datetime":datetime.datetime.now(),
    #         "date":datetime.date.today()
    #     },
    #     "ingredients":["Onions","Lemon","Salt",] ,
    #     "boolean_test":true
    # }
    req_data = request.get_json()
    language=escape(req_data['language'])
    framework=escape(req_data['framework'])
    name = escape(req_data['name'])
    date=escape(req_data['access_date']['date'])
    ingredients = req_data['ingredients']
    li_ingredients=''
    # Create a list of ingredients by <li>
    for ingredient in ingredients:
        esc_ingredient=str(escape(ingredient))
        li_ingredients+="<li>"+esc_ingredient+ "</li>"+"\n"
    boolean_test = req_data['boolean_test']
    return '''
        <h1> The langauge of your request is  {} <br></h1>
        This website is rendered by <b>{}</b> <br>
        Your Name is {} <br>
        Ingredients you want to buy today!<br>
        <ol>
        {}
        </ol>
        3+3=6 ? => {} <br>
        Today is {} <br>
    '''.format(language, framework, name, li_ingredients, boolean_test, date)

    # return '''
    #        The language value is: {}
    #        The framework value is: {}
    #        The Python version is: {}
    #        The item at index 0 in the example list is: {}
    #        The boolean value is: {}'''.format(language, framework, python_version, example, boolean_test)

## Run one of the following command to launch a web server
# env FLASK_APP=myapp.py flask run # If you want to use the defult Flask Server
# gunicorn myapp:app --config guniconf.py # assume that gunionf.py is already configured

# ----
# def app(environ, start_response):
#     data = b"Hello, World!\n"
#     start_response("200 OK", [
#         ("Content-Type", "text/plain"),
#         ("Content-Length", str(len(data)))
#     ])
#     return iter([data])

## Run the following command
# gunicorn -w 4 myapp:app


