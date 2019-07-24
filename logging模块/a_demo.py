'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: a_demo.py
@time: 2019-07-03 16:26
@desc:
'''

import logging

#全局配置
logging.basicConfig(level=logging.DEBUG,format='%(asctime)s-[%(name)s]-[%(levelname)s]>>%(message)s')

logger=logging.getLogger(__name__)

logger.info("it is info")
logger.debug("it is debug")
logger.warning("it is warning")
logger.info("end")
