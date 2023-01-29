import boto3
import logging

sqs = boto3.client('sqs')  #<------SQS resource code

sqs_queue = sqs.create_queue(QueueName='BlackSquad') #<----- Create the queue

print(sqs_queue.url)
print(sqs_queue)