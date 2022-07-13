from daka import dakarun,mainrun
from dakaCheck import checkResult
import logging
logging.basicConfig(filename='/home/daka/record/log', level=logging.INFO,format='%(asctime)s %(message)s')



def main():
    ####
    # write your id and password here
    ####
    f = mainrun('YourID','YourPassword')
    if not f:
        message = 'YourID is done\n'
        logging.info(message)
        return


if __name__ == '__main__':
    main()


