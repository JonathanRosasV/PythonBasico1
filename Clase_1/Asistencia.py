import pandas as pd

# Cargar el archivo CSV
data = pd.read_csv('dia1.csv')

# Display the names of all columns
print(data.columns.tolist())

# Mostrar las primeras filas para entender la estructura de los datos
print(data.head())

# Extract the day and time using string slicing
data['Día'] = data['Marca temporal'].str[:10]  # The first 10 characters are the date (YYYY/MM/DD)
data['Hora'] = data['Marca temporal'].str[11:15]  # Characters 11-16 are the time in HH:MM format (24-hour assumed)

# Display the updated DataFrame
print(data[['Día', 'Hora']].tail())