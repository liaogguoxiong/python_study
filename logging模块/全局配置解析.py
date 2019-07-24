'''
@author: lgx
@Email:297979949@qq.com
@project: python_study
@file: 全局配置解析.py
@time: 2019-07-04 9:33
@desc:
'''

import logging

logging.basicConfig(level=logging.INFO,filename='out.log',datefmt="%Y-%m-%d %H:%M:%S",
                    format='%(asctime)s - %(name)s - %(levelname)s - %(lineno)d - %(module)s - %(message)s')

logger=logging.getLogger(__name__)

logger.info('hello,world')

