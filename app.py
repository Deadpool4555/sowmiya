from flask import Flask, render_template,request
import os
app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page2')
def page2():
    return render_template('view.html')

@app.route('/Attendence')
def Attendence():
    os.system('python script1.py')
    return 'Attendence is being recoded'


@app.route('/form2', methods=['POST'])
def form2():
    input2 = request.form['fi']
    osCommandString = f"notepad.exe {input2}.csv"
    os.system(osCommandString)
    
    
    
    
    return f"Opeaning the attendence of {input2}"
    # Do something with input2
    
if __name__ == '__main__':
    app.run(debug=True)
