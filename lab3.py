import re
import string
import nltk
nltk.download('wordnet')
import os
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
#from nltk.stem import SnowballStemmer
#from nltk.stem import WordNetLemmatizer

#C:\Users\mini_\AppData\Local\Programs\Python\Python312\python.exe "C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab3\lab3.py"

nltk.download('punkt')
nltk.download('stopwords')

# Ruta al archivo de entrada
input_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab3\npl\doc-text'
# Ruta al archivo de salida
output_file = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab3\documento.txt'
# Ruta al archivo de salida TRUNCADO
output_file_final = r'C:\Users\mini_\OneDrive\Documentos\Code Test\TEST 1\lab3\documento-TRUNCADO.txt'

# Lista para almacenar las líneas procesadas
processed_lines = []
# Abre el archivo de entrada y procesa las líneas
with open(input_file, 'r', encoding="utf8") as f:
    current_text = ""
    for line in f:
        line = line.strip()
        if line.endswith('/'):  # Si la línea termina con '/'
            current_text += line.replace('/', '') + ''  # Agrega el texto actual con '/' al final        
            processed_lines.append(current_text.strip())  # Agrega el texto actual procesado a la lista
            current_text = ""  # Restablece el texto actual
        elif line:  # Si la línea no está vacía
            current_text += line + "|"  # Agrega la línea al texto actual            

# Escribe las líneas procesadas en el archivo de salida
with open(output_file, 'w', encoding="utf8") as f:
    for line in processed_lines:
        f.write(line[:-1] + "\n")

# -----------------
# LEER NUEVO ARCHIVO
# -----------------

# Lee el contenido del archivo externo
archivo_path = os.path.join(os.path.dirname(__file__), 'documento.txt')
with open(archivo_path, 'r', encoding='utf-8') as archivo:
    texto = archivo.read()
    
# -----------------
# ELIMINAR ESPACIOS Y TOKENIZACION
# -----------------

# Definimos una expresión regular para encontrar números seguidos de "|"
#regex_pattern = r'\d+\|'

# Utilizamos la función sub de la biblioteca re para reemplazar los números seguidos de "|"
#processed_content = re.sub(regex_pattern, '|', texto)

# Tokenización usando NLTK
#palabras = nltk.word_tokenize(processed_content) #cambiar a texto para regresar numeros

#palabras = processed_content.split() #cambiar a texto para regresar numeros

# Tokenización usando NLTK
#palabras = nltk.word_tokenize(texto)

# -----------------
# SIGNOS DE PUNTUACION
# -----------------

# Definir expresión regular para eliminar signos de puntuación
simbolos_extra = '’'
re_punc = re.compile('[%s%s]' % (re.escape(string.punctuation), re.escape(simbolos_extra)))

# Reemplazar "|" con espacio y eliminar otros signos de puntuación
stripped = re_punc.sub(lambda x: ' ' if x.group(0) == '|' else '', texto)

# ----------------------
# CONVERTIR A MINUSCULAS
# ----------------------

stripped = stripped.lower()

# -----------------
#    STOPWORDS
# -----------------

# Obtener lista de stopwords en inglés
stopwords_english = set(stopwords.words('english'))

# Divide el contenido en líneas
lines = stripped.split('\n')

# Elimina las stopwords de cada línea del documento
filtered_lines = []
for line in lines:
    # Divide la línea en palabras
    words = line.split()
    # Filtra las palabras que no son stopwords
    filtered_words = [word for word in words if word.lower() not in stopwords_english]
    # Une las palabras filtradas en una línea nuevamente
    filtered_line = ' '.join(filtered_words)
    # Agrega la línea filtrada a la lista de líneas filtradas
    filtered_lines.append(filtered_line)

# Une las líneas filtradas en un solo documento nuevamente
filtered_words = '\n'.join(filtered_lines)

# -----------------
#     TRUNCADO
# -----------------

stemmer = PorterStemmer()

# Divide el contenido en líneas
lines = filtered_words.split('\n')

# Trunca las palabras en cada línea del documento
stemmed_lines = []
for line in lines:
    # Divide la línea en palabras
    words = line.split()
    # Aplica el stemmer a cada palabra
    stemmed_words = [stemmer.stem(word) for word in words]
    # Une las palabras truncadas en una línea nuevamente
    stemmed_line = ' '.join(stemmed_words)
    # Agrega la línea truncada a la lista de líneas truncadas
    stemmed_lines.append(stemmed_line)

# Une las líneas truncadas en un solo documento nuevamente
stemmed_content = '\n'.join(stemmed_lines)


# -----------------
#      SALIDA
# -----------------

# Imprime las primeras 100 palabras truncadas
print("\n///// TEXTO CON PALABRAS TRUNCADAS (PRIMEROS 1000 CARACTERES)\n")
print(stemmed_content[:1000])

# Escribe las líneas procesadas en el archivo de salida
with open(output_file_final, 'w', encoding="utf8") as f:
    f.write(stemmed_content)