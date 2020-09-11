import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from datetime import datetime
import tkinter as tk

top = tk.Tk()

style.use('fivethirtyeight')
data = pd.read_csv('https://raw.githubusercontent.com/microsoft/Bing-COVID-19-Data/master/data/Bing-COVID19-Data.csv')

mass_data_all = data.loc[(data['AdminRegion1'] == 'Massachusetts') & (data['AdminRegion2'].isnull())]
mass_data_all.reset_index(drop = True, inplace = True)

print(type(mass_data_all['Updated'][1]))
plt.plot(mass_data_all['Updated'], mass_data_all['Confirmed'])

#for date in mass_data_all['Updated']:
	# convert to date time object
	#

plt.xlabel('Date')
plt.ylabel('Cases')
plt.title('COVID19 Cases in Massachusetts')
plt.xticks(np.linspace(0, 215, 10), rotation = 30, size = 8)
plt.yticks(np.linspace(0, 130000, 14), size = 8)
plt.grid(b = True)
#print(mass_data_all['Updated'][402015])
window = plt.get_current_fig_manager()
plt.tight_layout()
plt.show()

top.mainloop()

