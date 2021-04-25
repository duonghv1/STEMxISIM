# Python Library Imports
from collections import namedtuple, defaultdict

Article = namedtuple('Article', ['first_name', 'last_name', 'occupation', 'linkedin', 'website', 'article', 'statement', 'title'])

#Flask App
from flask import Flask, request, render_template, redirect

# Creating Flask App object
app = Flask(__name__, template_folder="templates")

database = defaultdict(list)
mailing_list = []
#load the home page
@app.route('/')
def root():
  return render_template('index.html')

#load the issues
@app.route('/issues')
def view_issue():
  return render_template('issues.html')

#load the about
@app.route('/about')
def about():
  return render_template('about.html')

#load the articles
@app.route('/articles/<category>')
def view(category):
    if category == "all":
        data = database
    else:
        data = [i for i in database if i['category'] == category]
    return render_template("articles.html", category=category, data=data)


# Render view page with specific category filter
#if you want to change the category later, have the method = "POST" and action = '/articles-cat' in <form>
@app.route('/articles-cat', methods=['POST'])
def change_category():
    category = request.form["category"]
    return redirect('/articles/' + category) 


# POST method (receives information, sends back information)
@app.route('/add-article', methods=['POST', 'GET'])
def add_article():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        category = request.form['category']
        occupation = request.form['occupation']
        linkedin = request.form['linkedin']
        personal_link = request.form["personalwebsite"]
        article = request.form['article']
        personal_statement = request.form['statement']
        title = request.form['title']
        

        database[category].append(Article(first_name, last_name, occupation, linkedin, personal_link, article, personal_statement, title))
    return redirect("/contribute")
  



@app.route('/contribute')
def contribute():
    return render_template('contribute.html')


@app.route('/add-email', methods=['POST'])
def add_email():
    email = request.form['email']
    mailing_list.append('email')
  
#load the issues
@app.route('/connect')
def connect():
  return render_template('connect.html')

# Runs Flask App
if __name__ == "__main__":
    app.run()
