from janome.tokenizer import Tokenizer
from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

app = Flask(__name__)

dict_polarity = {}
with open('./polarity.txt', 'r') as f:
    line = f.read()
    lines = line.split('\n')
    for i in range(len(lines)):
        linecomponents = lines[i].split(':')
        dict_polarity[linecomponents[0]] = linecomponents[3]

def judge_polarity(text):
    t = Tokenizer()
    tokens = t.tokenize(text)
    pol_val = 0
    for token in tokens:
        word = token.surface
        pos = token.part_of_speech.split(',')[0]
        if word in dict_polarity:
            pol_val += float(dict_polarity[word])
            pol_val = round(pol_val, 5)

    if pol_val > 0.3:
        return "ポジティブです。 Score: " + str(pol_val)
    elif pol_val < -0.3:
        return "ネガティブです。 Score: " + str(pol_val)
    else:
        return "ニュートラルです。 Score: " + str(pol_val)

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('app.html', form=form)

@app.route('/negaposi', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        sent = request.form['sayhello']
        result = judge_polarity(sent)
        return render_template('negaposi.html', sent=result)
    return render_template('app.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)