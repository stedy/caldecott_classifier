import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import seaborn as sns

sns.set(rc={"figure.figsize":(12.5,7)})

colors = pd.read_csv("all_book_cover_colors.csv")

colors[['year', 'title']] = colors['book'].str.split("_",1,expand=True)

colors = pd.DataFrame(colors.groupby(["year", "color"])["proportion"].sum())

colors_1 = colors.reset_index()

colors_wide = pd.pivot(colors_1, index="year", columns = "color", values ="proportion")

colors_wide1 = colors_wide.reset_index()

cal_palette = {'black': '#000000', 'blue': '#0000ff', 'brown': '#654321', 'green':
        '#008000', 'grey': '#808080', 'orange': '#ffa500',
        'red': '#ff0000', 'white': '#ffffff', 'yellow': '#ffff00'}
mcolors.get_named_colors_mapping().update(cal_palette)
colors_wide1.set_index('year').plot(kind='bar', stacked = True, width=0.95,
        color = ['black', 'blue', 'brown', 'green', 'grey','orange', 'red',
            'white','yellow'])
plt.legend(loc="upper left", bbox_to_anchor=(1, 1))

plt.xlabel('Year')
plt.ylabel('Proportion')
plt.title('Cover color proportion by year for Caldecott Medal winners')

plt.savefig('caldecott_colors.png')
