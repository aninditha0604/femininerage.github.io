from flask import Flask, request, jsonify, send_from_directory, render_template
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
import os
import json
from datetime import datetime
import uuid

app = Flask(__name__, static_folder='static', template_folder='templates')
CORS(app)

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max upload size

# Load data from JSON files or create if they don't exist
def load_data(filename):
    try:
        with open(f'data/{filename}.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        os.makedirs('data', exist_ok=True)
        return []

def save_data(data, filename):
    with open(f'data/{filename}.json', 'w') as f:
        json.dump(data, f, indent=4)

# Initialize data
users = [
    {
        "id": 1,
        "username": "clara",
        "password": generate_password_hash("surprisewood_3"),
        "isCreator": True
    },
    {
        "id": 2,
        "username": "mickey",
        "password": generate_password_hash("michaelarosealfano_30"),
        "isCreator": False
    },
    {
        "id": 3,
        "username": "hannah",
        "password": generate_password_hash("greatwhitefart_14"),
        "isCreator": False
    },
    {
        "id": 4,
        "username": "fiona",
        "password": generate_password_hash("moomoohorsecousin_17"),
        "isCreator": False
    },
    {
        "id": 5,
        "username": "lydia",
        "password": generate_password_hash("naughtygirl_20"),
        "isCreator": False
    },
    {
        "id": 6,
        "username": "jenna",
        "password": generate_password_hash("bombastic_24"),
        "isCreator": False
    },
    {
        "id": 7,
        "username": "anin",
        "password": generate_password_hash("cooch_6"),
        "isNextCreator": True
    }
]

# Initial questions data
default_questions = [
    {
        "id": 1,
        "text": "What feminine qualities do you most admire in yourself and why?",
        "creator": "clara",
        "createdAt": "2025-03-01T12:00:00
