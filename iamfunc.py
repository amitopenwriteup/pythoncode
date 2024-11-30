import boto3
from botocore.exceptions import ClientError, ParamValidationError

def create_iam_user(username):
    try:
        # Create IAM client
        iam = boto3.client('iam')
        
        # Create user
        user = iam.create_user(UserName=username)
        print("Created user: %s" % user)
        
    except iam.exceptions.EntityAlreadyExistsException:
        print(f"User {username} already exists")
    except ParamValidationError as e:
        print(f"Parameter validation error: {e}")
    except ClientError as e:
        print(f"Unexpected error: {e}")
