import json
import csv
import boto3


def lambda_handler(event, context):
    region = 'us-east-1'
    record_list = []

    try:
        s3 = boto3.client('s3')
        dynamodb = boto3.client('dynamodb',region_name=region)

        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        # print('bucket:', bucket, ' Key :', key)

        csv_file = s3.get_object(Bucket=bucket,Key=key)
        record_list = csv_file['Body'].read().decode('utf-8').split('\n')
        csv_reader = csv.reader(record_list, delimiter=',', quotechar='"')

        for row in csv_reader:
            student_id = row[0]
            student_fname = row[1]
            student_lname = row[2]
            student_dob = row[3]
            student_sex = row[4]
            student_form = row[5]
            student_year = row[6]
            student_email = row[7]
            student_grade = row[8]
            
            add_to_db = dynamodb.put_item(
                TableName = 'students',
                Item = {
                    'student_id' : {'S':str(student_id)},
                    'student_fname' : {'S':str(student_fname)},
                    'student_lname' : {'S':str(student_lname)},
                    'student_dob' : {'S':str(student_dob)},
                    'student_sex' : {'S':str(student_sex)},
                    'student_form' : {'S':str(student_form)},
                    'student_year' : {'S':str(student_year)},
                    'student_email' : {'S':str(student_email)},
                    'student_grade' : {'S':str(student_grade)},
                })
        # rows in csv are split by lines
            print('sucessfully added the records to the dynamodb table')
    except Exception as e:
            print(str(e))
    return {
        'statusCode': 200,
        'body': json.dumps('CSV to DynamoDB Success')
    }
