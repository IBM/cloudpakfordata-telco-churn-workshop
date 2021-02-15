# Machine Learning Model Deployment and Scoring

In this module, we will go through the process of deploying a machine learning model so it can be used by others. Deploying a model allows us to put a model into production, so that data can be passed to it to return a prediction. The deployment will result in an endpoint that makes the model available for wider use in applications and to make business decisions. There are several types of deployments available ([depending on the model framework used](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/pm_service_supported_frameworks.html)), of which we will explore:

* Online Deployments - Creates an endpoint to generate a score or prediction in real time.
* Batch Deployments - Creates an endpoint to schedule the processing of bulk data to return predictions.

This module is broken up into several sections that explore different model deployment options as well as the different ways to invoke or consume the model. The first section of this lab will build an online deployment and test the model endpoint using both the built in testing tool as well as external testing tools. The remaining sections are optional, they build and test the batch deployment, followed by using the model from a python application.

1. [Online Deployment for a Model](#online-model-deployment)
   * Create Online Deployment
   * Test model using Cloud Pak for Data tooling
   * (Optional) Test model using cURL

1. [(Optional) Batch Deployment for a Model](#optional-batch-model-deployment)
   * Create Batch Deployment
   * Create and Schedule a Job

1. [(Optional) Integrate Model to an External Application](#optional-integrate-model-to-python-flask-application)

>*Note: The lab instructions below assume you have completed one of the machine learning modules to promote a model to the deployment space. If not, follow the instructions in one of the machine learning modules to create and promote a machine learning model.*

## Online Model Deployment

After a model has been created and saved / promoted to our deployment space, we will want to deploy the model so it can be used by others. For this section, we will be creating an online deployment. This type of deployment will make an instance of the model available to make predictions in real time via an API. Although will use the Cloud Pak for Data UI to deploy the model, the same can be done programmatically.

* Navigate to the left-hand (☰) hamburger menu and choose `Analyze` -> `Analytics deployments`:

![Analytics Analyze deployments](../images/wml/AnalyzeAnalyticsDeployments.png)

* Choose the deployment space you setup previously by clicking on the name of the space.

![Deployment space](../images/wml/deployment-space.png)

* In your space overview, click on the model name that you want to create a deployment for.

![select model](../images/wml/deployment-select-model.png)

> Note: There may be more than one model listed in the 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whicever model is available that is using a `spark-mllib_2.3` runtime.

* Click `Create deployment` on the top-right corner.

![Actions Deploy model](../images/wml/ActionsDeployModel.png)

* On the 'Create a deployment' screen, choose `Online` for the *Deployment Type*, give the Deployment a name and optional description and click `Create`:

![Online  Create](../images/wml/OnlineDeploymentCreate.png)

* The Deployment will show as *In progress* and then switch to *Deployed* when done.

![Status Deployed](../images/wml/StatusDeployed.png)

### Test Online Model Deployment

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

* From the Model deployment page, once the deployment status shows as *Deployed*, click on the name of your deployment. The deployment *API reference* tab shows how to use the model using *cURL*, *Java*, *Javascript*, *Python*, and *Scala*. 

* To get to the built-in test tool, click on the `Test` tab. Click on the *Provide input data as JSON* icon.

![Test deployment with JSON](../images/autoai/autoai-test-json.png)

* Copy and paste one of the following data objects into the *Body* panel. If you are testing a model you built using the Jupyter notebooks, copy and paste the first object. If you are testing a model you built using AutoAI, copy and paste the second object.

```json
{
   "input_data":[
      {
         "fields":["gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"],
         "values":[["Female", 0, "No", "No", 1, "No", "No phone service", "DSL", "No", "No", "No", "No", "No", "No", "Month-to-month", "No", "Bank transfer (automatic)", 25.25, 25.25]]
      }
   ]
}
```

```json
{
   "input_data":[
      {
         "fields":[ "customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges"],
         "values":[[ "7567-VHVEG", "Female", 0, "No", "No", 1, "No", "No phone service", "DSL", "No", "No", "No", "No", "No", "No", "Month-to-month", "No", "Bank transfer (automatic)", 25.25, 25.25]]
      }
   ]
}
```

* Click the `Predict` button, the model will be called with the input data. The results will display in the *Result* window. Scroll down to the bottom of the result to see the prediction (i.e "Yes" or a "No" for Churn):

![Testing the deployed model](../images/wml/TestingDeployedModel.png)

> *Note: For some deployed models (for example AutoAI based models), you can provide the request payload using a generated form by clicking on the `Provide input using form` icon and providing values for the input fields of the form. If the form is not available for the model you deployed, the icon will remain grayed out.*

![Input to the fields](../images/autoai/autoai-input-fields.png)

### (Optional) Test Online Model Deployment using cURL

Now that the model is deployed, we can also test it from external applications. One way to invoke the model API is using the cURL command.

> NOTE: Windows users will need the *cURL* command. It's recommended to [download gitbash](https://gitforwindows.org/) for this, as you'll also have other tools and you'll be able to easily use the shell environment variables in the following steps. Also note that if you are not using gitbash, you may need to change *export* commands to *set* commands.

* In a terminal window (or command prompt in Windows), run the following command to get a token to access the API. Use your CP4D cluster `username` and `password`:

```bash
curl -k -X GET https://<cluster-url>/v1/preauth/validateAuth -u <username>:<password>
```

* A json string will be returned with a value for "accessToken" that will look *similar* to this:

```json
{"username":"samaya","role":"Admin","permissions":["administrator","can_provision","manage_catalog","manage_quality","manage_information_assets","manage_discovery","manage_metadata_import","manage_governance_workflow","manage_categories","author_governance_artifacts","virtualize_transform","access_catalog","access_information_assets","view_quality","sign_in_only"],"sub":"samaya","iss":"KNOXSSO","aud":"DSX","uid":"1000331015","authenticator":"default","accessToken":"eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InNhbWF5YSIsInJvbGUiOiJBZG1pbiIsInBlcm1pc3Npb25zIjpbImFkbWluaXN0cmF0b3IiLCJjYW5fcHJvdmlzaW9uIiwibWFuYWdlX2NhdGFsb2ciLCJtYW5hZ2VfcXVhbGl0eSIsIm1hbmFnZV9pbmZvcm1hdGlvbl9hc3NldHMiLCJtYW5hZ2VfZGlzY292ZXJ5IiwibWFuYWdlX21ldGFkYXRhX2ltcG9ydCIsIm1hbmFnZV9nb3Zlcm5hbmNlX3dvcmtmbG93IiwibWFuYWdlX2NhdGVnb3JpZXMiLCJhdXRob3JfZ292ZXJuYW5jZV9hcnRpZmFjdHMiLCJ2aXJ0dWFsaXplX3RyYW5zZm9ybSIsImFjY2Vzc19jYXRhbG9nIiwiYWNjZXNzX2luZm9ybWF0aW9uX2Fzc2V0cyIsInZpZXdfcXVhbGl0eSIsInNpZ25faW5fb25seSJdLCJzdWIiOiJzYW1heWEiLCJpc3MiOiJLTk9YU1NPIiwiYXVkIjoiRFNYIiwidWlkIjoiMTAwMDMzMTAxNSIsImF1dGhlbnRpY2F0b3IiOiJkZWZhdWx0IiwiaWF0IjoxNTkxMDQ2OTIxLCJleHAiOjE1OTEwOTAwODV9","_messageCode_":"success","message":"success"}
```

* You will save this access token to a temporary environment variable. Copy the access token value (without the quotes) in the terminal and then use the following export command to save the "accessToken" to a variable called `WML_AUTH_TOKEN`.

```bash
export WML_AUTH_TOKEN=<value-of-access-token>
```

* Back on the model deployment page, gather the `URL` to invoke the model from the *API reference* by copying the `Endpoint`, and exporting it to a variable:

![Model Deployment Endpoint](../images/wml/ModelDeploymentEndpoint.png)

* Now save that endpoint to a variable named `URL` by exporting it.

```bash
export URL=<value-of-endpoint>
```

* Now run this curl command from a terminal to invoke the model with the same payload we used previousy:

```bash
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": ["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"],"values": [["Female",0,"No","No",1,"No","No phone service","DSL","No","No","No","No","No","No","Month-to-month","No","Bank transfer (automatic)",25.25,25.25]]}]}' $URL
```

* A json string will be returned with the response, including a  prediction from the model (i.e a "Yes" of "No" at the end indicating the prediction of if the customer will churn or not).

```json
{"predictions":[{"fields":["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges","gender_IX","Partner_IX","Dependents_IX","PhoneService_IX","MultipleLines_IX","InternetService_IX","OnlineSecurity_IX","OnlineBackup_IX","DeviceProtection_IX","TechSupport_IX","StreamingTV_IX","StreamingMovies_IX","Contract_IX","PaperlessBilling_IX","PaymentMethod_IX","label","features","rawPrediction","probability","prediction","predictedLabel"],"values":[["Female",0,"No","No",1,"No","No phone service","DSL","No","No","No","No","No","No","Month-to-month","No","Bank transfer (automatic)",25.25,25.25,1.0,0.0,0.0,1.0,2.0,1.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,1.0,2.0,0.0,[18,[0,4,5,6,14,15,16,17],[1.0,1.0,2.0,1.0,1.0,2.0,25.25,25.25]],[10.461610182871798,9.538389817128202],[0.52308050914359,0.4769194908564101],0.0,"No"]]}]}
```

## (Optional) Batch Model Deployment

Another approach to expose the model to be consumed by other users/applications is to create a batch deployment. This type of deployment will make an instance of the model available to make predictions against data assets or groups of records. The model prediction requests are scheduled as jobs, which are exected asynchronously. For the lab, we will break this into two steps: first step is creating the deployment (which we will do using the UI), then second step is creating and scheduling a job with values.

Lets start by creating the deployment:

* Navigate to the left-hand (☰) hamburger menu and choose `Analyze` -> `Analytics deployments`:

![Analytics Analyze deployments](../images/wml/AnalyzeAnalyticsDeployments.png)

* Choose the deployment space you setup previously by clicking on the name of the space.

![Deployment space](../images/wml/deployment-space.png)

* In your space overview, click on the model name that you want to create a deployment for.

![select model](../images/wml/deployment-select-model.png)

> Note: There may be more than one model listed in the 'Models' section. This can happen if you have run the Jupyter notebook more than once or if you have run through both the Jupyter notebook and AutoAI modules to create models. Although you could select any of the models you see listed in the page, the recommendation is to start with whicever model is available that is using a `spark-mllib_2.3` runtime.

* Click `Create deployment` on the top-right corner.

![Actions Deploy model](../images/wml/ActionsDeployModel.png)

* On the `Create a deployment` screen, choose `Batch` for the *Deployment Type*, give the Deployment a name and optional description. The default values for environment definitions, hardware definition and nodes can be left (in scenarios with large or frequent batch jobs, you may choose to scale these values up). Click `Create`:

![Batch Deployment Create](../images/wml/create_batch_deployment.png)

* Once the status shows as *Deployed* , you will be able to start submitting jobs to the deployment.

![Status Deployed](../images/wml/batch_dep_status.png)

### Create and Schedule a Job

Next we can schedule a job to run against our batch deployment. We are going to do this programmatically using the Python client SDK. For this part of the exercise we're going to use a Jupyter notebook to create and submit a batch job to our model deployment.

>*Note: The batch job input is impacted by the machine learning framework used to build the model. There is a known issue with SparkML based models where batch jobs require inline payload to be used. For other frameworks, we can use data assets (i.e CSV files) as the input payload.*

#### Run the Batch Notebook

The Jupyter notebook is already included as an asset in the project you imported earlier.

* From the project overview page, *click* on the `Assets` tab to open the assets page where your project assets are stored and organized.

* Scroll down to the `Notebooks` section of the page and *Click* on the pencil icon at the right of the `machinelearning-churn-batchscoring` notebook.

![Notebook Open](../images/wml/batch_open_nb.png)

When the Jupyter notebook is loaded and the kernel is ready, we will be ready to start executing it in the next section.

Spend a minute looking through the sections of the notebook to get an overview. A notebook is composed of text (markdown or heading) cells and code cells. The markdown cells provide comments on what the code is designed to do.

You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook or hitting the keyboard short cut to run the cell (Shift + Enter but can vary based on platform). While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

**Please note that some of the comments in the notebook are directions for you to modify specific sections of the code. Perform any changes as indicated before running / executing the cell.**

##### Notebook sections

With the notebook open, you will notice:

* Section `1.0 Install required packages` will install some of the libraries we are going to use in the notebook (many libraries come pre-installed on Cloud Pak for Data). Note that we upgrade the installed version of Watson Machine Learning Python Client. Ensure the output of the first code cell is that the python packages were successfully installed.

* Section `2.0 Create Batch Deployment Job` will create a job for the batch deployment. To do that, we the Watson Machine Learning client to get our deployment and create a job.

  * In the first code cell for Section2.1, be sure to update the `wml_credentials` variable.

    * The url should be the hostname of the Cloud Pak for Data instance.
    * The username and password should be the same credentials you used to log into Cloud Pak for Data.

  * In section 2.2, be sure to update the `DEPLOYMENT_SPACE_NAME` variable with your deployment space name.

  * In section 2.3, be sure to update the `DEPLOYMENT_NAME` variable with the name of the batch deployment you created above.

* Continue to run the cells.

* Section `3.0 Monitor Batch Job Status` will start polling the job status until it completes or fails. The code cell will output the status every 5 seconds as the job goes from queued to running to completed or failed.

![Batch Job Status](../images/wml/batch_results_poll.png)

* Once the job completes, continue to run the cells until the end of the notebook.

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to conserve resources! You can do this by going to the Asset page of the project, selecting the notebook you have been running and selecting to `Stop Kernel` from the Actions menu. If you see a lock icon on the notebook, click it to unlock the notebook so you can stop the kernel.*

![Stop kernel](../images/wml/JupyterStopKernel.png)

## (Optional) Integrate Model to Python Flask Application

You can also access the online model deployment directly through the REST API. This allows you to use your model for inference in any of your apps. For this workshop we'll be using a Python Flask application to collect information, score it against the model, and show the results.

### Install Dependencies

> **Note** that this application only runs on python 3.6 and above, so the instructions here are for python 3.6+ only.

In a terminal go to the cloned repo directory. Then, in a terminal (`command prompt` or `powershell` in Windows) navigate to the unzipped folder.

```bash
git clone https://github.com/IBM/cloudpakfordata-telco-churn-workshop
cd cloudpakfordata-telco-churn-workshop/flaskapp
```

Initialize a virtual environment with [`venv`](https://docs.python.org/3/tutorial/venv.html).

```bash
# Create the virtual environment using Python. Use one of the two commands depending on your Python version.
# Note, it may be named python3 on your system.
python -m venv venv       # Python 3.X

# Source the virtual environment. Use one of the two commands depending on your OS.
source venv/bin/activate  # Mac or Linux
./venv/Scripts/activate   # Windows CMD or PowerShell
```

> **TIP** To terminate the virtual environment use the `deactivate` command.

Finally, install the Python requirements.

```bash
pip install -r requirements.txt
```

### Update Environment Variables

It's best practice to store configurable information as environment variables, instead of hard-coding any important information. To reference our model and supply an API key, we'll pass these values in via a file that is read, the key-value pairs in this files are stored as environment variables.

Copy the `env.sample` file to `.env`.

```bash
cp env.sample .env
```

Edit `.env` to and fill in the `MODEL_URL` as well as the `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`.

* `MODEL_URL` is your web service URL for scoring which you got from the section above
* `AUTH_URL` is the preauth url of your CloudPak4Data and will look like this: `https://<cluster_url>/v1/preauth/validateAuth`
* `AUTH_USERNAME` is your username with which you login to the CloudPak4Data environment
* `AUTH_PASSWORD` is your password with which you login to the CloudPak4Data environment

Note: Alternatively, you can fill in the `AUTH_TOKEN` instead of `AUTH_URL`, `AUTH_USERNAME`, and `AUTH_PASSWORD`. You will have generated this token in the section above. However, since tokens expire after a few hours and you would need to restart your app to update the token, this option is not suggested. Instead, if you use the username/password option, the app can generate a new token every time for you so it will always have a non-expired ones.

here's an example of a completed lines of the .env file.

```bash
# Required: Provide your web service URL for scoring.
# E.g., MODEL_URL=https://<cluster_url>/v4/deployments/<deployment_space_guid>/predictions
MODEL_URL=https://cp4d.cp4dworkshops.com/v4/deployments/5f939979-14c2-4538-a2af-a970aeb59abd/predictions

# Required: Please fill in EITHER section A OR B below:

# #### A: Authentication using username and password
#   Fill in the authntication url, your CloudPak4Data username, and CloudPak4Data password.
#   Example:
#     AUTH_URL=<cluster_url>/v1/preauth/validateAuth
#     AUTH_USERNAME=my_username
#     AUTH_PASSWORD=super_complex_password
AUTH_URL=https://cp4d.cp4dworkshops.com/v1/preauth/validateAuth
AUTH_USERNAME=username_001
AUTH_PASSWORD=my_secure_password_!
```

### Start Application

Start the flask server by running the following command:

```bash
python telcochurn.py
```

Use your browser to go to [http://0.0.0.0:5000](http://0.0.0.0:5000) and try it out.

> **TIP**: Use `ctrl`+`c` to stop the Flask server when you are done.

#### Sample output

Enter some sample values into the form (see screenshot below).

![Input a bunch of data...](../images/generic/input.png)

Click the `Submit` button and the churn percentage is returned:

![Get the churn percentage as a result](../images/generic/score.png)

## Conclusion

In this section we covered the followings:

* Creating and Testing Online Deployments for models.
* Creating and Testing Batch Deployments for models.
* Integrating the model deployment in an external application.

Taking a predictive model and infusing AI into applications.
