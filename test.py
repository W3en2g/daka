import logging
logging.basicConfig(filename='/home/daka/record/log', level=logging.INFO,format='%(asctime)s %(message)s')
user = "asdfasdf"
message = user +" is done"
logging.info(message)
logging.warning(" try again now")
