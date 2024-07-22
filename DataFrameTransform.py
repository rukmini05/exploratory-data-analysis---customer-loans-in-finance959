import pandas as pd

class DataFrameTransform:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def check_missing_values(self):
        #print('percentage of null values in each column:')
        dataframe.isnull().sum()/len(dataframe)
        #return self.dataframe.isnull().sum()
            
    def drop_columns_with_nulls_threshold(self, threshold=0.5):
        # Drop columns where the percentage of NULL values exceeds the threshold
        null_percentage = self.dataframe.isnull().mean()
        columns_to_drop = null_percentage[null_percentage > threshold].index
        self.dataframe.drop(columns=columns_to_drop, inplace=True)
        #DataFrame.drop(column_name, axis=1, inplace=True)
        return self.dataframe
    
    def drop_column_null(self,column_name):
        self.dataframe.drop(column_name, inplace=True)
        return self.dataframe
    
    def remove_null_rows(self,column_name):
        self.dataframe.dropna(column_name, inplace=True)
        return self.dataframe
        
    def fill_median(self, DataFrame, column_name):
        DataFrame[column_name]=DataFrame[column_name].fillna(DataFrame[column_name].median())
        return DataFrame
    
    def fill_mean(self, DataFrame, column_name):
        DataFrame[column_name]=DataFrame[column_name].fillna(DataFrame[column_name].mean())
        return DataFrame
    
    def fill_small_value(self, DataFrame, column_name):
        dataframe[column_name].astype('string')
        DataFrame[column_name]=DataFrame[column_name].fillna(DataFrame[column_name].nsmallest)
        return DataFrame
    
    def fill_small_value_for_date(self, DataFrame, column_name):
        #pd.to_datetime(self.dataframe[column_name],errors='coerce')
        DataFrame[column_name]=DataFrame[column_name].fillna(DataFrame[column_name].nsmallest)
        return DataFrame
    

if __name__=="__main__":

    dataframe=pd.read_csv("loan_payments.csv")
    object=DataFrameTransform(dataframe)

    #remove_column_list=['mths_since_last_delinq','mths_since_last_record','mths_since_last_major_derog']
    impute_column_list=['funded_amount','int_rate']
    date_column=['issue_date','last_payment_date','last_credit_pull_date']
    string_columns=['term','employment_length']

    object.check_missing_values()
    object.drop_columns_with_nulls_threshold()
    #object.drop_column_null(remove_column_list)
    object.fill_median(dataframe,impute_column_list)
    object.fill_small_value(dataframe,string_columns)
    object.fill_small_value_for_date(dataframe,date_column)
    
    
    



    

