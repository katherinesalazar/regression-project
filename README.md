# Zillow Regression Project Description
- The Zillow Data Science Team wants to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the "hot months" (in terms of real estate demand) of May-August, 2017.

![alt text](https://github.com/katherinesalazar/visuals/blob/main/zillow_objectives_goals.png)
![alt text](https://github.com/katherinesalazar/visuals/blob/main/zillow_exec_sum.png)
# Project Planning
- Refer to trello kanban board for planning overview: https://trello.com/b/IdNd8GPA/regression-project
- Utilized agile program management methodology 
# Initial Ideas
- The Zillow Data Science team would like to know:
  - What states and counties are these single unit properties located in?
  - What is the distribution of tax rates for each county of the single unit properties?
  
# Hypothesis
- Is there a correlation between in taxvaluedollarcnt (tax_value) for homes based on which county it is in?
- Is there a correlation between square feet of the home and its taxvaluedollarcnt (tax_value)?
    - **True Positive**: Predict there is a relationship and there is a relationship

    - **True Negative**:Predict there is no relationship and there is not relationship

    - **False Positive**: Predict there is a relationship and there is no relationship

    - **False Negative**: Predict there is no relationship and there is a relationship

# Data Dictionary
![alt text](https://github.com/katherinesalazar/visuals/blob/main/zillow_data_dict.png)
# How to Reproduce
-  Read this README.md
- Download the acquire.py, prep.py, explore.py, model.py and final_notebook.ipynb into your working directory
- Have your own SQL database connection with your own env.py file
- Run the final_notebook.ipynb 
