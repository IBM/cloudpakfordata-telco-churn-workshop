# Exercise 3: Build and deploy a machine learning model

## Build a model

### Steps

1. [Download the notebook](#1-download-the-notebook)
1. [Create a new project and load the notebook](#2-create-a-new-project-and-load-the-notebook)
1. [Configure and run the notebook](#3-configure-and-run-the-notebook)
1. [Upload the dataset](#3-upload-the-dataset)
1. [Import notebook to Watson Studio](#4-import-notebook-to-watson-studio)
1. [Import dataset into the notebook](#5-import-dataset-into-the-notebook)

### 1. Download the notebook

*   Either clone the repository:

```bash
git clone https://github.com/IBM/customer-churn-prediction.git
```

or download the notebook directly:

```bash
wget https://raw.githubusercontent.com/IBM/customer-churn-prediction/master/notebooks/customer-churn-prediction.ipynb
```

### 2. Create a new project and load the notebook

* From the Main Menu, Choose `Project`

![Choose Project](ChooseProject.png)

* Under the `Assets` tab in your project, Click `+ New Project`, give it a name of your choosing (preferably using a tag for you to easily identify it from other users), and click `OK`.

* Choose the `New` tab. Enter an optional description, and click `Create`.

* From the menu on the left, choose `Notebooks` and click `+Add Notebook`.

* Choose the `From file` tab and navigate to where you downloaded the `customer-churn-prediction.ipynb` notebook, either in `~/Downloads/` or the location where you cloned the repository, in the `customer-churn-prediction/notebooks/` directory.

### 3. Configure and run the notebook

#### Add the dataset to your project

* Under the `Assets` tab in your project, choose `Data sets`.

* Click `+Add data set`.

* If you cloned the github repository, you can add the dataset `WA_Fn-UseC_-Telco-Customer-Churn.csv` to your project from the
`customer-churn-prediction/data/` directory.

* If you directly downloaded the notebook with `wget`, use:

```bash
wget  https://raw.githubusercontent.com/IBM/customer-churn-prediction/master/data/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

## Deploy a model

Instructions go here

## Test a model

Instructions go here

## Write a UI to call the model

Instructions go here
