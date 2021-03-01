#!./venv/bin/python3
from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask
from flask_restful import Resource, Api
from get_last_spotteds import get_last_spotteds
import atexit
import time

app = Flask(__name__)
api = Api(app)

class Spotted(Resource):
    def get(self):
        return get_last_spotteds()
    
scheduler = BackgroundScheduler()
scheduler.add_job(func=get_last_spotteds, trigger="interval", minutes=25)

scheduler.start()
api.add_resource(Spotted, '/spotteds')
get_last_spotteds()
app.run()

atexit.register(lambda: scheduler.shutdown())

