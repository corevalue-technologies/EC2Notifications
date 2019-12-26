import json
import logging
import os




logger = logging.getLogger()
//you can change the logging level as per your comfort
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    logger.info("Event: " + str(event))
    
