from flask import Flask,render_template,redirect,request



#__name__==__main__
app = Flask(__name__)

friends = ["ram","shyam","rohan"]
num = 5

@app.route('/')
def hello():
    return render_template("index.html", my_friends = friends, number=num)

@app.route('/about')
def about():
    return "<h1>About Page</h1>"

@app.route('/home')
def home():
    return redirect('/')

@app.route('/submit', methods=['POST'])
def submit_data():
    if request.method == 'POST':
        name = request.form['username']
        f = request.files['userfile']
        print(f)
        f.save(f.filename)

    return "<h1>Hello {}".format(name)

if __name__ == "__main__":
    #app.debug = True
    app.run(debug = True)