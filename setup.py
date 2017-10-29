from setuptools import setup
setup(
  name = 'guetzli_recursively',
  py_modules=['guetzli_recursively'],
  version = '1.1.0',
  description = 'Script in Python to convert all the jpeg of a folder recursively with Guetzli.',
  author = 'Andros Fenollosa',
  author_email = 'andros@fenollosa.email',
  url = 'https://github.com/tanrax/guetzli-recursively',
  keywords = ['guetzli', 'jpeg', 'recursive'],
  classifiers = [],
  install_requires=[
        'Click>=6.7',
  ],
  entry_points='''
      [console_scripts]
      guetzli_recursively=guetzli_recursively:run
  '''
)
