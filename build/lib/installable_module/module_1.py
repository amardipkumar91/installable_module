import os
import boto3
class FileReader(object):
    def __init__(self, folder_path):
        self.folder_path = folder_path
    
    def no_of_files(self, all_file = []):
        for rootdir, dirs, files in os.walk(self.folder_path):
            for file in files:
                all_file.append(os.path.join(rootdir, file))
        return all_file
            
class S3Upload(object):
    def __init__(self):
        self.aws_access_key_id = 'AKIAZLOARO24OJV6244S'
        self.aws_secret_access_key = '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'
        self.bucket_name = 'new-image-upload'
    
    def s3_connnect(self):
        return boto3.client(
            's3',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key
        )
    def get_bucket_listing(self):
        response = self.s3_connnect().list_objects_v2(Bucket=self.bucket_name)
        if 'Contents' in response:
            for obj in response['Contents']:
                print(f"File: {obj['Key']} - Size: {obj['Size']} bytes")
        else:
            print("The bucket is empty or does not exist.")
    
    def upload_files(self, files):
        status = True
        for file in files:
            try:
                s3_object_name = os.path.basename(file)
                self.s3_connnect().upload_file(file, self.bucket_name, s3_object_name)
            except Exception as e:
                status = False
                break
        if status:
            return "Success"
        else:
            return "Failed"


def foo():
    return 10

if __name__ == '__main__':
    root_dir = '/Users/amardip.kumar/Documents/PracticePython2/installable_module/installable_module/media_dir/'
    obj = FileReader(root_dir)
    all_files = obj.no_of_files()
    s3_obj = S3Upload()
    status = s3_obj.upload_files(all_files)
    print (status)
    
