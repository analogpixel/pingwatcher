from setuptools import setup

setup(name='pingwatcher',
      version='0.1',
      description='simple latency grapher',
      url='https://github.com/analogpixel/pingwatcher',
      author='Matt Poepping',
      author_email='matt.poepping@gmail.com',
      license='MIT',
      install_requires=['multiping','rrdtool','statsd'],
      scripts=['pingwatcher']
      )
