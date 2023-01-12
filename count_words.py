from flask import Flask, request, render_template, flash, redirect 
import webbrowser
import string
import os

cwd = os.getcwd()
app = Flask(__name__, template_folder=cwd+'/html_files/')
app.secret_key = '123456'

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/', methods=['POST'])
def count_words():
    text = request.form.get('text')
    if not text:
        flash('Please enter some text to count words')        
        return redirect('/')
    
    words = len(text.translate(str.maketrans('','',string.punctuation)).split())    
    return render_template('count.html', text=text, words=words)

if __name__ == '__main__':    
    webbrowser.open("http://localhost:5000")
    app.run()    
    