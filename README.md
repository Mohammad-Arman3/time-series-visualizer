# Page View Time Series Visualizer (Ready to Upload)

This project visualizes freeCodeCamp forum page views (2016-05-09 to 2019-12-03) using Pandas, Matplotlib and Seaborn.

## Included files
- time_series_visualizer.py
- main.py
- test_module.py
- get_dataset.py (helper to download CSV)
- README.md

## How to get dataset
Option A: Automatic (requires requests)
```
pip install requests
python get_dataset.py
```
Option B: Manual
Download CSV from:
https://github.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/blob/master/fcc-forum-pageviews.csv
Save as `fcc-forum-pageviews.csv` in project folder.

## Run
Install dependencies:
```
pip install pandas matplotlib seaborn numpy requests
```
Then run:
```
python main.py
```
This will create `line_plot.png`, `bar_plot.png`, and `box_plot.png`.
