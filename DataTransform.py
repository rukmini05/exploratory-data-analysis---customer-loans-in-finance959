import pandas as pd


class DataTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def convert_string_columns(self,string_columns):
        for column in string_columns:
            
            self.dataframe[column] = self.dataframe[column].astype('string')

        return self.dataframe

    def convert_date_columns(self,date_columns):
        for column in date_columns:
            
            self.dataframe[column] = pd.to_datetime(self.dataframe[column],format='%Y%m%d',errors='coerce')
            #self.dataframe[column] = pd.to_datetime(self.dataframe[column],format='%b%Y',errors='coerce')
            #self.dataframe[column] = pd.to_datetime(self.dataframe[column],format=None,errors='coerce')
            #self.dataframe[column] =pd.to_datetime(dataframe[column].dt.strftime('%m-%Y'))
    
        
        return self.dataframe
    
    def convert_to_categorical(self, categorial_column_name):
        """Convert column to categorical."""
        self.dataframe[categorial_column_name] = self.dataframe[categorial_column_name].astype('category')

        return self.dataframe
    
if __name__=="__main__":

    dataframe=pd.read_csv("loan_payments.csv")
    object=DataTransform(dataframe)
    numeric_columns=['']
    string_columns=['term','grade','sub_grade','employment_length','home_ownership','verification_status','loan_status','payment_plan','purpose','earliest_credit_line','application_type']
    date_columns=['issue_date','last_payment_date','next_payment_date','last_credit_pull_date']
    categorial_column_name=['loan_status']
    object.convert_string_columns(string_columns)
    object.convert_date_columns(date_columns)
    object.convert_to_categorical(categorial_column_name)
    print(dataframe.dtypes)
    
   
    