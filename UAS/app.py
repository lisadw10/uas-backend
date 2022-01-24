from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

null = None

class inspire(Resource):
    def get(self):
        f = open("inspire.json","r")
        data = json.load(f)
        return data

class elements(Resource):
    def get(self):
        f = open("elements.json","r")
        data = json.load(f)
        return data

class service(Resource):
    def get(self):
        f = open("service.json","r")
        data = json.load(f)
        return data

class FAQ(Resource):
    def get(self):
        f = open("FAQ.json","r")
        data = json.load(f)
        return data

class about(Resource):
    def get(self):
        f = open("about.json","r")
        data = json.load(f)
        return data

class contactus(Resource):
    def get(self):
        f = open("contactus.json","r")
        data = json.load(f)
        return data

class pasone(Resource):
    def get(self):
        f = open("pasone.json","r")
        data = json.load(f)
        return data

class video(Resource):
    def get(self):
        f = open("video.json","r")
        data = json.load(f)
        return data


api.add_resource(inspire, '/home/')
api.add_resource(elements,'/elements/')
api.add_resource(service, '/service/')
api.add_resource(FAQ, '/FAQ/')
api.add_resource(about, '/about/')
api.add_resource(contactus, '/contactus/')
api.add_resource(pasone, '/pasone/')
api.add_resource(video, '/video/')

@app.errorhandler(404)
def page_not_found(e):
    return {"error":"Not Found"}, 404

if __name__ == '__main__':
    app.run(debug=True)