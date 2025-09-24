
import pandas as pd
import matplotlib.pyplot as plt

# --- USU Color Scheme ---
usu_colors = ['#003366','#9D9D9D','#6699CC', '#0055A4' ]

# Load customer data and establish region counts
customer_data = pd.read_csv('data/customer_data.csv')
region_counts = customer_data['region'].value_counts()

#Plot regional customer distributions
fig, ax = plt.subplots(figsize=(8, 8)) 
region_counts.plot.pie(
    ax=ax,
    autopct='%1.1f%%',
    startangle=90,
    colors=usu_colors[:len(region_counts)])

ax.set_title('Customer Region Distribution', fontsize=16, color='#003366', fontweight='bold')

ax.set_ylabel('')
plt.show()