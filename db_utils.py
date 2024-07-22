
import yaml;
from sqlalchemy import create_engine;
import pandas as pd


class RDSDatabaseConnector():
    
    def __init__(self, filename):

        self.filename = filename # when class is initiated it requires the credentials argument.

    def extract_credentials(self):
   
        with open(self.filename, 'r') as file:
            return yaml.safe_load(file)
    
    # Initialises SQLAlchemy engine.
    def connect(self,read_credentials):
        
        connection_string = f'postgresql://{read_credentials["RDS_USER"]}:{read_credentials["RDS_PASSWORD"]}@{read_credentials["RDS_HOST"]}:{read_credentials["RDS_PORT"]}/{read_credentials["RDS_DATABASE"]}'
        engine = create_engine(connection_string)
        return engine
    
    def extract_data(self,tablename,engine):
        
        return pd.read_sql_table(tablename,engine)
           

if __name__=="__main__":
    credentials="credentials.yaml"
    connector = RDSDatabaseConnector(credentials)
    credentials_dict = connector.extract_credentials()
    print (credentials_dict)
    engine=connector.connect(credentials_dict)
    print(engine)
    df=connector.extract_data("loan_payments",engine)
    #print(df)
    df.to_csv("loan_payments.csv", encoding= 'utf-8', index= False)

    print(df.head(5))
    #print (df.duplicated)  