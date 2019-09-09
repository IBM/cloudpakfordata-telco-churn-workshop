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

*   Either clone this repository:

```bash
git clone https://github.com/IBM/cloudpakfordata101
```

or download the notebook directly:

```bash
wget https://raw.githubusercontent.com/IBM/cloudpakfordata101/master/workshop/TelcoChurnICP4D.ipynb
```

### 2. Create a new project and load the notebook

* From the Main Menu, Choose `Project`

![Choose Project](../../doc/source/images/MenuChooseProject.png)

* Under the `Assets` tab in your project, Click `+ New Project`, give it a name of your choosing (preferably using a tag for you to easily identify it from other users), and click `OK`.

* Choose the `New` tab. Enter an optional description, and click `Create`.

* From the menu on the left, choose `Notebooks` and click `+Add Notebook`.

* Choose the `From file` tab and navigate to where you downloaded the `customer-churn-prediction.ipynb` notebook, either in `~/Downloads/` or the location where you cloned the repository, in the `customer-churn-prediction/notebooks/` directory.

### 3. Configure and run the notebook

#### Add the dataset to your project and notebook

* Under the `Assets` tab in your project, choose `Data sets`.

* Click `+Add data set`.

* If you cloned the github repository, you can add the dataset `WA_Fn-UseC_-Telco-Customer-Churn.csv` to your project from the
`cloudpakfordata101/workshop/` directory.

* If you directly downloaded the notebook with `wget`, use:

```bash
wget  https://raw.githubusercontent.com/IBM/cloudpakfordata101/master/workshop/WA_Fn-UseC_-Telco-Customer-Churn.csv
```

* In the notebook, highlight the cell `Insert data`.

* Click on the `10/01` tab at the top which has the tooltip `Find data`. Your previously loaded data set shoulud show up.

* Click `Insert to code` and choose `Insert pandas DataFrame`.

#### Run the notebook

* Run all the cells individually by highlighting each cell by clicking it, then either click the `Run` button at the top of the notebook or `control` + `return` at the same time. While the cell is running, an asterisck will show up in the brackets to the left of the cell `[*]` and when it is done, a sequential number will show up, i.e. `[17]`. Do this for the next steps, with some additional instructions:

* In the notebook, run the first 3 cells to `!pip install` the various packages needed.

* Re-start the Jupyter notebook kernel anytime after installing new packages. At the top menu, choose `kernel` -> `restart`.

#### Create the model

* Under `Create a model`, you may change the `MODEL_NAME` to something unique and easisly identifiable i.e. `<your name>-TelcoChurn`.

## Deploy a model

Next, we'll create a project release and tag the model under version control. We'll use model management and deployment to make the released model available as a web service (REST API).

### Commit the project changes

* Go back to the project homepage. You can see a "**Changes made**" message. Click on `commit and push`.

   ![changes_made.png](../../doc/source/images/changes_made.png)

* You will see there is a list of the assets that are created in this project. Provide a `Commit message` to identify and make note of changes being pushed. Provide a version tag under `Create version tag for release`. Please note that the tag and commit message are both very important to identify and deploy the changes.

   ![commit_and_push.png](../../doc/source/images/commit_and_push.png)

* Click the `Commit and push` button.

### Create a project release                                                        

Now that we have a committed and tagged version of the project, we can create a project release and deploy it as a web service. 

* Use the left menu's `Analyze` drop-down list and click on `Model management & deployment`.

   ![mmd.png](../../doc/source/images/mmd.png)

* Click on `Project release` to create the deployment.
   
* Give it a name that you can easily track. `Route` will be a part of the url. It should be lowercase. Choose the target source project and tag that you created above. Click the `Create` button.
 
   ![release.png](../../doc/source/images/release.png)

This project release is created.

### Create an online and batch deployment for the deployed model                    

* Under the `Assets` tab, select the model you just created and then click the upper-right `+ web service` button. This will add an online deployment service for this model.

   ![add_web_service.png](../../doc/source/images/add_web_service.png)

* Choose whether you want to reserve resources and how many replicas you want for this job.

* Click the `Create` button.

   ![create_web_service.png](../../doc/source/images/create_web_service.png)

   > Note: At this time, the online deployment is created. You can also find the REST API URL and deployment token under the `Overview` tab.

   ![deployment_token.png](../../doc/source/images/deployment_token.png)

The deployment is still not active. We need to launch and enable it before it can be used.

### Launch deployment                                                               

* Under the `Deployments` tab, there are jobs that we just created. You will find that they are currently disabled.

* Click `Launch` on the top right to activate those deployments. This may take few seconds.

* The onlinescore job is still disabled because there are extra steps to enable it. Click on the action menu (vertical 3 dots) and select `Enable`. This may take a little longer. Wait until `AVAILABILITY` shows `Enabled`.

   ![launch.png](../../doc/source/images/launch.png)

   > Note: For any additional changes made to the project, just update the MMD environment with the new tag, and the new version of assets are ready to be deployed.

   ![update.png](../../doc/source/images/update.png)

## Test a model

### Deployment testing in the UI                                                    

Test the model in the API interface.

* Click the enabled deployment. Under the `API` tab, we can test the model.
* There may be some inputs with `INSERT_VALUE`. Simply change them into values that makes sense.

   ![deployment_test.png](../../doc/source/images/deployment_test.png)
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

## Write a UI to call the model

Instructions go here
