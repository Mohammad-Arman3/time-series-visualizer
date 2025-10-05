import unittest
from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

class TimeSeriesTests(unittest.TestCase):
    def test_line_plot_returns_figure(self):
        fig = draw_line_plot()
        self.assertTrue(hasattr(fig, 'savefig'))

    def test_bar_plot_returns_figure(self):
        fig = draw_bar_plot()
        self.assertTrue(hasattr(fig, 'savefig'))

    def test_box_plot_returns_figure(self):
        fig = draw_box_plot()
        self.assertTrue(hasattr(fig, 'savefig'))

if __name__ == '__main__':
    unittest.main()
