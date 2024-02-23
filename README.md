# Predict Resort Price with a web app

The purpose of creating this web app is to predict the resort price based on the different variables with the pickle file which is the saved machine learning model. 




## Table of Contents
- [Folder Structure](#folder-structure)
- [Prerequisites](#prerequisites)
- [Deployment Guide](#deployment-guide)
- [Web App URL](#web-app-url)
- [Dependencies](#dependencies)




## Folder Structure

/mlops_resort_zy_2
  - static
    - style.css
  - templates
    - home.html
  - app.py
  - logs.log
  - MLOps_Assignment_Resort_Zhenyang_v2.ipynb
  - requirements.txt
  - resort_regression_zy.pkl


## Prerequisites

- On Anaconda prompt, create a virtual environment (conda create --mlops mlops python=3.10)
- activate the environment (conda activate mlops)
- install the pycaret library (pip install pycaret[full]) 
- launch jupyter notebook from the correct mlops environment

- on vscode, use back the same mlops environment and run the app.py and click on the link at the terminal and the flask web app should run locally




## Deployment Guide
(on render)
1) on the top right hand corner, click on "New +", and click on "web service"
2) "build and deploy from a git repository" is selected by default, after that, click "Next"
3) connected to my github repository


4) type in the following fields as shown below:

- name: mlops-resort-zy
- region: oregon (US West)
- instance type: free
- branch: master
- build command: pip install -r requirements.txt
- start command: python app.py

and click on "create web service"


5) wait for app.py to be deployed




## Web App URL
https://mlops-resort-zy.onrender.com/




## Dependencies

- refer to the requirements.txt file for the list of dependencies



