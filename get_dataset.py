import requests
URL = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/master/fcc-forum-pageviews.csv'
OUT = 'fcc-forum-pageviews.csv'
def download():
    print('Downloading dataset...')
    r = requests.get(URL, timeout=30)
    r.raise_for_status()
    with open(OUT, 'wb') as f:
        f.write(r.content)
    print('Saved', OUT)

if __name__ == '__main__':
    try:
        download()
    except Exception as e:
        print('Download failed:', e)
        print('Manual link: https://github.com/freeCodeCamp/boilerplate-page-view-time-series-visualizer/blob/master/fcc-forum-pageviews.csv')
