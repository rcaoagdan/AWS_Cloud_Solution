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
import logging
from botocore.exceptions import ClientError

##############################################################################
# Global Variables                                                           #
##############################################################################
s3 = boto3.client('s3')
buckets_found = s3.list_buckets()
##############################################################################
# Functions                                                                  #
##############################################################################
def list_buckets():
    print('known buckets')
    for bucket in buckets_found:
        print(f' {bucket["Name"]}')

##############################################################################
# Global Variables                                                           #
##############################################################################
list_buckets()
