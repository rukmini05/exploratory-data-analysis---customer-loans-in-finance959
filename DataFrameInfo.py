import pandas as pd

class DataFrameInfo:
    def __init__(self, dataframe):
        self.dataframe = dataframe
    
    def describe_columns(self):
        """Describe all columns in the DataFrame to check their data types."""
        return self.dataframe.dtypes

    def extract_statistics(self,statistical_columns):
        """Extract statistical values: median, standard deviation and mean from the columns and the DataFrame."""
        for column in statistical_columns:

            column_mean=dataframe[column].mean()
            #print(f'mean',column_mean)
            column_median=dataframe[column].median()
            column_std=dataframe[column].std()
            #print(f'std',column_std)

        return column_mean,column_median,column_std

    def count_distinct_values(self):
        """Count distinct values in categorical columns."""
        categorical_columns = self.dataframe.select_dtypes(include=['category', 'object']).columns
        distinct_counts = {col: self.dataframe[col].nunique() for col in categorical_columns}
        return distinct_counts

    def dataframe_shape(self):
        """Print out the shape of the DataFrame."""
        return self.dataframe.shape

    def null_value_counts(self):
        """Generate a count/percentage count of NULL values in each column."""
        null_counts = self.dataframe.isnull().sum()
        null_percentages = (self.dataframe.isnull().mean() * 100).round(2)
        return pd.DataFrame({'null_counts': null_counts, 'null_percentages': null_percentages})

    def head(self, n=5):
        """Return the first n rows of the DataFrame."""
        return self.dataframe.head(n)

    def tail(self, n=5):
        """Return the last n rows of the DataFrame."""
        return self.dataframe.tail(n)



if __name__=="__main__":

    dataframe=pd.read_csv("loan_payments.csv")
    #df=dataframe.copy()
    #print(df.dtypes)
    stastical_columns=dataframe.select_dtypes(include=['float64']).columns
    print(stastical_columns)
    object=DataFrameInfo(dataframe)
    object.extract_statistics(stastical_columns) 
    object.count_distinct_values()
    print(object.null_value_counts())
    print(object.dataframe_shape())
    print(object.head())
    object.tail()