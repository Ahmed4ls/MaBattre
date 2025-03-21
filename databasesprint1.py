import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate('Privatekey.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://mabattre-default-rtdb.firebaseio.com/'
})

ref = db.reference()


def read_data(user_id):
    try:
        data = ref.child(user_id).get() 
        return data
    except Exception as e:
        print(f"Error reading data for user {user_id}:", e)
        return None


def write_data(user_id, data): 
    try:
        ref.child(user_id).set(data) 
        return True
    except Exception as e:
        print(f"Error writing data for user {user_id}:", e)
        return False


def cleanup():
    firebase_admin.delete_app(firebase_admin.get_app())
