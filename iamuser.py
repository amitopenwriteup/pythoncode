import boto3
from botocore.exceptions import ClientError, ParamValidationError

try:
    iam = boto3.client('iam')
    user = iam.create_user(UserName='fred')
    print("Created user: %s" % user)
except iam.exceptions.EntityAlreadyExistsException:
    print("User already exists")
except ParamValidationError as e:
    print("Parameter validation error: %s" % e)
except ClientError as e:
    print("Unexpected error: %s" % e)

