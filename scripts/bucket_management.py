from google.cloud import storage

#create_bucket('name')
#list_all_buckets()
#bucket_metadata('name')
#list_items_in_bucket('name')
#list_items_in_subbucket('name','path')

def create_bucket(bucket_name, credentials):
    storage_client = storage.Client.from_service_account_json(credentials)

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class='STANDARD'
    new_bucket=storage_client.create_bucket(bucket, location='us')

    print(
        "Created bucket {} in {} with storage class {}".format(
            new_bucket.name, new_bucket.location, new_bucket.storage_class
        )
    )
    return new_bucket

def list_all_buckets(credentials):
    storage_client = storage.Client.from_service_account_json(credentials)
    buckets=storage_client.list_buckets()

    for bucket in buckets:
        print(bucket.name)

def bucket_metadata(bucket_name, credentials):
    storage_client = storage.Client.from_service_account_json(credentials)

    bucket = storage_client.get_bucket(bucket_name)

    print("ID: {}".format(bucket.id))
    print("Name: {}".format(bucket.name))
    print("Storage Class: {}".format(bucket.storage_class))
    print("Location: {}".format(bucket.location))
    print("Location Type: {}".format(bucket.location_type))
    print("Cors: {}".format(bucket.cors))
    print(
        "Default Event Based Hold: {}".format(bucket.default_event_based_hold)
    )
    print("Default KMS Key Name: {}".format(bucket.default_kms_key_name))
    print("Metageneration: {}".format(bucket.metageneration))
    print(
        "Retention Effective Time: {}".format(
            bucket.retention_policy_effective_time
        )
    )
    print("Retention Period: {}".format(bucket.retention_period))
    print("Retention Policy Locked: {}".format(bucket.retention_policy_locked))
    print("Requester Pays: {}".format(bucket.requester_pays))
    print("Self Link: {}".format(bucket.self_link))
    print("Time Created: {}".format(bucket.time_created))
    print("Versioning Enabled: {}".format(bucket.versioning_enabled))
    print("Labels:")
    print(bucket.labels)

def list_items_in_bucket(bucket_name, credentials):
    storage_client = storage.Client.from_service_account_json(credentials)

    blobs = storage_client.list_blobs(bucket_name)
    return blobs

def list_items_in_subbucket(bucket_name, prefix_path, credentials):
    storage_client = storage.Client.from_service_account_json(credentials)

    blobs = storage_client.list_blobs(bucket_name, prefix=prefix_path)
    return blobs


def bucket_size():
    pass
#need to add in gsutil backend for sizing

