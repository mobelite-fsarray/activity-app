import app
from firebase_admin import credentials, firestore, initialize_app, auth
from firebaseCRUD import create_document, delete_document

# setup firebase admin
admin = initialize_app(credential=credentials.Certificate("firebase.json"))
