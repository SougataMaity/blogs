
import streamlit as st
import matplotlib.pyplot as plt

def univariateplot(plot_type, df, variable_name):
    
    if plot_type == 'Line Plot':
        plt.plot(df[variable_name])
        plt.title('Line Plot')
        st.pyplot()
    elif plot_type == 'Bar Plot':
        plt.bar(df.index, df[variable_name])
        plt.title('Bar Plot')
        st.pyplot()
    elif plot_type == 'Scatter Plot':
        plt.scatter(df.index, df[variable_name])
        plt.title('Scatter Plot')
        st.pyplot()
    else:
        st.write('Select a plot type.')


def bivariateplot(plot_type, df, variable1, variable2):
    if plot_type == 'Line Plot':
        plt.plot(df[variable1], df[variable2])
        plt.title('Line Plot')
        st.pyplot()
    elif plot_type == 'Bar Plot':
        plt.bar(df[variable1], df[variable2])
        plt.title('Bar Plot')
        st.pyplot()
    elif plot_type == 'Scatter Plot':
        plt.scatter(df[variable1], df[variable2])
        plt.title('Scatter Plot')
        st.pyplot()
    else:
        st.write('Select a plot type.')
