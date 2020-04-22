# Automate model building with AutoAI

For this part of the workshop, we'll learn how to use [AutoAI](https://www.ibm.com/support/producthub/icpdata/docs/content/SSQNUZ_current/wsj/analyze-data/autoai-overview.html).
AutoAI is a capability that automates machine learning tasks to ease the tasks of data scientists. It automatically prepares your data for modeling, chooses the best algorithm for your problem, and creates pipelines for the trained models.

This section is broken up into the following steps:

1. [Set up your AutoAI environment and generate pipelines](#1-set-up-your-autoai-environment-and-generate-pipelines)
2. [Save AutoAI Model](#2-save-autoai-model)
3. [Deploy and test the model](#3-deploy-and-test-the-model)

>*Note: The lab instructions below assume you have a project already with the assets necessary to build a model. If not, follow the instructions in the pre-work section to create a project.*

## 1. Set up your AutoAI environment and generate pipelines

* Go to your analytics project overview page.

* To start the AutoAI experience, click `Add to Project` from the top and select `AutoAI`:

![Adding a project](../.gitbook/assets/images/autoai/autoai-add-project.png)

* Name your AutoAI experiment asset and choose one of the compute configuration options listed with a drop-down menu. Then, click `Create`:

![Naming your services](../.gitbook/assets/images/autoai/autoai-name-services.png)

* To configure the experiment, we must give it the dataset to use. Click on the `Select from project` option.

* In the dialog, select the 'Customer-Churn-Full.csv' file and click the `Select asset` button..

![Select file](../.gitbook/assets/images/autoai/autoai-chooseprojectdataset.png)

* Once the dataset is read in, we will need to indicate what we want the model to predict. Under *Select prediction column*, find and click on the `Churn` row.

* AutoAI will set up defaults values for the experiment based on the dataset. This includes the type of model to build, the metrics to optimize against, the test/train split, etc. You could view/change these values under 'Experiment settings', however, for now we will accept the defaults and click the `> Run experiment` button:

![Choose Churn column and run](../.gitbook/assets/images/autoai/autoai-choose-churn-and-run.png)

* The AutoAI experiment will now run and the UI will show progress as it happens:

![autoai progress](../.gitbook/assets/images/autoai/autoai-model-progress.png)

* The UI will show progress as different algorithms/evaluators are selected and as different pipelines are created & evaluated. You can view the performance of the pipelines that have completed by expanding each pipeline section.

* The experiment can take several minutes to run. Upon completion you will see a message that the pipelines have been created:

![autoai pipelines created](../.gitbook/assets/images/autoai/autoai-pilelines-complete.png)

## 2. Save AutoAI Model

The AutoAI process follows this sequence to build candidate pipelines:

* Data pre-processing
* Automated model selection (Pipeline 1)
* Hyperparameter optimization (Pipeline 2)
* Automated feature engineering (Pipeline 3)
* Hyperparameter optimization (Pipeline 4)

You can review each pipeline and select to deploy the top performing pipeline from this experiment.

* Scroll down to see the *Pipeline leaderboard*. The top performing pipeline is in the first rank.

* The next step is to select the model that gives the best result by looking at the metrics. In this case, Pipeline 4 gave the best result with the metric "Area under the ROC Curve (ROC AUC)." You can view the detailed results by clicking the corresponding pipeline from the leaderboard:

![pipeline leaderboard](../.gitbook/assets/images/autoai/autoai-pipeline-leaderboard.png)

* The model evaluation page will show metrics for the experiment, feature transformations that were performed (if any), which features contribute to the model, and more details of the pipeline.

![Model evaluation](../.gitbook/assets/images/autoai/autoai-model-evaluation.png)

* In order to deploy this model, we will Click on the `Save as model` button to save it.

* A window opens that asks for the model name, description (optional), and so on. You can accept the defaults or give your model a meaningful name/description and then click `Save`:

![Save model name](../.gitbook/assets/images/autoai/autoai-save-model-name.png)

* You receive a notification to indicate that your model is saved to your project. Go back to your project main page by clicking on the project name on the navigator on the top left:

![Model notification](../.gitbook/assets/images/autoai/autoai-model-notification.png)

* You will see the new model under *Models* section of the *Assets* page:

![choose AI model](../.gitbook/assets/images/autoai/autoai-choose-asset-ai-model.png)

## 3. Deploy and test the model

* Under the *Models* section of the *Assets* page, click the name of your saved model.

* To make the model available to be deployed, we need to make it available in the deployment space we previously set up. Click on the `Promote to deployment space`:

![Deploying the model](../.gitbook/assets/images/autoai/autoai-deploy-model.png)

* To promote the asset, you must associate your project with a deployment space. Click `Associate Deployment Space`:

![Associate Deployment Space](../.gitbook/assets/images/autoai/autoai-associate-deployment-space.png)

* You should have already created a deployment space in the *pre-work* section of the workshop. Click on `Existing` and choose that deployment then click the `Associate` button.

![Create Deployment Space](../.gitbook/assets/images/autoai/autoai-create-deployment-space.png)

* From the model page, once again click on the `Promote to deployment space`.

* This time you will see a notification that the model was promoted to the deployment space succesfully. Click `deployment space` from this notification. Also you can reach this page by using the (☰) hamburger menu and click `Analyze` -> `Analytics deployments`:

![deployment space](../.gitbook/assets/images/autoai/autoai-view-deployment.png)

![Menu analytics deployments ](../.gitbook/assets/images/autoai/autoai-menu-analytics-deployments.png)

* If you came in through the `Menu` -> `Analyze` -> `Analytics deployments` path, Click on your deployment space:

![click deployment space](../.gitbook/assets/images/autoai/autoai-click-deployment-space.png)

* Under the *Assets* tab, click on the AutoAI model you just promoted:

![click model in deployment space](../.gitbook/assets/images/autoai/autoai-deployment-space-choose-model.png)

* Under the *Deployments* tab, click the `Deploy` button to deploy this model:

![click deploy button](../.gitbook/assets/images/autoai/autoai-click-deploy.png)

* Give your deployment an name and optional description and click `Create`:

![create deployment](../.gitbook/assets/images/autoai/autoai-name-and-create-deployment.png)

* The Deployment will show as *In progress* and then switch to *Deployed* when done. Click on the deployment:

![click final deployment](../.gitbook/assets/images/autoai/autoai-deployed.png)

* The Deployment *API reference* tab show how to use the model using *cURL*, *Java*, *Javascript*, *Python*, and *Scala*:

![Deployment API reference](../.gitbook/assets/images/autoai/autoai-api-reference-curl.png)

### Testing the deployed model with the GUI tool

Now you can test your model from the interface that is provided after the deployment.

* Click on the `Test` tab.

* Click on the *Provide input data as JSON* icon and paste the following data under *Body*, then click `Predict`:

```json
   { "input_data":[ { "fields":[ "customerID", "gender", "SeniorCitizen", "Partner", "Dependents", "tenure", "PhoneService", "MultipleLines", "InternetService", "OnlineSecurity", "OnlineBackup", "DeviceProtection", "TechSupport", "StreamingTV", "StreamingMovies", "Contract", "PaperlessBilling", "PaymentMethod", "MonthlyCharges", "TotalCharges" ],
     "values":[ [ "7567-VHVEG", "Female", 0, "No", "No", 0, "No", "No phone service", "DSL", "No", "No", "Yes", "No", "No", "Yes", "Month-to-month", "No", "Bank transfer (automatic)", 85.25, 85.25 ] ] } ] }
```

![Test deployment with JSON](../.gitbook/assets/images/autoai/autoai-test-json.png)

* Alternately, you can click the *Provide input using form* icon and input the various fields, then click `Predict`:

![Input to the fields](../.gitbook/assets/images/autoai/autoai-input-fields.png)

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
curl -k -X POST --header 'Content-Type: application/json' --header 'Accept: application/json' --header "Authorization: Bearer  $WML_AUTH_TOKEN" -d '{"input_data": [{"fields": ["customerID","gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"],"values": [["7590-VHVEG","Female",0,"No","No",1,"No","No phone service","DSL","No","No","No","No","No","No","Month-to-month","No","Bank transfer (automatic)",25.25,25.25]]}]}' $URL
```

* A json string will be returned with the response, including a "Yes" of "No" at the end indicating the prediction of if the customer will churn or not.

## Conclusion

In this section we covered how to build and deploy a machine learning model to make a prediction. We could have gone through the steps in a typical data science workflow to wrange data, create/evaluate models, conducted feature engineering, experimented with different model parameters,  and more. However, we have seen how AutoAI automates and simplifies this process for us.
