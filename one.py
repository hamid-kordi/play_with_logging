import logging


logging.basicConfig(level=logging.NOTSET,filename='example.log',format='%(levelname)s<<<%(asctime)s--%(created)f---%(levelno)s>%(message)s')

logging.info('به نام خدا عزیزم سلام برنامه داره اجرا میشه ')
logging.error('حاجی ریدی ناموسا')
logging.debug('یه دستی هم به ما بکش .داریم زحمت میکشیم')
logging.warning('یه جای کار میلنگه مشتی')
logging.critical('به فنا رفتیم')
