# Dependências do Flask
from flask import Flask
from flask import jsonify
from flask import request
from flask_cors import CORS

# Dependências do Keras
import keras
from keras.models import load_model

# Dependências do Numpy
import numpy as np

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
CORS(app)

# Função que carrega a rede neural já treinada
def get_model():
    global model
    model = load_model("model.h5")
    print("Modelo carregado")


get_model()
print("Carregando a rede neural...")

# Endpoint com método que prevê se o paciente tem diabete
@app.route('/predict', methods=['POST'])
def predict():

    # Capturando o body da requisição
    request_body = request.get_json(force=True)

    # Recuperando os dados do paciente, no body
    age = request_body['age']
    bmi = request_body['bmi']
    glucose = request_body['glucose']
    insulin = request_body['insulin']
    pregnancies = request_body['pregnancies']
    skin_thickness = request_body['skin_thickness']
    blood_pressure = request_body['blood_pressure']
    diabetes_pedigree_func = request_body['diabetes_pedigree_func']

    # Montando o array com os dados do paciente
    patient_data = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_func, age]

    # Usando o modelo para fazer a previsão do começo de diabetes do paciente
    prediction = model.predict_proba(np.expand_dims(patient_data, axis=0))[0][0]

    response = {
        'prediction': {
            'diabetes': str(prediction)
        }
    }
    
    return jsonify(response)
