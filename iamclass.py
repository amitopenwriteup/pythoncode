import boto3
from botocore.exceptions import ClientError, ParamValidationError

class IAMUserManager:
    def __init__(self):
        # Initialize the IAM client
        self.iam = boto3.client('iam')

    def create_user(self, username):
        try:
            # Create IAM user
            user = self.iam.create_user(UserName=username)
            print(f"Created user: {user}")
        
        except self.iam.exceptions.EntityAlreadyExistsException:
            print(f"User {username} already exists.")
        
        except ParamValidationError as e:
            print(f"Parameter validation error: {e}")
        
        except ClientError as e:
            print(f"Unexpected error: {e}")

# Example usage
if __name__ == "__main__":
    iam_manager = IAMUserManager()  # Instantiate the IAMUserManager class
    iam_manager.create_user('fred')  # Create user 'fred'

