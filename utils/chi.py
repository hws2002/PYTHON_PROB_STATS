
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import chi2
import math


def draw_chi_pdf(df_list,x_start = 0,x_end = 40,step = 500):
    # Generate x-axis values from 0 to 40 (excluded) with 500 steps in between
    x = np.linspace(x_start,x_end,step)

    for df in df_list:
        # Calculate the corresponding probability density function (PDF) values
        pdf = chi2.pdf(x, df)
        # Plot the chi-square distribution
        plt.plot(x, pdf, label=f"Chi-square({df})")

    # Set the plot title and labels

    # Convert the values in df_list to strings
    df_values = [str(df) for df in df_list]

    # Join the values inside curly brackets
    plt.title("Chi-square Distribution (df = {})".format(", ".join(df_values)))
    plt.xlabel("x")
    plt.ylabel("Probability Density Function (PDF)")

    # Show the legend
    plt.legend()

    # Display the plot
    plt.show()
def draw_chi_cdf(df_list,x_start = 0,x_end = 40,step = 500):
    # Generate x-axis values from 0 to 40 (excluded) with 500 steps in between
    x = np.linspace(x_start,x_end,step)

    for df in df_list:
        # Calculate the corresponding probability density function (PDF) values
        cdf = chi2.cdf(x, df)
        # Plot the chi-square distribution
        plt.plot(x, cdf, label=f"Chi-square({df})")

    # Set the plot title and labels

    # Convert the values in df_list to strings
    df_values = [str(df) for df in df_list]

    # Join the values inside curly brackets
    plt.title("Chi-square Distribution (df = {})".format(", ".join(df_values)))
    plt.xlabel("x")
    plt.ylabel("Cumulative Density Function (CDF)")

    # Show the legend
    plt.legend()

    # Display the plot
    plt.show()