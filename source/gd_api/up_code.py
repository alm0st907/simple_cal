from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def client_auth():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    drive = GoogleDrive(gauth)
    return drive

def create_db():
    drive = client_auth()
    data = drive.CreateFile({'title': 'task_db.json'})
    data.Upload()
    


def main():
    create_db()

if __name__ == '__main__':
    main()