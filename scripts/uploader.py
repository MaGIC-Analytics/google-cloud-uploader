from google.cloud import storage
import md5_check

#upload_blob('bucket','source_file','destination_name_path')

def upload_blob(bucket_name, source_file_name, destination_blob_name, credentials):
   storage_client = storage.Client.from_service_account_json(credentials)
   bucket = storage_client.bucket(bucket_name)
   blob = bucket.blob(destination_blob_name)

   blob.upload_from_filename(source_file_name)
   
   print(
      "File {} uploaded to {}.".format(
         source_file_name, destination_blob_name
      )
   )
   blob_check = bucket.get_blob(destination_blob_name)
   blob_md5 = blob_check.md5_hash
   source_md5=md5_check.md5_file(source_file_name)

   if blob_md5==source_md5:
      print("MD5 checksums match for {}.".format(destination_blob_name))
      return True
   else:
      print('MD5 checksums do not match!!')
      return False
   