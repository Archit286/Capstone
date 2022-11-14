import pyrebase

config = {
    "apiKey": "AIzaSyCqkAkL7q2os6rn8ZGJuu3lz55MtjRSAMI",
    "authDomain": "capstone-409ff",
    "databaseURL": "https://capstone-409ff-default-rtdb.firebaseio.com/",
    "storageBucket": "project-1027702175882"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def setAlarm(num):
    db.child("alarm").set(num)


def sos():
    db.child("sos").set(1)


def checkAlarm():
    return db.child("alarm").get().val()