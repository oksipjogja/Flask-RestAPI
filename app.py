# Import Library
from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# Inisiasi object flask
app = Flask(__name__)

# Inisiasi objek flask_restful
api = Api(app)

# Inisiasi objek flask_cors
CORS(app)

# inisiasi variabel kosong bertipe dictionary
identitas = {}  # variabel global, dictionary JSON

# membuat class Resource
class ContohResource(Resource):
    # metode GET dan POST
    def get(self):
        # response = {"msg":"Holla Dunia, Ini app restful pertamaku"}
        return identitas

    def post(self):
        nama = request.form["nama"]
        umur = request.form["umur"]
        identitas["nama"] = nama
        identitas["umur"] = umur
        response = {"msg":"Data berhasil dimasukan"}
        return response


# Setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"],)

if __name__ == '__main__':
    app.run(debug=True, port=5080)