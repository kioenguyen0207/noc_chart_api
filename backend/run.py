from resources import *

#init
app = Flask(__name__)
api = Api(app)

#endpoint(s)
api.add_resource(Map, "/map")

if __name__=='__main__':
    app.run(host="0.0.0.0", port=443)
    # app.run()
    # gunicorn --chdir backend run:app -w 2 --threads 2 -b 0.0.0.0:443