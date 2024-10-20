import pandas as pd
import umap
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Paso 1: Cargar los datos
# Asegúrate de que el archivo 'phone_search.csv' esté en la carpeta 'data'
data = pd.read_csv('data/phone_search.csv')  # Ajusta la ruta según la ubicación de tu archivo

# Paso 2: Preprocesar los datos
# Seleccionar solo columnas numéricas para aplicar UMAP
numerical_data = data.select_dtypes(include=['float64', 'int64'])

# Paso 3: Estandarizar los datos
scaler = StandardScaler()
numerical_data_scaled = scaler.fit_transform(numerical_data)

# Paso 4: Aplicar UMAP para reducción de dimensionalidad
umap_model = umap.UMAP(n_components=2, random_state=42)
data_umap = umap_model.fit_transform(numerical_data_scaled)

# Paso 5: Crear un DataFrame con los resultados
umap_df = pd.DataFrame(data_umap, columns=['Dim1', 'Dim2'])

# Paso 6: Guardar el resultado en un archivo CSV
umap_df.to_csv('data/reduced_data.csv', index=False)

# Paso 7: Visualización de los resultados
plt.figure(figsize=(10, 8))
plt.scatter(umap_df['Dim1'], umap_df['Dim2'], alpha=0.5)
plt.title('Reducción de Dimensionalidad usando UMAP')
plt.xlabel('Dim1')
plt.ylabel('Dim2')
plt.grid()
plt.show()
