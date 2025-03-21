import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('Privatekey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mabattre-default-rtdb.firebaseio.com/'
})

ref = db.reference()
