from flask import Flask
import sys
import src.routes

sys.dont_write_bytecode = False

app = Flask(__name__)

src.routes.routes(app)

app.run(debug=True)