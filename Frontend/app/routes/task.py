from flask import render_template, jsonify, request, Blueprint, redirect, url_for
import requests
import uuid
from schemas.task import optionalArgGetTasks, optionalArgUserTasks

task = Blueprint('task', __name__)


# URL de la ruta en FastAPI
url = "http://localhost:8000/task/"
url_user = "http://localhost:8000/user/"


# def create_new_user(user: createUser):
# user.filtro
@task.route('/task/', methods=['GET'])
def getTasks(filtro = None):
    try:
        response_task = requests.get(url)
        response_users = requests.get(url_user)

        if response_task.status_code == 200:

            if response_users.status_code == 200:
                data_task = response_task.json()
                data_users = response_users.json()

                if filtro != "" and filtro is not None:
                    list_task = sorted(data_task, key=lambda x: x[filtro])
                else:
                    list_task = data_task

                #return jsonify(data)  # Devuelve la respuesta de la API en formato JSON

                return render_template('task.html', tasks=list_task, users=data_users)
            
            else:
                return f"Error: {response_users.status_code} - {response_users.text}"

        else:
            return f"Error: {response_task.status_code} - {response_task.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"


# enviar name de usuario o sus datos como argumento y luego puedo enviar una lista al render
@task.route('/userTasks/', methods=['GET'])
def userTasks():

    # Parametros que luego envio al template
    name = request.args.get('name')
    correo = request.args.get('correo')
    idUser = request.args.get('idUser')


    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            
            #return jsonify(data)  # Devuelve la respuesta de la API en formato JSON

            return render_template('userTasks.html', userTasks=data, name=name, correo=correo, idUser=idUser)

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

    response_users = requests.get(url_user)

    if response_users.status_code == 200:   
        data_users = response_users.json()

    # Obtener los datos enviados en el cuerpo de la solicitud
    tarea = request.form.get('tarea')
    usuario = request.form.get('userCorreo')
    estado = request.form.get('estado')


    for user in data_users:

        if user['correo'] == usuario:
            usuario_id = user['id']


    if estado == "Pendiente":
        id_estado = 1
    
    elif estado == "En progreso":
        id_estado = 2
                        
    elif estado == "Completada":
        id_estado = 3

    # Convertir los datos a un diccionario
    data = {
        "tarea": tarea,
        "usuario_id": usuario_id,
        "id_estado": id_estado
    }

    # Hacer el POST request a FastAPI
    response = requests.post(url, json=data)


    if response.status_code == 200:
        data = response.json()
        
        #return jsonify(data)

        return redirect(url_for('task.getTasks'))

    else:
        return f"Error: {response.status_code} - {response.text}"
    


# <td><a href="{{ url_for('task.update_task', id=task['id']) }}">✏️</a></td>
@task.route('/updateTask/<uuid:id>', methods=['GET', 'PUT'])
def update_task(id: uuid.UUID):

    estado = request.args.get('estado')
    pagina = request.args.get('pagina')

    response = requests.get(f"{url}{id}")

    if response.status_code == 200:
        data = response.json()

    try:
        # Obtener el JSON enviado en el cuerpo de la solicitud
        #data = request.get_json()

        if estado == "Pendiente":
            data['id_estado'] = 1
        
        elif estado == "En progreso":
            data['id_estado'] = 2
                            
        elif estado == "Completo":
            data['id_estado'] = 3


        # Hacer el PUT request a FastAPI
        update_response = requests.put(f"{url}{id}", json=data)

        if update_response.status_code == 200:
            #data = response.json()
            #return jsonify(data)

            if pagina == "task":
                return redirect(url_for('task.getTasks', filtro=" "))
            
            elif pagina == "user":
                # Parametros que luego envio al template
                name = request.args.get('name')
                correo = request.args.get('correo')
                idUser = request.args.get('idUser')


                return redirect(url_for('task.userTasks', userTasks=data, name=name, correo=correo, idUser=idUser))
           
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    


@task.route('/deleteTask/<uuid:id>', methods=['GET', 'DELETE'])
def delete_task(id: uuid.UUID):
    
    pagina = request.args.get('pagina')

    try:
        # Construir la URL para FastAPI con el ID proporcionado
        delete_url = f"{url}{id}"

        # Hacer el PUT request a FastAPI
        response = requests.delete(delete_url)
        print(response)

        if response.status_code == 200:
            # data = response.json()
            # return jsonify(data)

            if pagina == "task":
                return redirect(url_for('task.getTasks', filtro=" "))
            
            elif pagina == "user":
                return redirect(url_for('user.getUsers'))
            
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"
    
