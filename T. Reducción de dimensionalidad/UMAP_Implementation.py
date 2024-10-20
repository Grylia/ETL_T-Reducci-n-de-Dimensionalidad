from flask import Flask, jsonify
import pandas as pd
import umap
from sklearn.preprocessing import StandardScaler

# Crear la aplicación Flask
app = Flask(__name__)

# Cargar el dataset desde un archivo CSV
df = pd.read_csv('phone search.csv')  # Asegúrate de que este archivo esté en la misma carpeta que tu script

# Ruta principal de la API
@app.route('/')
def home():
    return "API de búsqueda de teléfonos y reducción de dimensionalidad (UMAP)"

# Ruta para aplicar UMAP y devolver los componentes principales
@app.route('/api/umap', methods=['GET'])
def apply_umap():
    # Seleccionar solo columnas numéricas para UMAP
    numerical_data = df.select_dtypes(include='number')
    
    if numerical_data.empty:
        return jsonify({'error': 'No hay datos numéricos en el dataset para aplicar UMAP.'}), 400

    # Estandarizar los datos
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(numerical_data)

    # Aplicar UMAP
    reducer = umap.UMAP(n_components=2, random_state=42)
    umap_result = reducer.fit_transform(scaled_data)

    # Crear un DataFrame con los resultados de UMAP
    umap_df = pd.DataFrame(data=umap_result, columns=['Componente 1', 'Componente 2'])

    # Devolver los resultados en formato JSON
    return jsonify(umap_df.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
