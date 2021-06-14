import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)


        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = '77schEZ44oEAAAAAAAAAAdwGTV8uJFuG8qrqX47Wasl4cfd0PyFMRvWY99N-zUs7'
    transferData = TransferData(access_token)

    file_from = "C:/Users/DELL/Desktop/python project/cloud_storage-master/cloud_storage-master/cloud_storage-master/sample.txt"
    file_to = "/game4/test3.txt" # This is the full path to upload the file to, including name that you wish the file to be called once uploaded.

    # API v2
    transferData.upload_file(file_from, file_to)
    print("file has been moved !!!")


main()
