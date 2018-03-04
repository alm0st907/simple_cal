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

#function to check for a file by its id
#this function only searches the root directory   
def find_db(file_id): # this function finds if the file exists by search via ID
    drive = client_auth()
    file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()

    status = False

    for file1 in file_list:
        print('title: %s, id: %s' % (file1['title'], file1['id']))
        if file1['id'] ==file_id:
            status = True
    
    return status
    
    #need to find our db file by its gdrive ID

#function creates a file within the folder specified by that hardcoded id
#change this to be dynamic later
def db_to_folder():
    drive = client_auth()
    file1 = drive.CreateFile({'title':'dummy.json', 'mimeType':'text/csv',
        "parents": [{"kind": "drive#fileLink","id": "1tbNBs1ZdWNOUB1lqWaryQABNyBDFNc-F"}]})
    file1.Upload()

#function to list what is in a folder
#ListFolder("root") will print root of the gdrive, and you can find our subdirectory within
#ListFolder("subdirectory file id") will find us the db file ID
def ListFolder(parent):
    drive = client_auth()
    filelist=[]
    file_list = drive.ListFile({'q': "'%s' in parents and trashed=false" % parent}).GetList()
    for f in file_list:
        if f['mimeType']=='application/vnd.google-apps.folder': # if folder
            filelist.append({"id":f['id'],"title":f['title'],"list":ListFolder(f['id'])})
        else:
            filelist.append({"id":f['id'],"title":f['title'],"title1":f['alternateLink']})
    return filelist

#NEED TO GET THE DB FILE ID BEFORE USING THIS IN SHIPPABLE
#function to update db file within subfolder, given the id of the file
def update_db():
    drive = client_auth()
    id = '1y1dsETkLA9M76gFpNMByfjlEhiJRd-ql'
    a=drive.auth.service.files().get(fileId=id).execute()
    a['title']="db.json"
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
def download_db(file_id):
    drive = client_auth()
    download_file = drive.CreateFile({'id': file_id})
    download_file.GetContentFile("task_db.json")

def main():
    #db_file = create_db()
    #create_folder()
    status = find_db("1-C3WrNfvt4aW1WM7PDBYyGbpQ_93CUDt") #pass in the id string of the file to search for it
    #print(db_file)
    print(status)
    #db_to_folder()
    #test_file_update()

    #getting all the file id's within the the directory we specifify to search
    test_list =ListFolder("1tbNBs1ZdWNOUB1lqWaryQABNyBDFNc-F")
    for lists in test_list:
        print(lists["id"])
    update_db()
    download_db('1y1dsETkLA9M76gFpNMByfjlEhiJRd-ql')
if __name__ == '__main__':
    main()