
@app.route('/new')
def myfun():
    return "welcome to flask"
@app.route('/else')
def myfun3():
    return "welcome to company"
@app.route('/else/<hello>')
def myfun4(hello):
    return "welcome to %s company" %hello

@app.route('/handle/<name>')
def myfun1(name):
    if name == 'mrv':
        return redirect(url_for('myfun'))
    elif name == 'tech':
        return redirect(url_for('myfun4',hello= name))
    else:
        return redirect(url_for('myfun3'))


if __name__ == "__main__":
    app.run()

@app.route('/valid/<name>')
def valid1(name):
    return "this is new class of %s" %name

@app.route('/send',methods=['POST','GET'])
def send():
    if request.method=='POST':
        user = request.form['name']
        return redirect(url_for('valid1',name = user))
    else:
        user = request.args.get('name')
        return redirect(url_for('valid1',name = user))
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/valid')
def myfun():
    dict = {'ajay':80,'arun':85,'surya':89,'megana':90}
    return render_template('hii.html', myfun = dict)

if __name__ == '__main__':
   app.run(debug = True)

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def marks():
    return render_template('hii.html')

@app.route('/localhost:5000/marks', methods=['POST', 'GET'])
def myfun():
    if request.method == 'POST':
        stdmarks = request.form
        return render_template('marks.html', myfun=stdmarks)
    return render_template('marks.html', myfun={})

if __name__ == '__main__':
    app.run(debug=True)

