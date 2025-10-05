import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

def draw_line_plot():
    # Import data (Make a copy to not modify original)
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    data = df.copy()

    # Clean data by removing top and bottom 2.5%
    lower = data['value'].quantile(0.025)
    upper = data['value'].quantile(0.975)
    data = data[(data['value'] >= lower) & (data['value'] <= upper)]

    # Draw line plot
    fig, ax = plt.subplots(figsize=(15,5))
    ax.plot(data.index, data['value'], color='red', linewidth=1)
    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    return fig

def draw_bar_plot():
    # Import data and clean
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    data = df.copy()
    lower = data['value'].quantile(0.025)
    upper = data['value'].quantile(0.975)
    data = data[(data['value'] >= lower) & (data['value'] <= upper)]

    # Prepare data for monthly average grouped by year
    df_bar = data.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()
    # groupby year and month and compute mean
    df_group = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Ensure months order Jan-Dec
    months_order = ['January','February','March','April','May','June','July','August','September','October','November','December']
    # reorder columns to months_order (some months may be missing in columns but unstack will include all)
    df_group = df_group.reindex(columns=months_order)

    # Draw bar plot
    fig = df_group.plot(kind='bar', figsize=(15,8)).figure
    plt.xlabel('Years')
    plt.ylabel('Average Page Views')
    plt.legend(title='Months')

    return fig

def draw_box_plot():
    # Import data and clean
    df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=['date'], index_col='date')
    data = df.copy()
    lower = data['value'].quantile(0.025)
    upper = data['value'].quantile(0.975)
    data = data[(data['value'] >= lower) & (data['value'] <= upper)]

    # Prepare data for box plots
    df_box = data.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = df_box['date'].dt.year
    df_box['month'] = df_box['date'].dt.strftime('%b')
    # For month order
    months_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    df_box['month_num'] = df_box['date'].dt.month
    df_box = df_box.sort_values('month_num')

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1,2, figsize=(20,8))

    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title('Year-wise Box Plot (Trend)')
    axes[0].set_xlabel('Year')
    axes[0].set_ylabel('Page Views')

    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=months_order)
    axes[1].set_title('Month-wise Box Plot (Seasonality)')
    axes[1].set_xlabel('Month')
    axes[1].set_ylabel('Page Views')

    return fig

if __name__ == '__main__':
    # Quick run to save images
    fig1 = draw_line_plot(); fig1.savefig('line_plot.png')
    fig2 = draw_bar_plot(); fig2.savefig('bar_plot.png')
    fig3 = draw_box_plot(); fig3.savefig('box_plot.png')
    print('Saved line_plot.png, bar_plot.png, box_plot.png')
