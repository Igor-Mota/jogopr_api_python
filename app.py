from flask import Flask
from flask_cors import CORS
import sys
import src.routes

sys.dont_write_bytecode = False

app = Flask(__name__)


src.routes.routes(app)

app.run(debug=True)
