# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:21:02 2023

@author: Home PC
"""

import pandas as pd
import numpy as np
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib



st.set_page_config(layout="wide")

st.title('HSE Performance Dashboard')
st.subheader('January to March')

# Load data into a pandas dataframe
file = "C:\\Users\\Home PC\\Desktop\\hsesummary.csv"
df = pd.read_csv('hsesummary.csv')

# Print the column names to check for typos
print(df.columns)

# Create a dropdown widget to select the region
Regions  = st.sidebar.selectbox('Select Regions', ('North', 'South'))

# Filter the data based on the selected region
df_region = df[df['Regions '] == Regions]

# Count the Total No of Audits
total_audits = df_region['Total No of Audits'].sum()

# Count the Number of Staff Trained (All segments Sites & Yards)
total_staff_trained = df_region['Number of Staff Trained (All segments Sites & Yards)'].sum()

# Count the Total number of Incidents
total_incidents = df_region['Total number of Incidents'].sum()

# Count the Number of training session
total_training_sessions = df_region['Number of training session'].sum()

# Display the summarized data using st.metric() function
col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Total No of Audits', value=total_audits)
col2.metric(label='Number of Staff Trained', value=total_staff_trained)
col3.metric(label='Total number of Incidents', value=total_incidents)
col4.metric(label='Number of training sessions', value=total_training_sessions) 




# Create a container to hold the bar charts
# Create a container to hold the bar charts
with st.container():
    # Create three columns to hold the bar charts
    col1, col2, col3 = st.columns(3)

    # Create a bar chart to display Rental Power and Rental Power Target values
    fig1, ax1 = plt.subplots()
    ax1.bar(['Rental Power', 'Rental Power Target'], 
            [df_region['Rental Power'].sum(), df_region['Rental Power Target'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax1.set_title('Rental Power vs Rental Power Target')
    col1.pyplot(fig1)

    # Create a bar chart to display Operation and Maintenance and Operation and Maintenance Target values
    fig2, ax2 = plt.subplots()
    ax2.bar(['Operation and Maintenance', 'Operation and Maintenance Target'], 
            [df_region['Operation and Maintenance (Power Houses)'].sum(), df_region['Operation and Maintenance (Power Houses) targets'].sum()],color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax2.set_title('Operation and Maintenance vs Operation and Maintenance Target')
    col2.pyplot(fig2)

    # Create a bar chart to display MHE and MHE Target values
    fig3, ax3 = plt.subplots()
    ax3.bar(['MHE', 'MHE targets'], 
            [df_region['MHE'].sum(), df_region['MHE targets'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax3.set_title('MHE vs MHE Target')
    col3.pyplot(fig3)
    
    
with st.container():
    # Create three columns to hold the pie charts
    col4, col5, col6 = st.columns(3)

    # Create a pie chart to display Logistics Vigilance and Logistics Vigilance Target values
    fig4, ax4 = plt.subplots()
    sizes = [df_region['Logistics Vigilance (Vehicles)'].sum(), df_region['Logistics Vigilance (Vehicles) Targets'].sum()]
    labels = ['Logistics Vigilance', 'Logistics Vigilance Target']
    ax4.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax4.set_title('Logistics Vigilance vs Logistics Vigilance Target')
    col4.pyplot(fig4)

    # Create a pie chart to display Yard (Power + Logistics) and Yard (Power + Logistics) Target values
    fig5, ax5 = plt.subplots()
    sizes = [df_region['Yard (Power + Logistics)'].sum(), df_region['Yard (Power + Logistics) Targets'].sum()]
    labels = ['Yard (Power + Logistics)', 'Yard (Power + Logistics) Targets']
    ax5.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax5.set_title('Yard (Power + Logistics) vs Yard (Power + Logistics) Target')
    col5.pyplot(fig5)

    # Create a pie chart to display Machine & Cranes and Machine & Cranes Target values
    fig6, ax6 = plt.subplots()
    sizes = [df_region['Machine & Cranes'].sum(), df_region['Machine & Cranes Targets'].sum()]
    labels = ['Machine & Cranes', 'Machine & Cranes Targets']
    ax6.pie(sizes, labels=labels, autopct='%1.1f%%')
    ax6.set_title('Machine & Cranes vs Machine & Cranes Target')
    col6.pyplot(fig6)



# # Create a container to hold the bar charts
# with st.container():
#     ax1, ax2, ax3 = st.columns(3)
#     # Create a bar chart to display Rental Power and Rental Power Target values
#     fig1, ax1 = plt.subplots()
#     ax1.bar(['Rental Power', 'Rental Power Target'], 
#             [df_region['Rental Power'].sum(), df_region['Rental Power Target'].sum()])
#     ax1.set_title('Rental Power vs Rental Power Target')
#     st.pyplot(fig1)

#     # Create a bar chart to display Operation and Maintenance and Operation and Maintenance Target values
#     fig2, ax2 = plt.subplots()
#     ax2.bar(['Operation and Maintenance', 'Operation and Maintenance Target'], 
#             [df_region['Operation and Maintenance (Power Houses)'].sum(), df_region['Operation and Maintenance (Power Houses) targets'].sum()])
#     ax2.set_title('Operation and Maintenance vs Operation and Maintenance Target')
#     st.pyplot(fig2)

#     # Create a bar chart to display MHE and MHE Target values
#     fig3, ax3 = plt.subplots()
#     ax3.bar(['MHE', 'MHE targets'], 
#             [df_region['MHE'].sum(), df_region['MHE targets'].sum()])
#     ax3.set_title('MHE vs MHE Target')
#     st.pyplot(fig3)



# with st.container():
#     bar1, hbar2, bar3 = st.columns(3)
#     # Create the first bar plot for Rental Power and Rental Power Target
#     fig, ax = plt.subplots()
#     ax.bar(df_region['Regions '], df_region['Rental Power'], color='blue', label='Rental Power')
#     ax.bar(df_region['Regions '], df_region['Rental Power Target'], color='gray', label='Target')
#     plt.title('Rental Power vs Target')
#     # bar1.pyplot(fig)
    
    






