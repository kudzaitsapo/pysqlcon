from setuptools import setup, find_packages
 
setup(name='',
      version='0.4',
      url='https://github.com/kudzaitsapo/pysqlcon',
      license='MIT',
      install_requires=[
        'pyodbc>=0.4.26'
    ],
      author='Kudzai Tsapo',
      author_email='kudzai@charteredsys.com',
      description='Easy execution of sql statements and stored procedures on MSSQL database',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md').read(),
      zip_safe=False)