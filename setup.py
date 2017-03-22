from setuptools import setup


def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='permutive-sdk',
      version='0.1',
      description='Python wrapper for Permutive API',
      url='http://github.com/tailsdotcom/permutive-sdk',
      author='Dinesh Vitharanage',
      author_email='dinesh@tails.com',
      license='MIT',
      packages=['permutive'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
