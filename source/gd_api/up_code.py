from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

#this function gets our google drive info/credentials so we can use it
#allows us to return the "drive" so we can upload/download stuff as needed
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
#default name is "CalData"
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
    #the id is returned so ideally we can keep track of this easily
    #probably write it to a file to easily parse in
    #file ID's dont mean too much security wise so its not 

#function to find our db folder
#this function only searches the root directory   
def find_db(): # this function finds if the file exists by search via ID
    drive = client_auth()
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    status = 0 #placeholder for the id

    for file1 in file_list:
        #print('title: %s, id: %s' % (file1['title'], file1['id']))
        if file1['title'] =="CalData":
            status = file1['id'] #ripping the id string
    
    return status
    
    #need to find our db file by its gdrive ID

#function creates a file within the folder specified by that hardcoded id
#change this to be dynamic later
def db_to_folder():
    drive = client_auth()
    folder_id = find_db()
    file1 = drive.CreateFile({'title':'task_db.json', 'mimeType':'text/csv',
        "parents": [{"kind": "drive#fileLink","id": folder_id}]})
    file1.Upload()

#function to list what is in a folder
#should find the db file id so we can use this function and pass it to the update db function
def ListFolder():
    drive = client_auth()
    filelist=[] #list of our files
    folder_id = find_db() #get our folder id
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % folder_id}).GetList()
    
    #iterate through the folder to find all our ids
    for f in file_list:
        if f['mimeType']=='application/vnd.google-apps.folder': # if folder
            filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
        else:
            filelist.append({"id":f['id'],"title":f['title'],"title1":f['alternateLink']})
            
    db_file_id = 0 # temp for the file id
    for files in file_list:
        if files["title"] == "task_db.json":
            db_file_id = files['id']

    return db_file_id

#NEED TO GET THE DB FILE ID BEFORE USING THIS IN SHIPPABLE
#function to update db file within subfolder, given the id of the file
def update_db():
    drive = client_auth()
    id = ListFolder()
    a=drive.auth.service.files().get(fileId=id).execute()
    a['title']="task_db.json"
    file1 = drive.CreateFile({'id': id})
    content = file1.GetContentString()
    #this data allows us to test inserting to the json and updating it
    data = input("test string here:")
    if data == "delete":
        file1.SetContentString("null")
    else:
        file1.SetContentString(content+ data)
    file1.Upload()
   
    update=drive.auth.service.files().update(fileId=id,body=a).execute()

#download file based on file id
def download_db():
    file_id = ListFolder() # finds our database file id within its subfolder
    drive = client_auth()
    download_file = drive.CreateFile({'id': file_id})
    download_file.GetContentFile("task_db.json") #downloading the file, 

def main():
    create_folder()#create the directory
    db_to_folder() #establish our folder and create the db file within
    update_db() #update that db file
    download_db() #download back to houston

if __name__ == '__main__':
    main()