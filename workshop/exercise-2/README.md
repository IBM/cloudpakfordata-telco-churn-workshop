# Exercise 2: Visualize Customer Churn Data
# Real Time Prediction of Telco Customer Churn using Watson Machine Learning from Cognos Dashboard


Cognos 11 is not only positioned towards the professional report author but specifically towards power users and data scientists by offering Watson-like features such as natural language search and automatic proposal of charts. Now with all these latest features in Cognos, interacting or communicating with cloud hosted services is also possible from the Cognos application.

It was always a tedious task to display a real time Watson Machine Learning (WML) model output from Cognos application. 
To achieve that, we need to have an external mechanism to invoke the model, pass the required input parameters and finally the scores are written back to the database. Cognos reads the latest scores from the database and displays on the dashboard.

Cognos dashboard traditionally display’s content from descriptive Analytics. As adoption of predictive analytics in the surge it more makes sense to bring in the Descriptive as well as Predictive content to same plane.
Things like invoking an ML model or scoring real-time. Through Watson Machine learning API, you will be able to access a model across a different platform be it Spark, R, Python or the IBM’s Proprietary Library SPSS. 


The latest version of Cognos comes with Custom control feature. It gives the capability to create a real time dashboard where we can pass the inputs through a custom widget which internally invokes the model through REST API, gets the output and displays on the dashboard.

For this, one need to build a custom control using JavaScript to get inputs and to show outputs as chart/table. Then this control can be imported into Cognos dashboard and gets real time output. In this pattern, we demonstrate to build custom control, integration of the custom control in Cognos, invoke the Machine learning model from the Cognos Dashboard and show model output at run time on Cognos Dashboard.

The dataset considered for this pattern is `Sample Customer Data in Telecom Domain`. Using the dataset, the behaviour to retain the customers is predicted. You can analyse all relevant customer data and develop focused customer retention programs.

**Use case**

Customer churn occurs when customers or subscribers stop doing business with a company or service, also known as customer attrition. It is also referred as loss of clients or customers. One industry in which churn rates are particularly useful is the telecommunications industry, because most customers have multiple options from which to choose within a geographic location.

Using this kind of data and with the help of Watson Machine Learning model output, you will be able to predict the most likely churn customers (telecom customers) from the Cognos dashboard and by taking appropriate actions (such as giving offers and needful service) will decrease the churn rate and prevent customer attrition. In other words we would be able to identify which customers are at risk of losing?

## Pre-requisites

* Cognos server - Have on-prim or SaaS offering of Cognos with `admin access`.
   > Note: Cognos version should be over 11.0.05.
 
