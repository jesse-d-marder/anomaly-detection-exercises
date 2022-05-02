import pandas as pd
import os
from env import get_db_url

def acquire():
    
    filename = 'curriculum.csv'
    
    if os.path.exists(filename):
        
        return pd.read_csv(filename)
    
    else:
        query = """SELECT * FROM logs LEFT JOIN cohorts ON logs.user_id = cohorts.id"""
        df = pd.read_sql(query, get_db_url('curriculum_logs'))
        
        df.to_csv(filename, index=False)
        
        return df