import os
import pandas as pd
from eda import TaxiDataAnalysis, AnomalyDetection
import matplotlib.pyplot as plt

class DataVisualization:
    def __init__(self, df, output_dir='Visualizations'):
        self.df = df
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def plot_fare_and_distance_distribution(self):
        plt.figure(figsize=(12, 5))

        plt.subplot(1, 2, 1)
        plt.title('Distribution of Fare Amount')
        plt.hist(self.df[self.df['payment_type'] == 'Card']['fare_amount'], histtype='barstacked', bins=20, edgecolor='k', color='#FA643F', label='Card')
        plt.hist(self.df[self.df['payment_type'] == 'Cash']['fare_amount'], histtype='barstacked', bins=20, edgecolor='k', color='#FFBCAB', label='Cash')
        plt.legend()

        plt.subplot(1, 2, 2)
        plt.title('Distribution of Trip Distance')
        plt.hist(self.df[self.df['payment_type'] == 'Card']['trip_distance'], histtype='barstacked', bins=20, edgecolor='k', color='#FA643F', label='Card')
        plt.hist(self.df[self.df['payment_type'] == 'Cash']['trip_distance'], histtype='barstacked', bins=20, edgecolor='k', color='#FFBCAB', label='Cash')
        plt.legend()

        plt.savefig(os.path.join(self.output_dir, 'fare_and_distance_distribution.png'))
        plt.close()

    def plot_payment_preference(self):
        plt.title("Preference of Payment")
        plt.pie(self.df['payment_type'].value_counts(normalize=True), labels=self.df['payment_type'].value_counts().index, startangle=90, shadow=True, autopct='%1.1f%%', colors=['#FA643F', '#FFBCAB'])
        plt.savefig(os.path.join(self.output_dir, 'payment_preference.png'))
        plt.close()

    def plot_passenger_count_distribution(self):
        passenger_count = self.df.groupby(['payment_type', 'passenger_count'])[['passenger_count']].count()
        passenger_count.rename(columns={"passenger_count": 'count'}, inplace=True)
        passenger_count.reset_index(inplace=True)
        passenger_count['perc'] = (passenger_count['count'] / passenger_count['count'].sum()) * 100

        new_df = pd.DataFrame(columns=['payment_type', 1, 2, 3, 4, 5, 6])
        new_df['payment_type'] = ['Card', 'Cash']
        new_df.iloc[0, 1:] = passenger_count.iloc[0:6, -1].values
        new_df.iloc[1, 1:] = passenger_count.iloc[6:, -1].values

        fig, ax = plt.subplots(figsize=(20, 6))
        new_df.plot(x='payment_type', kind='barh', stacked=True, ax=ax, color=['#FA643F', '#FFBCAB', '#CBB2B2', '#F1F1F1', '#FD9F9F'])

        for p in ax.patches:
            width = p.get_width()
            height = p.get_height()
            x, y = p.get_xy()
            ax.text(x + width / 2, y + height / 2, '{:.0f}%'.format(width), horizontalalignment='center', verticalalignment='center')

        plt.savefig(os.path.join(self.output_dir, 'passenger_count_distribution.png'))
        plt.close()

    def generate_all_plots(self):
        self.plot_fare_and_distance_distribution()
        self.plot_payment_preference()
        self.plot_passenger_count_distribution()

# Example usage:
if __name__ == "__main__":
    # Load and preprocess data using TaxiDataAnalysis and AnomalyDetection classes (not shown here)
    analysis = TaxiDataAnalysis('yellow_tripdata_2020-01.csv')
    analysis.run_analysis()

    anomaly_detector = AnomalyDetection(analysis.filtered_df)
    cleaned_df = anomaly_detector.get_cleaned_data()

    # Generate visualizations
    visualizer = DataVisualization(cleaned_df)
    visualizer.generate_all_plots()