* [IBM Cloud account](https://console.bluemix.net/): You must have an IBM Cloud account to work with this code pattern. If you do not have an IBM Cloud account, please create an account [here](https://console.bluemix.net/).

* [IBM Cloud CLI](https://console.bluemix.net/docs/cli/reference/ibmcloud/download_cli.html#install_use): IBM Cloud CLI provides the command line interface for managing resources in IBM Cloud. 

## Steps
Follow these steps to setup and run this code pattern. The steps are described in detail below.

1. [Create and Deploy Watson Machine Learning model from Watson Studio](#1-create-and-deploy-watson-machine-learning-model-from-watson-studio)
2. [Get WML Credentials and model API code](#2-get-wml-credentials-and-model-api-code)
3. [Host the WML model through node application](#3-host-the-wml-model-through-node-application)
4. [Create custom control widgets](#4-create-custom-control-widgets)
5. [Build Cognos report and import custom control widget](#5-build-cognos-report-and-import-custom-control-widget)
6. [Run the report and Analyse the results](#6-run-the-report-and-analyse-the-results) 



### 1. Create and Deploy Watson Machine Learning model from Watson Studio

[Create Watson Studio](https://console.bluemix.net/catalog/services/watson-studio) service. IBM Watson Studio can build and train AI & machine learning models, prepare and analyze data. All in a flexible, hybrid cloud environment.

- Click on ```Create``` button by selecting Lite Pricing plan as shown in below screenshot.


![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/WatsonStudioCreate.png)


- Click on ```Get started``` button to launch Watson Studio

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/WS_GetStarted.png)


- Create a new Watson Studio project.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/ws_newProj.png)

By creating a project in Watson Studio a free tier ``Object Storage`` service will be created in your IBM Cloud account. Choose the storage type as ```Cloud Object Storage``` for this code pattern.

- Define the project by giving a Name and click on ```Create```.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/define_project.png)

- Once a project is created click on ```Assets``` tab.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/WS_Assets.png)

- Under ```Modeler flows``` click on ```New Flow``` to create a Watson Machine Learning model.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/modeller.png)

- We have used sample model for this pattern, select model type as ```From sample``` radio button and choose built Machine Learning `Customer Satisfaction Prediction` model as shown and provide appropriate model name.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/sample_wml_model.png)

- The model has been created and saved. It's time to deploy it. From the ```Deployments``` tab, click on ```Add Deployment``` and select deployment type as ```Web service```.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/add_to_deploy.png)

The model should be deployed successfully.

### 2. Get WML Credentials and model API code

**WML Credentials**

Once deployment is completed, need to copy the Watson Machine Learning credentials. There are two ways to look up Watson Machine Learning service credentials, depending on where you start.
 
```Option 1: From Watson Studio```

 * From the `Services` menu in the top menu bar of Watson Studio, choose ```Watson Services```.
 * Choose the `ACTIONS` menu beside the service instance for which you want to retrieve credentials. This opens the service details page for the Watson Machine Learning service instance.
 * In the Machine Learning section, select ```Manage in IBM Cloud```.
 * Click on ```Service credentials```.
 * If there are no service credentials yet, click the ```New credential``` button.
 * Under the `ACTIONS` menu, click ```View credentials```.

 
 ```Option 2: From IBM Cloud```

 * Log in to IBM Cloud. This takes you to your IBM Cloud dashboard.
 * In your IBM Cloud dashboard, click on the ```Watson Machine Learning``` service instance for which you want to retrieve credentials. This opens the service details page for the Watson Machine Learning service instance.
 * Click on ```Service credentials```.
 * If there are no service credentials yet, click the ```New credential``` button.
 * Under the `ACTIONS` menu, click ```View credentials```.

Sample credentials as follows:
  ```
  {
    "instance_id": "5xxxxxxx-c2a6-4c76-9b3a-xxxdbe00000",
    "password": "samplepwd-xxx-pwd0-pwd-samplepwd",
    "url": "https://eu-gb.ml.cloud.ibm.com",
    "username": "7ab12e8-xxx-yyyy-xxxx-123456789
  }
```
Copy the credentials, it will be used later.

**Model API Code**

 * In `Watson Studio` reached to the `Deployments` tab from where you deployed model as explained in previous step. 
 * From the ```Deployments``` tab, click on the ```deployed model``` which will navigate you to code snippet page.
 * Under ```Implementation``` tab, you will find the `Code snippets`. Copy the code snippet of JavaScript which will be used in the app.js file in the next section.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/CodeSnippet_js.png)


### 3. Host the WML model through node application

As shown in previous step, we have got the Javascript implementation of WML Model API. To avoid CORS error, we deployed WML model API as a nodejs application. [Node application code](https://github.com/IBM/invoke-wml-using-cognos-custom-control/tree/master-sm/src/wml-api-node-app) is available at `src/wml-api-node-app`. Perform the following steps to deploy this node application.

 * Clone the repo.
   ```
   git clone https://github.com/IBM/invoke-wml-using-cognos-custom-control.git
   ```
   
 * Change the directory.
   ``` 
   cd invoke-wml-using-cognos-custom-control/src/wml-api-node-app
   ```
   
 * Update the `WML credentials` in `app.js`. Use the credentials obtained in step2.
   ![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/wml-credentials-appjs.png)
   
 * Update `scoring_url` in `app.js` as shown. Get scoring URL for your model from your JavaScript code as explained in step 2. Scoring URL will looks like ```https://xxxx.ml.cloud.ibm.com/v3/wml_instances/xxxxxx/deployments/xxxyyy/online```.
 
   ![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/scoring-url-appjs.png)
   
 * Push the application on IBM Cloud. Before running the following command, please make sure you are logged-in to IBM Cloud using cli and able to run commands. For more information, refer this [link](https://console.bluemix.net/docs/cli/reference/ibmcloud/bx_cli.html#ibmcloud_cli).
 
   ```
   ibmcloud cf push <unique name of application>
   ```
 * Get the deployed application URL. URL will be ```https://<name of application>.mybluemix.net```. This URL will be used in next step.
 
   ![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/app-url-node.png)
 

### 4. Create custom control widgets

Create the custom control widget using Javascript. The custom control developed for this pattern: 

  * asks to provide the value of required parameters as an input for the WML model.
  * calls REST API which in-turn invokes WML model using the provided input parameters.
  * API sends response back to custom control in Cognos.
  * parses the output (confidence score) and display as a d3 pie chart on Cognos Dashboard. 

In this repository, custom control code is available at `./custom-control-code`. Update the URL in `report1.js ` file as shown and save the file.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/custom-control-API.png)
  
Here, copy the URL of your node application deployed in previous step.

### 5. Build Cognos report and import custom control widget

- Place the custom widget related javaScript files [report1.js](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/custom-control-code/report1.js) and [report.css](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/custom-control-code/report.css) in the Cognos installation webcontent directory.


Path as follows
```
<Cognos installation directory>\samples\javascript\wml\
eg: "c:\Program Files\IBM\cognos\analytics\webcontent\samples\javascript\wml\
 ```
 
 ```Note:``` 
 Create the folder by name ```wml``` for this pattern under JavaScript directory.

- Launch Cognos through url in the browser (preferred browsers are Google Chrome or Mozilla Firefox).
 sample url as follows:
 ```
 http://Cognos_Server_IP:port/bi/?perspective=home
 ```

- Click on ```+ New button``` to upload the `Telco-Customer-Churn` data set to Cognos server. See screenshot for details.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/uploadcsv.png)

- Browse to upload the [Telco-customer-churn](https://github.com/IBM/invoke-wml-using-cognos-custom-control/tree/master/data/Telco-Customer-Churn.csv) csv file which you would have downloaded to your local system.

- After uploading the csv file, go to `Team Content` tab and navigate to `sample` > `Data` folder and select the recently uploaded data set and create a report using the same. See below screenshot for reference.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/createreport.png)

- Cognos will pop up to select the available templates. Pick the blank template and click `Open`. See below screenshot.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/report_template.png)

- Click on source tab to see the meta data of the data set

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/source_data_tab.png)

