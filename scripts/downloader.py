from google.cloud import storage
import md5_check

#download_blob('name', 'source_blob','destination_file_path')

def download_blob(bucket_name, source_blob_name, destination_file_name, credentials):
    storage_client = storage.Client.from_service_account_json(credentials)
    bucket = storage_client.bucket(bucket_name)
    blob=bucket.blob(source_blob_name)

    blob.download_to_filename(destination_file_name)
    print(
        "File {} downloaded to {}.".format(
         source_blob_name, destination_file_name
      )
    )
    blob_check = bucket.get_blob(source_blob_name)
    blob_md5 = blob_check.md5_hash
    destination_md5=md5_check.md5_file(destination_file_name)

    assert (blob_md5==destination_md5),'MD5 checksums do not match!!'
    print("MD5 checksums match for {}.".format(destination_file_name))
