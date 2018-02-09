from setuptools import setup

setup(name='pingwatcher',
      version='0.1',
      description='simple latency grapher',
      url='http://github.com/blah',
      author='Matt Poepping',
      author_email='matt.poepping@gmail.com',
      license='MIT',
      install_requires=['multiping','rrdtool','statsd'],
      scripts=['pingwatcher']
      )
