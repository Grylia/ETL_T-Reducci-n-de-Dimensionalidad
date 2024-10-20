from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar el dataset
df = pd.read_csv('phone search.csv')
print(df)
# Definir una ruta básica
@app.route('/')
def home():
    return "API de búsqueda de teléfonos"

# Ruta para obtener todos los datos
@app.route('/api/phones', methods=['GET'])
def get_phones():
    data = df.to_dict(orient='records')
    return jsonify(data)

# Ruta para obtener un teléfono específico por ID
@app.route('/api/phones/<int:id>', methods=['GET'])
def get_phone(id):
    phone = df[df['id'] == id].to_dict(orient='records')
    if phone:
        return jsonify(phone[0])
    return jsonify({'error': 'Teléfono no encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)