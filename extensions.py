import os
from flask_pymongo import PyMongo
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from dotenv import load_dotenv

load_dotenv()

mongo = PyMongo()
jwt = JWTManager()
cors = CORS()
