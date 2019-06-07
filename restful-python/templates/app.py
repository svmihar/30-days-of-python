from flask import Flask, jsonify, request
from flask_restful import Api, Resource


app = Flask(__name__)
api = Api(app)

def check_posted_data(posted_data, function_name): 
    if (function_name == "add"): 
        if 'x' not in posted_data or 'y' not in posted_data: 
            return 301
        else: 
            return 200

def check_json(json, method='Add'): 
    if 200 != check_posted_data(json, method): 
        return True 
    return return_json

class Add(Resource): 
    def post(self): 
        # resource add requested with post
        posted_data = request.get_json()
        if check_json(posted_data, method='Add'): 
            return_json = {
                'Message': 'Error occured', 
                'Status': 301
            }
            return return_json
            
        x = posted_data['x']
        y = posted_data['y']
        x, y = int(x), int(y)
        ret = x+y 

        return_map = {
            'Sum': ret, 
            'Status Code':200 
        }
        return jsonify(return_map)


    def get(self): 
        # resource add requests using get
        pass

    def put(self): 
        pass

    def delete(self): 
        pass

class Subtract(Resource): 
    def post(self): 
    # resource add requested with post
        posted_data = request.get_json()
        if check_json(posted_data, method='Subtract'): 
            return_json = {
                'Message': 'Error occured', 
                'Status': 301
            }
            return return_json
            
        x = posted_data['x']
        y = posted_data['y']
        x, y = int(x), int(y)
        ret = x-y 

        return_map = {
            'Sum': ret, 
            'Status Code':200 
        }
        return jsonify(return_map)

class Multiply(Resource): 
    def post(self): 
        posted_data = request.get_json()
        if check_json(posted_data, method='Multiply'): 
            return_json = {
                'Message': 'Error occured', 
                'Status': 301
            }
            return return_json
            
        x = posted_data['x']
        y = posted_data['y']
        x, y = int(x), int(y)
        ret = x*y 

        return_map = {
            'Sum': ret, 
            'Status Code':200 
        }
        return jsonify(return_map)

class Divide(Resource): 
    def post(self): 
        # resource add requested with post
        posted_data = request.get_json()
        if check_json(posted_data, method='Add'): 
            return_json = {
                'Message': 'Error occured', 
                'Status': 301
            }
            return return_json
            
        x = posted_data['x']
        y = posted_data['y']
        x, y = int(x), int(y)
        try: 
            ret = x/y 
        except: 
            return_json = {
                'Message': 'CANNOT DIVIDE BY ZERO', 
                'Status': 000
            }
            return jsonify(return_json)

        return_map = {
            'Sum': ret, 
            'Status Code':200 
        }
        return jsonify(return_map)


api.add_resource(Add, "/add")

@app.route('/')
def hello_world(): 
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True)