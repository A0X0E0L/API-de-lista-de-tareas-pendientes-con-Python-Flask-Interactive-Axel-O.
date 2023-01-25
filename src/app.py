from flask import Flask,jsonify,request 
import json
app = Flask(__name__)
# la combinacion de keys y valores es un diccionario
todos = [{ "label": "My first task", "done": False }]



@app.route('/todos', methods=['GET'])
def hello_world():
  # La va convertir en algo con formato json, jsonify es una funcion que se encarga de convertir diccionario en un archivo json.
    json_text=jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])#añade un nuevo elemento
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    
    json_text=jsonify(todos)
    return json_text

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    json_text=jsonify(todos)
    return json_text
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245,debug=True)