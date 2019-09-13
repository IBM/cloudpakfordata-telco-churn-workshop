# Exercise 2: Machine Learning

This section is broken up into the following steps:

1. [Build a model with Spark](#build-a-model-with-spark)
1. [Create a project release](#create-a-project-release)
1. [Testing the model with Cloud Pak for Data](#testing-the-model-with-cloud-pak-for-data)
1. [(Optional) Create a Python Flask app that uses the model](#optional-create-a-python-flask-app-that-uses-the-model)

## Build a model with Spark

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

Section `1.0 Install required packages` will install libraries used to create the model, such as: [`pyspark`](https://spark.apache.org/docs/latest/api/python/index.html), and [`sklearn`](https://scikit-learn.org/stable/).

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

## Create a project release

Next, we'll create a project release and tag the model under version control. We'll use model management and deployment to make the released model available as a web service (REST API).

### Commit the project changes

* Go back to the project homepage. You may see a "**Changes made**" message. If so, you can Click on `commit and push`. If not, follow the instructions below.

![x](../.gitbook/assets/images/wml/changes_made.png)

* You will see there is a list of the assets that are created in this project. Provide a `Commit message` to identify and make note of changes being pushed. Provide a version tag under `Create version tag for release`. Please note that the tag and commit message are both very important to identify and deploy the changes.

![x](../.gitbook/assets/images/wml/commit_and_push.png)

* Click the `Commit and push` button.

* If the "**Changes made**" message is not visible, click the icon for git merge in the upper left, and choose `Commit`. Add a commit message, and click 'Commit'.

![x](../.gitbook/assets/images/wml/ICP4DgitCommit.png)

* Use the same git icon, and choose 'Push'. Add a tag, i.e. `v1`, `v2`, etc and click `Push`

### Release a new version

Now that we have a committed and tagged version of the project, we can create a project release and deploy it as a web service.

* Click the upper left (☰) menu and choose the left menu's `Adminster` drop-down list and click on `Manage deployments`.

* Click on `+ Add Project release` to create the deployment.

* This will bring up the `Create project release` page. Choose the `From IBM Cloud Private for Data` tab.

* Give it a name that you can easily track. `Route` will be a part of the url. It should be lowercase. Choose the target source project and tag that you created above. Click the `Create` button.

![x](../.gitbook/assets/images/wml/ICP4DcreateProjectRelease.png)

### Create an online and batch deployment for the deployed model

* Under the `Assets` tab, select the model you just created and then click the upper-right `+ web service` button. This will add an online deployment service for this model.

![x](../.gitbook/assets/images/wml/add_web_service.png)

* Give the web service a name, which will be appended to the URL.

* Pick the model version (i.e. Use lates version) and Web Service environment

* Choose whether you want to reserve resources and how many replicas you want for this job.

* Click the `Create` button.

![x](../.gitbook/assets/images/wml/ICP4DcreateWebService.pngg)

  > Note: At this time, the online deployment is created. You can also find the REST API URL and deployment token under the `Overview` tab.

![x](../.gitbook/assets/images/wml/ICP4DwebAppOverview.png)

The deployment is still not active. We need to launch and enable it before it can be used.

### Launch deployment

* Back in `Project releases` Click the tile for your release. Under the `Deployments` tab, there are jobs that we just created. You will find that they are currently disabled.

* Click `Launch` on the top right and then choose `Launch` from the popup window, to activate those deployments. This may take few seconds.

![x](../.gitbook/assets/images/wml/ICP4DLaunchDeployment.png)

* The onlinescore job is still disabled because there are extra steps to enable it. Click on the action menu (vertical 3 dots) and select `Enable`. This may take a little longer. Wait until `AVAILABILITY` shows `Enabled`.

![x](../.gitbook/assets/images/wml/ICP4DenableJob.png)

  > Note: For any additional changes made to the project, just update the MMD environment with the new tag, and the new version of assets are ready to be deployed.

![x](../.gitbook/assets/images/wml/update.png)

## Testing the model with Cloud Pak for Data

### Deployment testing in the UI

Test the model in the API interface.

* Click the enabled deployment. Under the `API` tab, we can test the model.
* There may be some inputs with `INSERT_VALUE`. Simply change them into values that makes sense.

![x](../.gitbook/assets/images/wml/deployment_test.png)

* Click `Submit`. The result is shown on right with inputs and prediction results.
* You can click the `Generate Code` button to get the code for [deployment testing using curl](#deployment-testing-with-curl).
* Under `Overview`, you can copy the POST API and deployment token. Save it for [using the model in an app](#10-use-the-model-in-an-app).

#### Deployment testing with curl

Using curl on the command line is a good way to test the REST APIs before integrating them with more complicated code. To access the model, use the generated code obtained during [deployment testing in the UI](#deployment-testing-in-the-ui).

For example, in a terminal run a `curl` command like the following:

```bash
curl -k -X POST \
  https://9.10.111.122:31843/dmodel/v1/churn1/pyscript/churn/score \
  -H 'Authorization: Bearer yeJhbGaaaiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyAAA2VybmFtZSI6InN0dXJkZXZhbnQiLCJwYWNrYWdlTmFtZSI6InJlbGVhc2UxIIIicGFja2FnZVJvdXRlIjoiY2h1cm4xIiwiaWF0IjoxNTQ5Njg0NTg0fQ.BBBBXw48b0MN-TslNNN8e8ZASEW1xWPSen8-1o696i54U4v75wJjiQmGMs-xMe44444yq62qE8zNvXEsHM8TnnAEfaFPvokEgWtKpduWSQo1SAKch-bQhfhMJUK2wetYsUpOw5Gffuamd_jkqqQlqi4asbL_DSGBbHhNx-nnnnnsnMKm7giBa8IgtFrf6JITVIwS2xbob2t1xE_ztG0p43KK1UrddPBpztqifQybH_zbdEPOoF6Xf-ZRBcDkRMHbhC-FFF7saWLkX3AYmCboLzatB0_ufLOy2S2TosSie_UPKOS0aLcXjJDMbgsGqy9C_AsK5n28HysmH2NeXzEN9A' \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"args":{"input_json":[{"ID":4,"GENDER":"F","STATUS":"M","CHILDREN":2,"ESTINCOME":52004,"HOMEOWNER":"N","AGE":25,"TOTALDOLLARVALUETRADED":5030,"TOTALUNITSTRADED":23,"LARGESTSINGLETRANSACTION":1257,"SMALLESTSINGLETRANSACTION":125,"PERCENTCHANGECALCULATION":3,"DAYSSINCELASTLOGIN":2,"DAYSSINCELASTTRADE":19,"NETREALIZEDGAINS_YTD":0,"NETREALIZEDLOSSES_YTD":251}]}}'
```

## (Optional) Create a Python Flask app that uses the model

Instructions go here
