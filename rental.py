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
with st.container():
    
    # Create three columns to hold the bar charts
    col1, col2, col3 = st.columns(3)

    # Create a bar chart to display Rental Power and Rental Power Target values
    fig1, ax1 = plt.subplots()
    ax1.bar(['Rental Power Audits', 'Rental Power Target'], 
            [df_region['Rental Power Audits'].sum(), df_region['Rental Power Target'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax1.set_title('Rental Power vs Rental Power Target')
    for i, v in enumerate([df_region['Rental Power Audits'].sum(), df_region['Rental Power Target'].sum()]):
        ax1.text(i, v + 0.5, str(v), ha='center', fontweight='bold')
    col1.pyplot(fig1)

    # Create a bar chart to display Operation and Maintenance and Operation and Maintenance Target values
    fig2, ax2 = plt.subplots()
    ax2.bar(['Operation and Maintenance Audits', 'Operation and Maintenance Target'], 
            [df_region['Operation and Maintenance Audits'].sum(), df_region['Operation and Maintenance (Power Houses) targets'].sum()],color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax2.set_title('Operation and Maintenance vs Operation and Maintenance Target')
    for i, v in enumerate([df_region['Operation and Maintenance Audits'].sum(), df_region['Operation and Maintenance (Power Houses) targets'].sum()]):
        ax2.text(i, v + 0.08, str(v), ha='center', fontweight='bold')
    col2.pyplot(fig2)

    # Create a bar chart to display MHE and MHE Target values
    fig3, ax3 = plt.subplots()
    ax3.bar(['MHE Audits', 'MHE targets'], 
            [df_region['MHE Audits'].sum(), df_region['MHE targets'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax3.set_title('MHE vs MHE Target')
    for i, v in enumerate([df_region['MHE Audits'].sum(), df_region['MHE targets'].sum()]):
        ax3.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    col3.pyplot(fig3)
    
    
with st.container():
    # Create three columns to hold the pie charts
    col4, col5, col6 = st.columns(3)

    # Create a pie chart to display Logistics Vigilance and Logistics Vigilance Target values
    fig4, ax4 = plt.subplots()
    ax4.bar(['Logistics Vigilance (Vehicles)','Logistics Vigilance (Vehicles) Targets'], 
            [df_region['Logistics Vigilance (Vehicles)'].sum(), df_region['Logistics Vigilance (Vehicles) Targets'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax4.set_title('Logistics Vigilance vs Logistics Vigilance Target')
    for i, v in enumerate([df_region['Logistics Vigilance (Vehicles)'].sum(), df_region['Logistics Vigilance (Vehicles) Targets'].sum()]):
        ax4.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    col4.pyplot(fig4)
    
    

    # Create a pie chart to display Yard (Power + Logistics) and Yard (Power + Logistics) Target values
    fig5, ax5 = plt.subplots()
    ax5.bar(['Yard (Power + Logistics) Audits','Yard (Power + Logistics) Targets'], 
            [df_region['Yard (Power + Logistics) Audits'].sum(), df_region['Yard (Power + Logistics) Targets'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)
    ax5.set_title('Yard (Power + Logistics) vs Yard (Power + Logistics) Target')
    for i, v in enumerate([df_region['Yard (Power + Logistics) Audits'].sum(), df_region['Yard (Power + Logistics) Targets'].sum()]):
        ax5.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    col5.pyplot(fig5)

    # Create a pie chart to display Machine & Cranes and Machine & Cranes Target values
    fig6, ax6 = plt.subplots()
    
    ax6.bar(['Machine & Cranes Audits','Machine & Cranes Targets'], 
            [df_region['Machine & Cranes Audits'].sum(), df_region['Machine & Cranes Targets'].sum()], color=['blue', 'orange']) # Set the color of the second bar to orange)

    ax6.set_title('Machine & Cranes vs Machine & Cranes Target')
    for i, v in enumerate([df_region['Machine & Cranes Audits'].sum(), df_region['Machine & Cranes Targets'].sum()]):
        ax6.text(i, v + 0.1, str(v), ha='center', fontweight='bold')
    col6.pyplot(fig6)
    






