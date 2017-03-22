from setuptools import setup

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
