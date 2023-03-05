#!/bin/bash


###################

# Author: latesh 
# date: 05/03/2023
#
# version: draft version
#
# This script will help in report the AWS resource usage
###################

set -x

# AWS s3
# AWS EC2 
# AWS lambda
# AWS IAM USER


# list s3 bucket
echo "print list of s3 bucket"
aws s3 ls > resourceTracker

# list EC2 buckets
echo "print list of ec2 bucket"
aws ec2 describe-instances  | jq '.Reservations[].Instances[].InstanceID'

# list lambda
echo "print list of lambda function"
aws lambda list-functions >> resourceTracker:q!

# list IAM users
echo "print list of IAM usres"
aws iam list-users
