#                                                                            12-11-2024
#                                                                            LAB SESSION 27:
#                                                                                 
# 
#                                                                             Program 27
#Show party wise seat share for following results of the Assembly Elections 2023 in
# 1) Two different pie charts on two different plots. Party with highest percentage should be shown as slightly detached
# ( show the percentage seat share on each wedge )
# 2)Two pie charts as subplots on the same figure object
# 3)As a bar chart with party name on X axis and seats won on y axis. Show results of both the states on the same bar plot. Give proper legends
# Madhya Pradesh
# BJP - Win (163) INC - Win (66) BSP – Win ( 0) Others – Win (1)
# Rajasthan
# INC - Win (69) BJP- Win (115) BSP- Win (2) Others-Win (13)

import matplotlib.pyplot as plt
import numpy as np

mp_parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]

rajasthan_parties = ['INC', 'BJP', 'BSP', 'Others']
rajasthan_seats = [69, 115, 2, 13]


fig, axes = plt.subplots(1, 2, figsize=(14, 7))


mp_colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
mp_wedges, mp_texts, mp_autotexts = axes[0].pie(mp_seats, labels=mp_parties, autopct='%1.1f%%', 
                                              colors=mp_colors, startangle=90, pctdistance=0.85)


mp_wedges[0].set_edgecolor('black')  
mp_wedges[0].set_linewidth(1.5)


rajasthan_colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
rajasthan_wedges, rajasthan_texts, rajasthan_autotexts = axes[1].pie(rajasthan_seats, labels=rajasthan_parties, autopct='%1.1f%%', colors=rajasthan_colors, startangle=90, pctdistance=0.85)

rajasthan_wedges[1].set_edgecolor('black') 
rajasthan_wedges[1].set_linewidth(1.5)

axes[0].set_title('Madhya Pradesh - 2023 Election Results')
axes[1].set_title('Rajasthan - 2023 Election Results')

for ax in axes:
    ax.axis('equal')

plt.tight_layout()
plt.show()

parties = ['BJP', 'INC', 'BSP', 'Others']
mp_seats = [163, 66, 0, 1]
rajasthan_seats = [115, 69, 2, 13]

fig, ax = plt.subplots(figsize=(10, 6))

width = 0.35  
x = np.arange(len(parties))  

rects1 = ax.bar(x - width/2, mp_seats, width, label='Madhya Pradesh', color='lightblue')
rects2 = ax.bar(x + width/2, rajasthan_seats, width, label='Rajasthan', color='lightgreen')

ax.set_ylabel('Seats Won')
ax.set_title('Seat Share in Madhya Pradesh and Rajasthan (2023 Elections)')
ax.set_xticks(x)
ax.set_xticklabels(parties)
ax.legend()

def add_labels(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  
                    textcoords="offset points",
                    ha='center', va='bottom')

add_labels(rects1)
add_labels(rects2)

plt.tight_layout()
plt.show()
