# grab data : https://stackoverflow.com/questions/10556048/how-to-extract-tables-from-websites-in-python
# pickle : https://stackoverflow.com/questions/11218477/how-can-i-use-pickle-to-save-a-dict

import requests
import pandas as pd
import pickle
from matplotlib import pyplot as plt
import numpy as np

def grab_year(year):
    # Saves financial tables from a government website
    # The result is returned
    url = 'https://www.treasury.gov/resource-center/data-chart-center/interest-rates/pages/TextView.aspx?data=yieldYear&year='
    url_year = url + str(year)
    raw_html = requests.get(url_year).content
    df = pd.read_html(raw_html)[1]
    # df.to_csv('data_'+str(year)+'.csv') #another saving option
    return df

def scrape():
    # Collects the tables for a range of years
    # Saves the result as a pickle
    # Minimize the impact on the website by accessing the data only once
    # and saving it in a pickle file.
    data = [ grab_year(i) for i in range(2000,2022) ]
    with open('data.p', 'wb') as handle:
        pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_data(fn):
    # Load the pickle file from a filename
    with open(fn, 'rb') as my_file:
        pdata = pickle.load(my_file)
    return pdata

def get_date_changes(dates):
    # Returns a list of tuples from the dataframe dates column
    # The tuple will be [index of change, last two digits of year]
    #   The type will be a List[int, string]
    # Remember to include the start and end years
    
    # create list and add start year
    date_changes = [(0, "00")]
    
    # current year counter
    x = 0
    # current index counter
    index = 0
    # cycle dates column
    for row in dates:
        # check if current year does not match current year counter
        if (int(row[-2]+row[-1]) != x):
            # if it doesn't match then we increase current year counter
            x = x + 1
            # and add new index of change and year to our list
            date_changes.append((index, row[-2]+row[-1]))
        # increase index counter
        index = index + 1
    # add end year
    date_changes.append((index, "22"))

    return date_changes

def plot_data(cols, r):
    # Plot each of the columns in a loop using plt
    
    my_data = r.to_numpy()
    for i in range(12):
        # reference a column of the data to plot
        col1 = my_data[:,(i+1)]
        x = np.arange(5506)
        y = col1[x]
        # Add the column name as a label
        plt.plot(x,y, label=cols[i+1])

    pass

def plot_finalize(dc, r):
    
    # Set the xticks to the values from the date changes variable
    plt.xticks([el[0] for el in dc], [el[1] for el in dc])

    # Set x ticks to be every 1
    # Set the axis range to be reasonable
    plt.xlim([0, 5506])
    plt.ylim([0,10])
    
    # Turn the grid on
    plt.grid()
    
    # Show the legend
    plt.legend(loc="upper right", bbox_to_anchor=(1.30, 1.0))
    
    # Show (for testing)
    plt.show()
    
    # Save (for submitting)
    pass

def wrangle():
    # Load the pickle data
    data = load_data('data.p')
    # Concatenate data frames and set NaN values to -1 with fillna
    r = pd.concat(data).fillna(-1)
    # Get column names
    cols = data[0].columns
    
    # Get times the year changed
    dc = get_date_changes(r[cols[0]].values)

    # Plot 
    plot_data(cols, r)
    plot_finalize(dc, r)

    # Visually cross verify the 30 yr with the following link
    # https://www.macrotrends.net/2521/30-year-treasury-bond-rate-yield-chart

if __name__ == "__main__":
    # This is idiomatic for the main function
    # Notice how there's no code in the global scope except for import statements
    # Notice how the functions are short and do only 1 small thing
    # Try to follow these programming practices
        # Only imports, functions, and decorators (@jit, etc) in global scope
        # Short functions
        # Deterministic functions which compute then return
        # Write tests when sensible (not required for this assignment)

    # This has been commented out (as a courtesy to minimize load)
    #scrape() the data is already included
    # You'll be implementing some minor functions to plot the data
    wrangle()