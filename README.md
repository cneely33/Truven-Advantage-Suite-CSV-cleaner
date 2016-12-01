# Truven-Advantage-Suite-CSV-cleaner
A python Script used to clean/prep CSV's downloaded from Truven Advantage Suite for further analysis

Truven Advantage Suite Reports can be downloaded as a CSV for furhter analysis. However, each CSV needs the headers adjusted before being loaded as a dataframe. 

This script will cycle through all .csv files in the current working directory, create a new folder to store modified files in, write the modified files to the new directory. 
