# European Soccer

Demo Project for Code Louisville Data Analysis

## Overview

The purpose of this project is to demonstrate a simple data analysis using SQL, 
Python, and Tableau.

1. Explore Data using SQL
1. Clean Data using Python
1. Analyze Data using Python
1. Visualize Data using Tableau


## Instructions

1. Fork and clone this repo.
1. Create a virtual environment and install the required libraries in 
`requirements.txt`.
1. [Download the SQLite database from Kaggle](https://www.kaggle.com/datasets/hugomathien/soccer) 
and save it to the project directory.
1. Run the `01_explore.ipynb` notebook.


## Demo 1: Explore the data

- View the gitignore updates- ignoring the settings.json (sqlite extension) and
database.sqlite files
- Connect to the database and list the tables and columns. Note that these queries
are database-specific - they would need to be changed when using something other
than SQLite.
- Explore a numeric field - get a sense for the distribution
- Explore a categorical field


## Demo 2: Clean the data

- Remove unneeded columns
- Remove records with NULL values
- Translate dates to Birth Month
