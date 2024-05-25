import logging

logger = logging.getLogger(__name__)

file_h = logging.FileHandler('example.log')
file_h_info = logging.FileHandler('example_info.log')
stream_h = logging.StreamHandler()


file_f = logging.Formatter('%(asctime)s--%(levelname)s>%(levelno)s< :::%(message)s')
stream_f = logging.Formatter('%(levelname)s//%(message)s')
stream_f_info = logging.Formatter('%(message)s')

file_h.setFormatter(file_f)
stream_h.setFormatter(stream_f)
file_h_info.setFormatter(stream_f_info)


file_h.setLevel(logging.ERROR)
stream_h.setLevel(logging.WARNING)
file_h_info.setLevel(logging.INFO)


logger.addHandler(stream_h)
logger.addHandler(file_h)
logger.addHandler(file_h_info)

logger.setLevel(logging.INFO)

logger.error('oh no this is err')
logger.info('oh yes this is info')
logger.warning('oh yes this is warning')