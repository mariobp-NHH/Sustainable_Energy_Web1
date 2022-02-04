# -*- coding: utf-8 -*-
"""
Created on Sun Jan 30 21:59:00 2022

@author: gabri
"""

from sqlalchemy import create_engine
import pandas as pd

class testdf():
   def __init__(self,table,DBURI):
       engine_local =create_engine(DBURI)
       
       df_in=pd.read_sql("SELECT * FROM {}".format(table),engine_local) 
       self.test_val=df_in.shape[0]
       
       if self.test_val==0:
           self.test_bin=False
       else:
           self.test_bin=True
        
       engine_local.dispose()  