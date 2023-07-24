from flask import render_template, jsonify, request, Blueprint
import requests
import uuid

user = Blueprint('user', __name__)


# URL de la ruta en FastAPI
url = "http://localhost:8000/user/"


@user.route('/user/', methods=['GET'])
def getUsers():
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            return jsonify(data)  # Devuelve la respuesta de la API en formato JSON
            

        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    


@user.route('/user/<uuid:id>', methods=['GET'])
def getUser(id: uuid.UUID):
    try:
        print(f"{url}{id}")
        response = requests.get(f"{url}{id}")

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)  # Devuelve la respuesta de la API en formato JSON
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"



# {
#     "nombre": "pedro", 
#     "edad": 28, 
#     "correo": "pedro016@mail.com"
# }

@user.route('/user/', methods=['POST'])
def create_user():
    try:
        # Obtener el JSON enviado en el cuerpo de la solicitud
        data = request.get_json()
        print(data)

        # Hacer el POST request a FastAPI
        response = requests.post(url, json=data)

        print(response)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    


@user.route('/user/<uuid:id>', methods=['PUT'])
def update_user(id: uuid.UUID):
    try:
        # Obtener el JSON enviado en el cuerpo de la solicitud
        data = request.get_json()

        # Construir la URL para FastAPI con el ID proporcionado
        update_url = f"{url}{id}"

        # Hacer el PUT request a FastAPI
        response = requests.put(update_url, json=data)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    


@user.route('/user/<uuid:id>', methods=['DELETE'])
def delete_user(id: uuid.UUID):
    try:
        # Construir la URL para FastAPI con el ID proporcionado
        delete_url = f"{url}{id}"

        # Hacer el PUT request a FastAPI
        response = requests.delete(delete_url)
        print(response)

        if response.status_code == 200:
            data = response.json()
            return jsonify(data)
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    