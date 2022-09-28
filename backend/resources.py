from flask import Flask, jsonify
from flask_restful import Api, Resource
import json

class Map(Resource):
    def get(self):
        try:
            f = open('geojson_sample_data.json', 'r')
            data = json.load(f)
            f.close()
            return data
        except:
            return {'msg': "Something's happened, server is on but your request is incompleted"}, 500