"""
@author: Kudzai Tsapo (kudzai@charteredsys.com)

Description
-----------
File for testing methods implemented in the library

"""
from models import PySQLCon
from models import Table, Column, Query


table = Table('Users', [
    Column('id', 'int', 'NOT NULL PRIMARY KEY IDENTITY(1,1)'),
    Column('firstname', 'nvarchar(50)', 'NOT NULL'),
    Column('surname', 'nvarchar(50)', 'NOT NULL')
])

