import logging
from saveresult import BASIC_FILE
import time



# logger1=logging.getLogger('logger1')
# logger12=logging.getLogger('logger1.logger2')
# logger1.setLevel(logging.WARNING)
# logger12.setLevel(logging.DEBUG)
#
# ch=logging.FileHandler(BASIC_FILE+'/test.log')
#
# # logger1.log(msg='hello')
# logger1.addHandler(ch)
# logger1.log(level=logging.WARNING,msg='hello')


timea=time.time()*1000
print str(int(timea))