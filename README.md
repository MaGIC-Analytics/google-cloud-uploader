# google-cloud-uploader
This repository is for the tools to manage data between a local server and Google Cloud Storage. 
Primarily this has been set up and structured for storing of Genomics sequencing data from the Rutgers Genomics Center

# Setup
You first need to set up your authentication through a service account. You could set this up automatically for your machine, I opted for use of a credentials file for flexibility. You can generate one through the GCP console as [detailed here](https://cloud.google.com/iam/docs/service-accounts). Double check that the service account you've set up includes the appropriate cloud storage permissions. Since this is for archiving data, a big aspect for me is severely restricting (or omitting) delete permissions. 

From there we have a local server with a local directory called "GENOMICS_DATA_ARCHIVE". Within that directory we have everything organized according to our [SOPs](https://github.com/RU-MaGIC/Operating_procedures/blob/master/workflow_procedures/Cloud_archive.md). 

# Execution
## Upload
Upload will take your local directory and upload it with the associated directory structure as blob prefixes. To upload:
'''
upload(dir_start=os.path.abspath('/path/to/GENOMICS_DATA_ARCHIVE'))
'''

## Download
Download is structured for picking a select blob prefix on GCP and downloading it to a local directory of choice. This will also strip off the prefix when downloading. 
You must define your bucket name and prefix path, as well as local target. 
'''
bucket_name='bucket-name'
prefix_path='investigator_name/project_folder/'
download(bucket_name, prefix_path, '/path/to/local_dir/')
'''

# Use cases
## Automate upload
This is the more common use for this. As we have it set up, we manually perform demultiplexing and validation of samples. This also allows an easy stop gap for investigators to pick up raw data before we purge. The FASTQs then get deposited in to our directory for upload. We then use a local cronjob (or similar) to automatically perform uploads on a regular basis. 

## Download links
You can also create signed URLs for each of the objects. This can be useful if you need to send links to collaborators etc. 