from time_series_visualizer import draw_line_plot, draw_bar_plot, draw_box_plot

if __name__ == '__main__':
    fig1 = draw_line_plot(); fig1.savefig('line_plot.png')
    fig2 = draw_bar_plot(); fig2.savefig('bar_plot.png')
    fig3 = draw_box_plot(); fig3.savefig('box_plot.png')
    print('Saved line_plot.png, bar_plot.png, box_plot.png')
