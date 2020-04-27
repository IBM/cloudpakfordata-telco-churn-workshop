# Machine Learning in Jupyter Notebook

In this module, we will go through the process of exploring our data set and building a predictive model that can be used to determine the likelyhood of a customer churning. For this use case, the machine learning model we are building is a classification model that will return a prediction of Yes (the customer will churn) or No (the customer will not churn). The approach we will take in this lab is to some fairly popular libraries / frameworks to build the model in Python using a Jupyter notebook. Once we have built the model, we will make it available for deployment so that it can be used by others.

This module is broken up into the following steps:

1. [Build a model](#1-build-a-model)
1. [Deploying the model](#2-deploying-the-model)
1. [Testing the model](#3-testing-the-model)

>*Note: The lab instructions below assume you have a project and a deployment space already. If not, follow the instructions in the pre-work section to create a project and a space.*

## 1. Build a model

For this part of the exercise we're going to use a Jupyter notebook to create the model. The Jupyter notebook is already included as an asset in the project you imported earlier.

>*Note: The Jupyter notebook included in the project has been cleared of output. If you would like to see the notebook that has already been completed with output: **Notebook with output**: [with-output/TelcoChurnICP4DOutput.ipynb](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/blob/master/notebooks/with-output/TelcoChurnICP4DOutput.ipynb)*

Open the notebook:

* From the project overview page, *click* on the `Assets` tab to open the assets page where your project assets are stored and organized.

* Scroll down to the `Notebooks` section of the page and *Click* on the pencil icon at the right of the `machinelearning-churn-sparkmlmodel` notebook.

![Notebook Open](../.gitbook/assets/images/wml/wml-open-notebook.png)

When the Jupyter notebook is loaded and the kernel is ready, we will be ready to start executing it in the next section.

![Notebook loaded](../.gitbook/assets/images/wml/wml-3-notebook-loaded.png)

### Run the notebook

Spend an minute looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do.

You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

**Please note that some of the comments in the notebook are directions for you to modify specific sections of the code. Perform any changes as indicated before running / executing the cell.**

#### Notebook sections

With the notebook open, you will notice:

* Section `1.0 Install required packages` will install some of the libraries we are going to use in the notebook (many libraries come pre-installed on Cloud Pak for Data). Note that we upgrade the installed version of Watson Machine Learning Python Client. Ensure the output of the first code cell is that the python packages were successfully installed.

* Section `2.0 Load and Clean data` will load the data set we will use to build out machine learning model. In order to import the data into the notebook, we are going to use the code generation capability of Watson Studio.

  * Highlight the code cell below by clicking it. Ensure you place the cursor below the `import pandas as pd` line.
  * Click the 10/01 "Find data" icon in the upper right of the notebook to find the data asset you need to import.
  * If you are using virtualized data, then choose your virtualized merged view (i.e. User999.BILLINGPRODUCTCUSTOMERS). If you are using this notebook without virtualized data, you can use the `Customer-Churn.csv` CSV file version of the data set that has been included in the project.
  * For your dataset, Click `Insert to code` and choose `Insert Pandas DataFrame`. The code to bring the data into the notebook environment and create a Pandas DataFrame will be added to the cell below.
  * Run the cell and you will see the first five rows of our dataset.

![Add the data as a Pandas DataFrame](../.gitbook/assets/images/wml/wml-4-add-dataframe.png)

![Generated code to handle Pandas DataFrame](../.gitbook/assets/images/wml/wml-5-generated-code-dataframe.png)

> **IMPORTANT**: Since we are using generated code to import the data, you will need to update the next cell to assign the `df` variable. Copy the variable that was generated in the previous cell ( it will look like `df=data_df_1`, `data_df_2`, etc) and assign it to the `df` variable (for example `df=df_data_1`).

* Continue to run the remaining cells in section 2 to explore and clean the data.

* Section `3.0 Create a model` cells will run through the steps to build a model pipeline.

  * We will split our data into training and test data, encode the categorial string values, create a model using the Random Forest Classifier algorithm, and evaluate the model against the test set.
  * Run all the cells in section 3 to build the model.

![Building the pipeline and model](../.gitbook/assets/images/wml/wml-6-buid-pipeline-and-model.png)

#### Save the model

* Section `4.0 Save the model` will save the model to your project.

* We will be saving and deploying the model to the Watson Machine Learning service within our Cloud Pak for Data platform. In the next code cell, be sure to update the `wml_credentials` variable.

  * The url should be the hostname of the Cloud Pak for Data instance.
  * The username and password should be the same credentials you used to log into Cloud Pak for Data.

* You will update the `MODEL_NAME` and `DEPLOYMENT_SPACE_NAME` variables. Use a unique and easily identifiable model name.

```python
MODEL_NAME = "user123 customer churn model"
DEPLOYMENT_SPACE_NAME = "Name you used for deployment space"
```

* Continue to run the cells in the section to save the model to Cloud Pak for Data. We'll be able to test it out with the Cloud Pak for Data tools in just a few minutes!

**We've successfully built and deployed a machine learning model. Congratulations!**

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to conserve resources! You can do this by going to the Asset page of the project, selecting the notebook you have been running and selecting to `Stop Kernel` from the Actions menu. If you see a lock icon on the notebook, click it to unlock the notebook so you can stop the kernel.*

![Stop kernel](../.gitbook/assets/images/wml/JupyterStopKernel.png)

## 2. Deploying the model

Now that we have created a model and saved it to our respository. We will want to deploy the model so it can be used by others. For this section, we will be creating an online deployment. This type of deployment will make an instance of the model available to make predictions in real time via an API. Although will use the Cloud Pak for Data UI to deploy the model, the same can be done programmatically.

* Navigate to the left-hand (☰) hamburger menu and choose `Analyze` -> `Analytics deployments`:

![Analytics Analyze deployments](../.gitbook/assets/images/wml/AnalyzeAnalyticsDeployments.png)

* Choose the deployment space you setup previously by clicking on the name of the space.

* In your space overview, select the model name that you just built in the notebook and click the 3 dots under `Actions`, and choose `Deploy`:

![Actions Deploy model](../.gitbook/assets/images/wml/ActionsDeployModel.png)

* On the 'Configure and deploy' screen, choose `Online` for the *Deployment Type*, give the Deployment a name and optional description and click `Create`:

![Online Deployment Create](../.gitbook/assets/images/wml/OnlineDeploymentCreate.png)

* Once the status shows as *Deployed* , you will be able to click on the deployment name to begin testing:

![Status Deployed](../.gitbook/assets/images/wml/StatusDeployed.png)

## 3. Testing the model

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

### Test the saved model with built-in tooling

* From the Model deployment page, click on the name of your deployment and then click on the `Test` tab and paste the following into the *Enter input data* cell:

```json
{
   "input_data":[
      {
         "fields":[
            "gender",
            "SeniorCitizen",
            "Partner",
            "Dependents",
            "tenure",
            "PhoneService",
            "MultipleLines",
            "InternetService",
            "OnlineSecurity",
            "OnlineBackup",
            "DeviceProtection",
            "TechSupport",
            "StreamingTV",
            "StreamingMovies",
            "Contract",
            "PaperlessBilling",
            "PaymentMethod",
            "MonthlyCharges",
            "TotalCharges"
         ],
         "values":[
            [
               "Female",
               0,
               "No",
               "No",
               1,
               "No",
               "No phone service",
               "DSL",
               "No",
               "No",
               "No",
               "No",
               "No",
               "No",
               "Month-to-month",
               "No",
               "Bank transfer (automatic)",
               25.25,
               25.25
            ]
         ]
      }
   ]
}
```

* Click `Predict` and the model will be called with the input data. The results will display in the *Result* window. Scroll down to the bottom (Line #114) to see either a "Yes" or a "No" for Churn:

![Testing the deployed model](../.gitbook/assets/images/wml/TestingDeployedModel.png)

### Test the deployed model with cURL

Now that the model is deployed, we can also test it from external applications. One way to invoke the model API is using the cURL command.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps. Also note that if you are not using gitbash, you may need to change *export* commands to *set* commands.

* In a terminal window (or command prompt in Windows), run the following command to get a token to access the API. Use your CP4D cluster `username` and `password`:

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

* A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"username":"scottda","role":"Admin","permissions":["access_catalog","administrator","manage_catalog","can_provision"],"sub":"scottda","iss":"KNOXSSO","aud":"DSX","uid":"1000331002","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNjb3R0ZGEiLCJyb2xlIjoiQWRtaW4iLCJwZXJtaXNzaW9ucyI6WyJhY2Nlc3NfY2F0YWxvZyIsImFkbWluaXN0cmF0b3IiLCJtYW5hZ2VfY2F0YWxvZyIsImNhbl9wcm92aXNpb24iXSwic3ViIjoic2NvdHRkYSIsImlzcyI6IktOT1hTU08iLCJhdWQiOiJEU1giLCJ1aWQiOiIxMDAwMzMxMDAyIiwiYXV0aGVudGljYXRvciI6ImRlZmF1bHQiLCJpYXQiOjE1NzM3NjM4NzYsImV4cCI6MTU3MzgwNzA3Nn0.vs90XYeKmLe0Efi5_3QV8F9UK1tjZmYIqmyCX575I7HY1QoH4DBhon2fa4cSzWLOM7OQ5Xm32hNUpxPH3xIi1PcxAntP9jBuM8Sue6JU4grTnphkmToSlN5jZvJOSa4RqqhjzgNKFoiqfl4D0t1X6uofwXgYmZESP3tla4f4dbhVz86RZ8ad1gS1_UNI-w8dfdmr-Q6e3UMDUaahh8JaAEiSZ_o1VTMdVPMWnRdD1_F0YnDPkdttwBFYcM9iSXHFt3gyJDCLLPdJkoyZFUa40iRB8Xf5-iA1sxGCkhK-NVHh-VTS2XmKAA0UYPGYXmouCTOUQHdGq2WXF7PkWQK0EA","_messageCode_":"success","message":"success"}
```

* You will save this access token to a tepmorary environment variable. Use the export command to save the "accessToken" part of this response in the terminal window to a variable called `WML_AUTH_TOKEN`.

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

* Back on the model deployment page, gather the `URL` to invoke the model from the *API reference* by copying the `Endpoint`, and exporting it to a `:

![Model Deployment Endpoint](../.gitbook/assets/images/wml/ModelDeploymentEndpoint.png)

* Now save that endpoint to a variable named `URL` by exporting it.

```bash
export URL=https://blahblahblah.com
```

* Now run this curl command from a terminal to invoke the model with the same payload we used previousy:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": ["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"],"values": [["Female",0,"No","No",1,"No","No phone service","DSL","No","No","No","No","No","No","Month-to-month","No","Bank transfer (automatic)",25.25,25.25]]}]}' $URL
```

* A json string will be returned with the response, including a "Yes" of "No" at the end indicating the prediction of if the customer will churn or not.

## Conclusion

In this section we covered how the followings:

* Creating a Jupyter Notebook
* Creating Models
* Deploying Models
* Testing your deployed model

With this knowledge you should feel right at home within the Jupyter notebook. Moreover, you now know how to build a model and use it in a real life scenario.
