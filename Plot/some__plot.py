import matplotlib.pyplot as plt 
import numpy as np 
import random 
import seaborn as sns 

num_card_draws = 1_000_000
draws = [random.randrange(1, 15) for i in range(num_card_draws)]
card, repeat = np.unique(draws, return_counts=True)

draws_str = f'{num_card_draws:,}'.replace(',' , ' ')
plot_name = f'Frequency of cards randomly drawn from a stock after performing {num_card_draws} draws'
sns.set_style('darkgrid')
axis = sns.barplot(x = card, y = repeat, palette = 'bright')
axis.set(xlabel = 'card type', ylabel = 'Frequency')
axis. set_ylim(top = max(repeat)*1.10)

for column, frequency_of_card in zip(axis.patches, repeat): 
    text_x = column.get_x() + column.get_width() / 2 
    text_y = column.get_height()
    frequency_of_card_str = f'{frequency_of_card:,}'.replace(',' , ' ')
    text_plot = f'{frequency_of_card_str}\n{frequency_of_card/num_card_draws:.3%}'
    axis.text(text_x, text_y, text_plot, fontsize = 11, ha = 'center', va = 'bottom')

plt.show()

 