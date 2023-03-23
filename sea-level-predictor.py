import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress

def draw_plot():
  # Read data from file
  sea = pd.read_csv('epa-sea-level.csv')
  lreg= linregress(sea['Year'],sea['CSIRO Adjusted Sea Level'])
  slope,y_intercept = lreg.slope,lreg.intercept
  # Create scatter plot
  plt.plot(sea['Year'],sea['CSIRO Adjusted Sea Level'],'ro')
  # Create first line of best fit
  next = pd.Series(list(range(len))) +sea['Year'].max()+1
  bestfit = sea['Year'].append(next)
  
  # Create second line of best fit
  secfit = sea[sea['Year']>1999]['Year'].append(next)
  plt.plot(bestfit,slope*bestfit+y_intercept,'b+',secfit,slope*secfit+y_intercept,'p')

  # Add labels and title
  plt.xlabel('Year');plt.ylabel('Sea Level (inches)')
  plt.grid(); plt.title('Rise of sea level')
  plt.legend(['Sea level','Upper Error','Lower Error','Line of the best fit over'])
# Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
