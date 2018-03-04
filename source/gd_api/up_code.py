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

#function to create our folder, to have stability within a users gdrives
def create_folder():
    drive = client_auth()
    folder_metadata = {'title' : 'CalData', 'mimeType' : 'application/vnd.google-apps.folder'}
    folder = drive.CreateFile(folder_metadata)
    folder.Upload()

#creates our .json file for our task data
def create_db():
    drive = client_auth()
    data = drive.CreateFile({'title': 'task_db.json'})
    data.Upload()
    return data['id'] # this is how you access file id
    
def find_db(file_id): # this function finds if the file exists by search via ID
    drive = client_auth()
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    status = False

    for file1 in file_list:
        #print('title: %s, id: %s' % (file1['title'], file1['id']))
        if file1['id'] ==file_id:
            status = True
    
    return status
    
    #need to find our db file by its gdrive ID


def main():
    db_file = create_db()
    create_folder()
    status = find_db(db_file) #pass in the id string of the file to search for it
    print(db_file)
    print(status)

if __name__ == '__main__':
    main()