from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


def client_auth():
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile("user.txt") #try to load credentials for gdrive

    if gauth.credentials is None:
        #we need to get them if they arent able to be loaded
        gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.
    elif gauth.access_token_expired:
        gauth.Refresh()
        #refresh the creds if necessary
    else:
        gauth.Authorize()
        #using saved credentials and moving on
    gauth.SaveCredentialsFile("user.txt")
    #this saves our credentials so we dont pop the webpage every opening

    drive = GoogleDrive(gauth)

    return drive #return usable list file

def create_db():
    drive = client_auth()
    data = drive.CreateFile({'title': 'task_db.json'})
    data.Upload()
    


def main():
    create_db()

if __name__ == '__main__':
    main()