import json
import boto3
import os
 
def lambda_handler(event, context):
    message = event["message"]
    topic_arn = None
    substring = event["substring"]
    sns_client = boto3.client('sns')
    response = sns_client.list_topics()
    for topic in response['Topics']:
        print(topic['TopicArn'])
        if substring in topic['TopicArn']:
            topic_arn = topic['TopicArn']
    if(topic_arn == None):
        print('Topic not found')
        return {
            'statusCode': 200,
            'body': json.dumps('Topic not found!')
        }
    else:
        print('Topic found',topic_arn)
        response = sns_client.publish(
        TopicArn=topic_arn,
        Message=message,
        Subject='Sales Performance'
        )
        # TODO implement
        return {
            'statusCode': 200,
            'body': json.dumps('Email sent successfully!')
        }