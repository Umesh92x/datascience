import pandas as pd
import matplotlib.pyplot as plt


def add_bar_percentage(df_ax, x_end_margin = 5, y_end_margin = .1, xlable = 'Category', ylable = 'Values', title = 'Added a title'):
    for p in df_ax.patches:
        percentage = (p.get_width() / total) * 100
        ax.annotate(f'{percentage:.2f}%', (p.get_x() + p.get_width() + x_end_margin, p.get_y() + .1))
    plt.xlabel(xlable)
    plt.ylabel(ylable)
    plt.title(title)
    plt.show()

df = pd.read_csv("../data.csv")
ax = df.sort_values('Products', ascending = True).plot('Forecast Type', 'Products', kind = 'barh',color = 'g',figsize = (12,7))
add_bar_percentage(ax, x_end_margin = 5, y_end_margin = .1, xlable = 'Category', ylable = 'Values', title = 'Added a title')

# output : attached in directory 
