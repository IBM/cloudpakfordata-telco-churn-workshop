# Exercise 2: Machine Learning

This section is broken up into the following steps:

1. [Build a model with Spark](#1-build-a-model-with-spark)
1. [Create a project release](#2-create-a-project-release)
1. [Testing the model with Cloud Pak for Data](#3-testing-the-model-with-cloud-pak-for-data)
1. [(Optional) Create a Python Flask app that uses the model](#4-optional-create-a-python-flask-app-that-uses-the-model)

## 1. Build a model with Spark

For this part of the exercise we're going to build a model with a Jupyter notebook, by importing our data, and creating a machine learning model by using a Random Forest Classifier.

### Import the notebook

At the project overview click the *New Asset* button, and choose *Add notebook*.

![Add a new asset](../.gitbook/assets/images/wml/wml-1-add-asset.png)

On the next panel select the *From URL* tab, give your notebook a name, provide the following URL, and choose the Python 3.6 environment:

```bash
https://raw.githubusercontent.com/IBM/cloudpakfordata-telco-churn-workshop/master/notebooks/TelcoChurnICP4D.ipynb
```

> The notebook is hosted in the same repo as [the workshop](https://github.com/IBM/cloudpakfordata-telco-churn-workshop).
>
> * **Notebook**: [TelcoChurnICP4D.ipynb](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/blob/master/notebooks/TelcoChurnICP4D.ipynb)
> * **Notebook with output**: [with-output/TelcoChurnICP4D.ipynb](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/blob/master/notebooks/with-output/TelcoChurnICP4D.ipynb)

![Add notebook name and URL](../.gitbook/assets/images/wml/wml-2-add-name-and-url.png)

When the Jupyter notebook is loaded and the kernel is ready then we can start executing cells.

![Notebook loaded](../.gitbook/assets/images/wml/wml-3-notebook-loaded.png)

### Run the notebook

Spend an minute looking through the sections of the notebook to get an overview. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook. While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

#### Install Python packages

Section `1.0 Install required packages` will show the libraries that come pre-installed on Cloud Pak for Data. Note that we'll have to upgrade the installed version of Watson Machine Learning Python Client. This workshop uses [`pyspark`](https://spark.apache.org/docs/latest/api/python/index.html), and [`sklearn`](https://scikit-learn.org/stable/) to build our model.

#### Add the data set to the notebook

Section `2.0 Load and Clean data` will load the virtualized data from the previous exercise. Highlight the cell labelled `# Place cursor ...` by clicking on it. Click on the *10/01* button to select a specific data set. Choose The *Remote* tab, and pick the virtualized data set that has all three joined tables (i.e. `User999.billing+products+customers`), and opt to insert the data as a *Pandas DataFrame*.

![Add the data as a Pandas DataFrame](../.gitbook/assets/images/wml/wml-4-add-dataframe.png)

By adding data a block of code will be added to the notebook. The code will automatically load that data set and create a Pandas DataFrame.

![Generated code to handle Pandas DataFrame](../.gitbook/assets/images/wml/wml-5-generated-code-dataframe.png)

> **IMPORTANT**: Don't forget to update the next cell `df = df1` with the variable from the generated code.

Continue to run the remaining cells in the section to clean the data.

#### Create the model

Section `3.0 Create a model` will split the data into training and test data, and create a model using the Random Forest Classifier algorithm.

![Building the pipeline and model](../.gitbook/assets/images/wml/wml-6-buid-pipeline-and-model.png)

Continue to run the remaining cells in the section to build the model.

#### Save the model

Section `4.0 Save the model` will save the model to your project. Update the `MODEL_NAME` variable to something unique and easisly identifiable.

```python
MODEL_NAME = "user123 customer churn model"
```

Continue to run the remaining cells in the section to save the model to Cloud Pak for Data. We'll be able to test it out with the Cloud Pak for Data tools in just a few minutes!

#### Deploy to Watson Machine Learning

Section `5.0 Deploy the model to Watson Machine Learning` will deploy your model to the Watson Machine Learning service with the Watson Machine Learning client. Update the credentials in the cell seen below. Your instructor will provide the URL, the username and password are the same used to log into Cloud Pak for Data.

![Update credentials](../.gitbook/assets/images/wml/wml-7-update-credentials.png)

Once deployed the model and deployment will be viewed.

![Building the pipeline and model](../.gitbook/assets/images/wml/wml-8-deploy-to-wml.png)

We've successfully built and deployed a machine learning model. Congratulations!

## 2. Create a project release

Next, we'll create a project release and tag the model under version control. We'll use model management and deployment to make the released model available as a web service (REST API).

### Commit the project changes

On the project home click on the *Git* button on the top row and choose *Commit*

![Commit the project changes](../.gitbook/assets/images/wml/project-1-git-commit.png)

A list of the assets will appear that were created in this project. Provide a commit message to identify the changes being pushed.

![Provide a commit message](../.gitbook/assets/images/wml/project-2-git-commit-message.png)

Again, click the same *Git* button and this time choose *Push*.

![Push a new version](../.gitbook/assets/images/wml/project-3-git-push.png)

Provide a version tag under *Create version tag for release*. Add a tag, i.e. `v1` or `v2` and click *Push*.

![Provide a commit message](../.gitbook/assets/images/wml/project-4-git-push-version.png)

### Release a new version

Now that we have a committed and tagged version of the project, we can create a project release and deploy it as a web service.

To start creating a new project release, go the (☰) menu and click on the *Manage deployments* option.

![(☰) Menu -> Manage deployments](../.gitbook/assets/images/wml/project-5-manage-deployments.png)

Click on `+ Add Project Release` to start creating a new project release.

![There are currently no releases for this project](../.gitbook/assets/images/wml/project-6-new-project-release.png)

On the next panel ensure the *From IBM Cloud Pak for Data* tab is selected, and give your project release a name and route. Select the project and version from the drop down menus, and click on *Create*.

![Fill in the project release details](../.gitbook/assets/images/wml/project-7-new-project-release-details.png)

### Configure project release

It's now time to configure the project release. Here we will choose what assets will be deployed and how they will be deployed.

We start by deploying the model we built as a web service. Click on the model on the list of *Assets* and choose to add a *Web Service*.

![Deploy the model as a web service](../.gitbook/assets/images/wml/project-8-deployment-overview.png)

Give the web service a *Name*, select a *Model version*, and *Web Service environment*. Click the *Create* button.

![Deploy the model as a web service](../.gitbook/assets/images/wml/project-9-add-web-service.png)

Once created the model details will appear, take note of the *Endpoint* and *Deployment token* that have been generated.

![Endpoint and token for the deployed model](../.gitbook/assets/images/wml/project-10-model-endpoint.png)

> **NOTE**: The deployment is not yet active. We need to launch and enable it before it can be used.

### Deploy the project

* You will be brough back to the project release page where you will see your model is *Disabled*. Click the *Launch* button to deploy your project.

![Deploy your project](../.gitbook/assets/images/wml/project-11-model-disabled.png)

Once the deployment is complete click on the action action menu (vertical 3 dots) of the model and select *Enable*.

![Endpoint and token for the deployed model](../.gitbook/assets/images/wml/project-12-model-enabled.png)

## 3. Testing the model

Cloud Pak for Data offers tools to quickly test out Watson Machine Learning models. We begin with the built-in tooling.

### Test the saved model with built-in tooling

Once the model is enabled we can test the API interface from Cloud Pak for Data. Click the enabled model deployment. From the *API* tab, default values are given and we can simply click the *Submit* button. The results are shown on the right.

![Testing the deployed model](../.gitbook/assets/images/wml/testing-1-api.png)

### Test the deployed model with cURL

Clicking the *Generate Code* button will pop open a window with some copy for you to copy. The code will use the cURL command line utility to test the REST APIs. Here's an example of the generated code that can be run from a terminal window with the `curl` command.

```bash
curl -k -X POST \
  https://9.10.111.122:31843/dmodel/v1/churn1/pyscript/churn/score \
  -H 'Authorization: Bearer yeJhbGaaaiJSUzI1NiIsInR5cCI6IkpXVCJ9...jJDMbgsGqy9C_AsK5n28HysmH2NeXzEN9A' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"args":{"input_json":[{"ID":4,"GENDER":"F","STATUS":"M","CHILDREN":2,"ESTINCOME":52004,"HOMEOWNER":"N","AGE":25,"TOTALDOLLARVALUETRADED":5030,"TOTALUNITSTRADED":23,"LARGESTSINGLETRANSACTION":1257,"SMALLESTSINGLETRANSACTION":125,"PERCENTCHANGECALCULATION":3,"DAYSSINCELASTLOGIN":2,"DAYSSINCELASTTRADE":19,"NETREALIZEDGAINS_YTD":0,"NETREALIZEDLOSSES_YTD":251}]}}'
```

## 4. (Optional) Create a Python Flask app that uses the model

You can also access the web service directly through the REST API. This allows you to use your model for inference in any of your apps. For this workshop we'll be using a Python Flask application to collect information, score it against the model, and show the results.

### Install dependencies

The general recommendation for Python development is to use a virtual environment ([`venv`](https://docs.python.org/3/tutorial/venv.html)). To install and initialize a virtual environment, use the `venv` module on Python 3 (you install the virtualenv library for Python 2.7):

In a terminal go to the cloned repo directory.

```bash
git clone https://github.com/IBM/cloudpakfordata-telco-churn-workshop
cd cloudpakfordata-telco-churn-workshop
```

Initialize a virtual environment with [`venv`](https://docs.python.org/3/tutorial/venv.html).

```bash
# Create the virtual environment using Python. Use one of the two commands depending on your Python version.
# Note, it may be named python3 on your system.
python -m venv venv       # Python 3.X
virtualenv venv           # Python 2.X

# Source the virtual environment. Use one of the two commands depending on your OS.
source venv/bin/activate  # Mac or Linux
./venv/Scripts/activate   # Windows PowerShell
```

> **TIP** :bulb: To terminate the virtual environment use the `deactivate` command.

Finally, install the Python requirements.

```bash
cd flaskapp
pip install -r requirements.txt
```

### Update environment variables

It's best practice to store configurable information as environment variables, instead of hard-coding any important information. To reference our model and supply an API key, we'll pass these values in via a file that is read, the key-value pairs in this files are stored as environment variables.

Copy the `env.sample` file to `.env`.

```bash
cp env.sample .env
```

Edit `.env` to reference the `URL` and `TOKEN`.

* `URL` is your web service URL for scoring.
* `TOKEN` is your deployment access token.

```bash
# Required: Provide your web service URL for scoring.
# E.g., URL=https://9.10.222.3:31843/dmodel/v1/project/pyscript/tag/score
URL=

# Required: Provide your web service deployment access token.
#           This TOKEN should start with "Bearer ".
# E.g., TOKEN=Bearer abCdwFg.fgH1r2... (and so on, tokens are long).
TOKEN=
```

### Start the application

Start the flask server by running the following command:

```bash
python telcochurn.py
```

Use your browser to go to [http://0.0.0.0:5000](http://0.0.0.0:5000) and try it out.

> **TIP** :bulb: Use `ctrl`+`c` to stop the Flask server when you are done.

### Sample output

The prediction screen:

> Need to add an image

Pressing `Reset` allows you to enter new values:

> Need to add an image
