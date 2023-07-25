from flask import render_template, jsonify, request, Blueprint, redirect, url_for
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
            
            #return jsonify(data)  # Devuelve la respuesta de la API en formato JSON
            
            return render_template('user.html', users=data)
            

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

        # Obtener los datos enviados en el cuerpo de la solicitud
        nombre = request.form.get('nombre')
        edad = request.form.get('edad')
        correo = request.form.get('correo')

        # Convertir los datos a un diccionario
        data = {
            "nombre": nombre,
            "edad": int(edad),
            "correo": correo
        }

        # Hacer el POST request a FastAPI
        response = requests.post(url, json=data)

        print(response)

        if response.status_code == 200:
            data = response.json()
            
            #return jsonify(data)

            return redirect(url_for('user.getUsers'))

        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

    


@user.route('/updateUser/<uuid:id>', methods=['GET', 'POST', 'PUT'])
def update_user(id: uuid.UUID):
    
    if request.method == 'POST':
        try:

            # Obtener los datos enviados en el cuerpo de la solicitud
            nombre = request.form.get('nombre')
            edad = request.form.get('edad')
            correo = request.form.get('correo')

            # Convertir los datos a un diccionario
            data = {
                "nombre": nombre,
                "edad": int(edad),
                "correo": correo
            }

            # Construir la URL para FastAPI con el ID proporcionado
            update_url = f"{url}{id}"

            # Hacer el PUT request a FastAPI
            response = requests.put(update_url, json=data)

            if response.status_code == 200:
                data = response.json()
                #return jsonify(data)

                return redirect(url_for('user.getUsers'))
            else:
                return f"Error: {response.status_code} - {response.text}"
        
        except requests.exceptions.RequestException as e:
            return f"Error: {e}"

    response = requests.get(f"{url}{id}")
    data = response.json()
    return render_template('updateUser.html', user=data)
        
        


@user.route('/deleteUser/<uuid:id>', methods=['GET', 'POST', 'DELETE'])
def delete_user(id: uuid.UUID):
    try:
        # Construir la URL para FastAPI con el ID proporcionado
        delete_url = f"{url}{id}"

        # Hacer el PUT request a FastAPI
        response = requests.delete(delete_url)
        print(response)

        if response.status_code == 200:
            return redirect(url_for('user.getUsers'))
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    