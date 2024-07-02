import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import scipy.stats as st
import matplotlib.pyplot as plt
import warnings
import statsmodels.api as sm

warnings.filterwarnings('ignore')

class TaxiDataAnalysis:
    def __init__(self, filepath):
        self.filepath = filepath
        self.df = None
        self.filtered_df = None
    
    def load_data(self):
        self.df = pd.read_csv(self.filepath)
        self.df['tpep_pickup_datetime'] = pd.to_datetime(self.df['tpep_pickup_datetime'])
        self.df['tpep_dropoff_datetime'] = pd.to_datetime(self.df['tpep_dropoff_datetime'])
        self.df['duration'] = (self.df['tpep_dropoff_datetime'] - self.df['tpep_pickup_datetime']).dt.total_seconds() / 60
    
    def filter_data(self):
        self.filtered_df = self.df[['passenger_count', 'payment_type', 'fare_amount', 'trip_distance', 'duration']]
        self.filtered_df['passenger_count'] = self.filtered_df['passenger_count'].astype('int64')
        self.filtered_df['payment_type'] = self.filtered_df['payment_type'].astype('int64')
        self.filtered_df.drop_duplicates(inplace=True)
    
    def get_payment_type_distribution(self):
        return self.filtered_df['payment_type'].value_counts(normalize=True)

    def run_analysis(self):
        self.load_data()
        self.filter_data()
        payment_distribution = self.get_payment_type_distribution()
        return payment_distribution

class AnomalyDetection:
    def __init__(self, df):
        self.df = df
    
    def preprocess_data(self):
        # Filter for cash and card payments
        self.df = self.df[self.df['payment_type'] < 3]
        
        # Filter for passenger counts between 1 and 6
        self.df = self.df[(self.df['passenger_count'] > 0) & (self.df['passenger_count'] <= 6)]
        
        # Replace payment types with labels
        self.df['payment_type'].replace([1, 2], ['Card', 'Cash'], inplace=True)
        
        # Filter for positive fare amount, trip distance, and duration
        self.df = self.df[self.df['fare_amount'] > 0]
        self.df = self.df[self.df['trip_distance'] > 0]
        self.df = self.df[self.df['duration'] > 0]
    
    def plot_boxplot(self, column):
        plt.boxplot(self.df[column])
        plt.title(f'Boxplot of {column}')
        plt.show()
    
    def remove_outliers(self):
        for col in ['fare_amount', 'trip_distance', 'duration']:
            q1 = self.df[col].quantile(0.25)
            q3 = self.df[col].quantile(0.75)
            IQR = q3 - q1

            lower_bound = q1 - 1.5 * IQR
            upper_bound = q3 + 1.5 * IQR

            self.df = self.df[(self.df[col] >= lower_bound) & (self.df[col] <= upper_bound)]
    
    def get_cleaned_data(self):
        self.preprocess_data()
        for col in ['fare_amount', 'trip_distance', 'duration']:
            self.plot_boxplot(col)
        self.remove_outliers()
        return self.df

# Example usage:
analysis = TaxiDataAnalysis('C:/Users/akamma1/Videos/maximizing_revenue/data/yellow_tripdata_2020-01.csv')
analysis.run_analysis()

anomaly_detector = AnomalyDetection(analysis.filtered_df)
cleaned_df = anomaly_detector.get_cleaned_data()
print(cleaned_df.head())
