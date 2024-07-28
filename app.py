from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model_file = open('mulmodel.pkl', 'rb')
model = pickle.load(model_file, encoding='bytes')

@app.route('/')
def index():
    return render_template('index.html', insurance_cost=0)

@app.route('/predict', methods=['POST'])
def predict():
    '''
    Predict the insurance cost based on user inputs
    and render the result to the html page
    '''
    fone, ftwo, fthree, ffour, ffive = [x for x in request.form.values()]

    data = []

    #data.append(int(age))
    if fone == '1':
        data.extend([1])
    else:
        data.extend([0])
    
    if ftwo == '1':
        data.extend([1])
    else:
        data.extend([0])

    if fthree == '1':
        data.extend([1])
    else:
        data.extend([0])
        
    if ffour == '1':
        data.extend([1])
    else:
        data.extend([0])
    
    if ffive == '1':
        data.extend([1])
    else:
        data.extend([0])

    prediction = model.predict([data])

    output = round(prediction[0], 1)

    return render_template('index.html', insurance_cost=output, fone=fone, ftwo=ftwo, fthree=fthree, ffour=ffour, ffive=ffive)


if __name__ == '__main__':
    app.run(debug=True)