- Select Page1 to start adding custom widgets to the Cognos report

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/selectPage1.png)

-  Add a custom control from the toolbox icon, drag the custom control icon to the report. See below screenshot.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/custom_control_drag.png)

- Select the custom control and click the `Show properties` icon. To specify the location of the file that contains the JavaScript that you want to use for the control, click the `Module path` property. And add the other properties as per the below screenshot. To specify how you want the control to interact with the report, click the UI type property and set as `UI without event propagation`.
```
Note: Module path will be pointing to the javascripts files that was created for custom control.
eg: /samples/javascript/wml/report1.js
```

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/cc_prop.png)

-  To set the full interactivity of the report, then go to `Pages` tab, click on `Report` as per below screenshot and on the properties window ensure the `Run with full interactivity` is set to `Yes`. 

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/run_full_interactivity.png)


> Note: The below steps are optional. If you wish to skip then save the report go to step 6 which is 
`Run the report and Analyse the results`.


-  Go to report page again, add a list object to the report and then add required fields to the list. See below screenshot for reference. 

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/SampleList.png)

- Also add a Rave packed bubble chart visualization to the report and add data items to those visualizations widget to get some insights of the data. See screenshot for details.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/rave_viz.png)

- save the report under Team Content or My content by creating a folder and name it as `Invoking Watson Machine Learning Model from Cognos Dashboard`.


### 6. Run the report and Analyse the results

From Cognos report, you can view insights of the Telecom data set and along with that we can now dynamically invoke the machine learning model and get the scores or results instantly. 

- Run the saved report in `html` format ONLY. See screenshot for reference.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/run_report.png)

- In order for you to get the output of the Watson machine learning model, fill the form with required input parameters and click on `Submit` button to get the results of the WML model. See screen shot for reference.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/form_wml.png)

- Cognos will notify you saying ```Invoking Watson Machine Learning model```. Click on `OK`.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/invoke_popup.png)


- At run time, along with the input form you will now see the output of the watson machine from Cognos application itself.

![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/output_wml.png)


- From the one single Cognos dashboard, now we will be able to see the insights of the data through dataware house and along with that we can now do predictions by invoking dynamically watson machine learning models and display the output if the model on the dashboard. For the data that we passed in this scenario, we could see that the customer is most likey to churn based on the input parameters. Chances are high that this customer is likely to churn. So, the telco subscriber can now offer some good deals to that particular or set of customers who fall in the same category and try to retain them in future.
Overall output of the report will look as below screen shot.


![](https://github.com/IBM/invoke-wml-using-cognos-custom-control/blob/master/images/Report_Output.png)


With this pattern now we can avoid tedious process of invoking the Watson Machine Learning models at real time and get the output of those models displayed on the fly.

## Learn More
- [IBM Cognos Custom Widgets](https://www.ibm.com/support/knowledgecenter/en/SSEP7J_11.0.0/com.ibm.swg.ba.cognos.ag_manage.doc/c_ca_add_db_widgets.html).

- [Adding javascript to cognos](https://www.ibm.com/support/knowledgecenter/en/SSEP7J_11.0.0/com.ibm.swg.ba.cognos.ug_cr_rptstd.doc/t_rpting_add_javascrpt.html)


# Troubleshooting

[See DEBUGGING.md.](DEBUGGING.md)

## Optional: Business glossary

Instructions go here

## Optional: Data Refinery

Instructions go here

## Optional: Knowledge Catalog

Instructions go here
