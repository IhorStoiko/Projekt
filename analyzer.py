import pandas as pd
import matplotlib.pyplot as plt


class SalesAnalyzer:
    """Performs loading, cleaning, analysis, and visualization
    of sales data stored in a CSV file."""

    def __init__(self, filepath):
        """Initializes the SalesAnalyzer.
        Args: filepath (str): Path to the raw sales CSV file."""
        self.filepath = filepath
        self.df = None

    def load_data(self):
        """Loads sales data from a CSV file into a pandas DataFrame.
        Returns: pandas.DataFrame: Loaded sales data."""
        self.df = pd.read_csv(self.filepath)
        return self.df

    def clean_data(self):
        """
        Cleans the sales data:
        - removes duplicates
        - converts dates to datetime
        - converts order amounts to float
        - fills missing order status values

        Returns:
            pandas.DataFrame: Cleaned sales data.
        """
        df = self.df.copy()
        df = df.drop_duplicates()
        df['order_date'] = pd.to_datetime(df['order_date'])
        df['order_amount'] = df['order_amount'].astype(float)
        df['status'] = df['status'].fillna('pending')
        self.df = df
        return self.df

    def export_clean_data(self, output_path):
        """
        Exports the cleaned sales data to a CSV file.

        Args:
            output_path (str): Path to the output CSV file.
        """
        self.df.to_csv(output_path, index=False)

    def total_revenue(self):
        """
        Calculates total revenue from all orders.

        Returns:
            float: Total revenue.
        """
        return self.df['order_amount'].sum()

    def average_order_value(self):
        """
        Calculates the average order value.

        Returns:
            float: Average order amount.
        """
        return self.df['order_amount'].mean()

    def customer_count(self):
        """
        Counts the number of unique customers.

        Returns:
            int: Number of customers.
        """
        return self.df['customer_id'].nunique()

    def repeat_customer_rate(self):
        """
        Calculates the percentage of repeat customers.

        Returns:
            float: Repeat customer rate in percent.
        """
        counts = self.df.groupby('customer_id').size()
        repeat = counts[counts > 1].count()
        return repeat / self.customer_count() * 100

    def cancellation_rate(self):
        """
        Calculates the percentage of cancelled orders.

        Returns:
            float: Cancellation rate in percent.
        """
        cancelled = self.df[self.df['status'] == 'cancelled'].shape[0]
        return cancelled / len(self.df) * 100

    def top_customers(self, n=10):
        """
        Returns top N customers by total order amount.

        Args:
            n (int, optional): Number of top customers to return.

        Returns:
            pandas.Series: Top customers sorted by revenue.
        """
        return (
            self.df
            .groupby('customer_id')['order_amount']
            .sum()
            .sort_values(ascending=False)
            .head(n)
        )

    def average_order_by_category(self):
        """
        Calculates the average order value per product category.

        Returns:
            pandas.Series: Average order value by category.
        """
        return self.df.groupby('product_category')['order_amount'].mean()

    def plot_revenue_by_category(self, save_path="figures/revenue_by_category.png"):
        """
        Creates and saves a bar chart of total revenue by product category.

        Args:
            save_path (str): Path to save the plot image.
        """
        cat_rev = self.df.groupby('product_category')['order_amount'].sum()
        ax = cat_rev.plot(kind='bar', title='Revenue by Category', figsize=(8, 5))
        ax.set_ylabel('Revenue')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_monthly_revenue(self, save_path="figures/monthly_revenue_trend.png"):
        """
        Creates and saves a line chart showing monthly revenue trend.

        Args:
            save_path (str): Path to save the plot image.
        """
        self.df['month'] = self.df['order_date'].dt.to_period('M')
        month_rev = self.df.groupby('month')['order_amount'].sum()
        ax = month_rev.plot(kind='line', title='Monthly Revenue Trend', figsize=(8, 5))
        ax.set_ylabel('Revenue')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()

    def plot_order_distribution(self, save_path="figures/order_value_distribution.png"):
        """
        Creates and saves a histogram of order value distribution.

        Args:
            save_path (str): Path to save the plot image.
        """
        ax = self.df['order_amount'].plot(
            kind='hist',
            bins=20,
            title='Order Value Distribution',
            figsize=(8, 5)
        )
        ax.set_xlabel('Order Amount')
        plt.tight_layout()
        plt.savefig(save_path)
        plt.close()
