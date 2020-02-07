# -*- coding: utf-8 -*-

import numpy as np
import pandas as pd

# Function to calculate missing values by column
def missing_values_table(df):

    # Total missing values
    mis_val = df.isnull().sum()

    # Percentage of missing values
    mis_val_percent = 100 * df.isnull().sum() / len(df)

    # Make a table with the results
    mis_val_table = pd.concat([mis_val, mis_val_percent], axis=1)

    # Rename the columns
    mis_val_table_ren_columns = mis_val_table.rename(
    columns = {0 : 'Missing Values', 1 : '% of Total Values'})

    # Sort the table by percentage of missing descending
    # .iloc[:, 1]!= 0: filter on missing missing values not equal to zero
    mis_val_table_ren_columns = mis_val_table_ren_columns[
        mis_val_table_ren_columns.iloc[:,1] != 0].sort_values(
    '% of Total Values', ascending=False).round(2)  # round(2), keep 2 digits

    # Print some summary information
    print("Your slelected dataframe has {} columns.".format(df.shape[1]) + '\n' +
    "There are {} columns that have missing values.".format(mis_val_table_ren_columns.shape[0]))

    # Return the dataframe with missing information
    return mis_val_table_ren_columns

    # Function to change not main categories to "Other", this funtion will be used in train and test to keep coherence between datasets
def change_cat_to_other(array_main_cat, df):
    array_categories = list(df.value_counts().index)
    array_others = [x for x in array_categories if x not in array_main_cat]
    return df.replace(array_others, 'Other')
