from flask import Flask, render_template,request
from numberToWord import *
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/',methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        number=request.form['number']
        word = convertNumToWord(number)
        return render_template('home.html',**{"amountToWord":word,"value":number})
    return render_template('home.html',**{"amountToWord":''})

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)