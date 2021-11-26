import boto3
def lambda_handler(event, context):
    print("This is a lambda function created from Coudformation")
    return "Success"


{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "A template for creating lambda funtion from s3 buckets",
    "Resources": {
        "LambdaFunResource": {
            "Type": "AWS::Lambda::Function",
            "Properties": {
                "FunctionName": "new-lambda-function",
                
                "Code": {
                                "S3Bucket" : "cf-templates-1jzuu4nsixb9a-eu-west-2",
                                "S3Key" : "lambdafunction.zip"
                        },
                "Description": "Used to run job",
                "Handler": "lambdafunction.lambda_handler",
                "Role": "arn:aws:iam::420843361844:role/lambda-role",
                "Runtime": "python3.6",
                "Timeout": 120
            }
        }
  }
}

https://s3.eu-west-2.amazonaws.com/cf-templates-1jzuu4nsixb9a-eu-west-2/2021326aDj-mercy.templatex7nk3422l7