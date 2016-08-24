# coding=utf-8
import os
import shutil
import json

basedir = os.path.dirname(os.path.abspath(__file__))
zmirror_dir = os.path.abspath(os.path.join(basedir, '..'))


def zmirror_file(filename):
    return os.path.join(zmirror_dir, filename)


def copy_default_config_file():
    if os.path.exists(zmirror_file('config.py')):
        print('[Waring] the config.py already exists, it would be temporary renamed to config.py._unittest_raw')
        shutil.move(zmirror_file('config.py'), zmirror_file('config.py._unittest_raw'))

    if os.path.exists(zmirror_file('custom_func.py')):
        print('[Waring] the custom_func.py already exists, it would be temporary renamed to custom_func.py._unittest_raw')
        shutil.move(zmirror_file('custom_func.py'), zmirror_file('custom_func.py._unittest_raw'))

    shutil.copy(zmirror_file('config_default.py'), zmirror_file('config.py'))
    shutil.copy(zmirror_file('custom_func.sample.py'), zmirror_file('custom_func.py'))

    # 下面是flask的一个trick, 强行生成多个不同的flask app 对象
    # with open(zmirror_file('config.py'), 'a', encoding='utf-8') as fp:
    #     fp.write('\n')
    #     fp.write('import random\n')
    #     fp.write('from flask import Flask\n')
    #     fp.write("unittest_app = Flask('unittest' + str(random.random()).replace('.', ''))\n")


def restore_config_file():
    os.remove(zmirror_file('config.py'))
    os.remove(zmirror_file('custom_func.py'))
    if os.path.exists(zmirror_file('config.py._unittest_raw')):
        shutil.move(zmirror_file('config.py._unittest_raw'), zmirror_file('config.py'))
    if os.path.exists(zmirror_file('custom_func.py._unittest_raw')):
        shutil.move(zmirror_file('custom_func.py._unittest_raw'), zmirror_file('custom_func.py'))


def env(ip="1.2.3.4", **kwargs):
    """
    :rtype: dict
    """
    result = {"REMOTE_ADDR": ip}
    result.update(kwargs)
    return result


DEFAULT_USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"


def headers(
        accept_encoding="gzip, deflate",
        user_agent=DEFAULT_USER_AGENT,
        **kwargs
):
    """
    :rtype: dict
    """
    result = {"accept-encoding": accept_encoding,
              "user-agent": user_agent}
    result.update(kwargs)
    return result


def load_rv_json(rv):
    """

    :type rv: Response
    :rtype: dict
    """
    return json.loads(rv.data.decode(encoding='utf-8'))