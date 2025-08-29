

````markdown
# AWS Boto3 & Python Practice

This repository contains Python scripts and examples for learning **AWS Boto3 SDK** along with basic Python programming concepts.  
It includes IAM examples, math functions, collections, and setup steps for using Boto3 with AWS.  

---

## 📂 Repository Structure

- **classtest.py** – Example Python class usage  
- **dictionary, list, set, tuple** – Examples of Python collections  
- **firstcode.py, secondcode.py** – Beginner Python scripts  
- **functionmax.py, functiontext** – Function examples in Python  
- **iamclass.py, iamfunc.py, iamuser.py** – IAM (Identity & Access Management) examples with Boto3  
- **installboto, setupaws, virtualenv** – Setup instructions for using AWS SDK  
- **samplecodeboto.py** – Sample Boto3 script for AWS resource interaction  
- **mathdir.py, mathsin.py** – Math function examples in Python  
- **boto3.pptx** – Slides on Boto3 concepts  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/amitopenwriteup/amitopenwriteup.git
cd amitopenwriteup
````

### 2️⃣ Setup Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
```

### 3️⃣ Install Dependencies

```bash
pip install boto3
```

### 4️⃣ Configure AWS Credentials

Make sure AWS CLI is installed and configured:

```bash
aws configure
```

---

## 📌 Example: Create IAM User with Boto3

```python
import boto3

iam = boto3.client('iam')

response = iam.create_user(
    UserName='test-user'
)

print("Created IAM User:", response['User']['UserName'])
```

---

## 🎯 Learning Goals

* Practice Python basics (functions, loops, classes, collections)
* Learn how to use **Boto3** for AWS services like IAM, S3, etc.
* Understand environment setup (virtualenv + boto3 installation)

---

## 📖 References

* [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
* [AWS IAM Documentation](https://docs.aws.amazon.com/iam/)
* [Python Official Docs](https://docs.python.org/3/)

---

## 👤 Author

**Amit Maheshwari**
📧 [amit@openwriteup.com](mailto:amit@openwriteup.com)

```

---

