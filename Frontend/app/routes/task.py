from flask import render_template, jsonify, request, Blueprint
import requests
import uuid

task = Blueprint('task', __name__)


# URL de la ruta en FastAPI
url = "http://localhost:8000/task/"


@task.route('/task/', methods=['GET'])
def getTasks():
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            #return jsonify(data)  # Devuelve la respuesta de la API en formato JSON

            return render_template('task.html', tasks=data)

        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    


@task.route('/task/<uuid:id>', methods=['GET'])
def getTask(id: uuid.UUID):
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
#     "usuario_id": "37996716-0f81-4e4e-bd08-ad6795b344e7", 
#     "tarea": "Crear frontend con Flask", 
#     "id_estado": 1
# }
@task.route('/task/', methods=['POST'])
def create_task():
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
    


@task.route('/task/<uuid:id>', methods=['PUT'])
def update_task(id: uuid.UUID):
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
    


@task.route('/task/<uuid:id>', methods=['DELETE'])
def delete_task(id: uuid.UUID):
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
    