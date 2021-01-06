import sys, glob, os
sys.path.append('./scripts/')

import uploader, downloader, bucket_management

#store credentials in local dir in .json format
credentials=glob.glob('./*.json')[0]

def upload(dir_start):
    for dirpath, dirnames, filenames in os.walk(dir_start, topdown=True):
        for f in filenames:
            sname=os.path.join(dirpath,f) #source name
            gname=sname.split('GENOMICS_DATA_ARCHIVE')[1].lstrip('/') #google blob name
            
            status=uploader.upload_blob('genomics-data-archive',sname, gname, credentials)
            #Once the file has been uploaded it should be removed from local
            if status==True:
                print('Success up')
                os.remove(os.path.join(dirpath, f))

def download(target_bucket, prefix_path, down_dir):
    blobs=bucket_management.list_items_in_subbucket(target_bucket, prefix_path, credentials) #Get all the blobs in the bucket with prefix of choice
    for blob in blobs:
        down_name=blob.name.lstrip(str(prefix_path)) #Strips out the prefix from the blob name for a targeted drop
        down_path='/'.join(down_name.split('/')[:-1]) #Builds the path of directories that would be needed from the blob object
        try:
            os.makedirs(os.path.join(down_dir, down_path)) #If the directory doesnt exist then this will make it
        except:
            pass #And if its there it will throw and error but then pass
        downloader.download_blob(target_bucket, blob.name, os.path.join(down_dir, down_name), credentials)