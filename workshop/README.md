
## Analyzing Telco Customer Churn with Cloud Pak for Data on OpenShift

Welcome to our workshop! In this workshop we'll be using the Cloud Pak for Data platform to Collect Data, Organize Data, Analyze Data, and Infuse AI into our applications. The goals of this workshop are:

* Collect and virtualize data
* Visualize data with Data Refinery
* Create and deploy a machine learning model
* Monitor the model
* Create a Python app to use the model

### About this workshop

The introductory page of the workshop is broken down into the following sections:

* [Agenda](#agenda)
* [Compatability](#compatability)
* [About Cloud Pak for Data](#about-cloud-pak-for-data)
* [Credits](#credits)

### About the data set

The data set used for this workshop is originally from Watson Analytics and was used on a [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) project, it contains information about customer churn for a Telecommunications company. The data is split into three CSV files and are located in the [data](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/tree/master/data/split) directory of the GitHub repository you will download in the pre-work section.

#### **[billing.csv](../../data/split/billing.csv)**

This file has the following attributes:

* Customer ID
* Contract *(Month-to-month, one year, two year)*
* Paperless Billing *(Yes, No)*
* Payment Method *(Bank transfer, Credit card, Electronic check, Mailed check)*
* Monthly Charges *($)*
* Total Charges *($)*
* Churn *(Yes, No)*

#### **[customer-service.csv](../../data/split/customer-service.csv)**

* Customer ID
* Gender *(Male, Female)*
* Senior Citizen *(1, 0)*
* Partner *(Yes, No)*
* Dependents *(Yes, No)*
* Tenure *(1-100)*

#### **[products.csv](../../data/split/products.csv)**

* Customer ID
* Phone Service *(Yes, No)*
* Multiple Lines *(Yes, No, No phone service)*
* Internet Service *(DSL, Fiber optic, No)*
* Online Security *(Yes, No, No internet service)*
* Online Backup *(Yes, No, No internet service)*
* Device Protection *(Yes, No, No internet service)*
* Tech Support *(Yes, No, No internet service)*
* Streaming TV *(Yes, No, No internet service)*
* Streaming Movies *(Yes, No, No internet service)*

## Agenda

|   |   |
| - | - |
| [Pre-work](pre-work/README.md) | Creating a project, downloading the data set, seeding a database |
| [Data Connection and Virtualization for Admins](db-connection-and-virtualization/README.md) | Creating a new connection, virtualizing the data, importing the data into the project |
| [Import Data to Project](addData/README.md) | Import the data into your project |
| [Data Visualization with Data Refinery](data-visualization-and-refinery/README.md) | Refining the data, vizualizing and profiling the data |
| [Enterprise data governance for Viewers using Watson Knowledge Catalog](watson-knowledge-catalog-user/README.md) | Use and Enterprise data catalog to search, manage, and protect data |
| [Enterprise data governance for Admins using Watson Knowledge Catalog](watson-knowledge-catalog-admin/README.md) | Create new Categories, Business terms, Policies and Rules in Watson Knowledge Catalog |
| [Machine Learning with Jupyter](machine-learning-in-Jupyter-notebook/README.md) | Building a model with Spark, deploying the model with Watson Maching Learning, testing the model with a Python Flask app |
| [Machine Learning with AutoAI](machine-learning-autoai/README.md) | Use AutoAi to quickly generate a Machine Learning pipeline and model |
| [Deploy and Test Machine Learning Models](machine-learning-deployment-scoring/README.md) | Deploy and machine learning models using several approaches |
| [Monitoring models with OpenScale GUI (Fastpath Monitoring)](openscale-fastpath/README.md) | Quickly deploy an OpenScale demo with FastPath |
| [Monitoring models with OpenScale GUI (Manual Config)](openscale-gui-manual-config/README.md) | Use the OpenScale tool to monitor deployed machine learning models |
| [Monitoring models with OpenScale (Notebook)](openscale-notebook/README.md) | See the OpenScale APIs in a Jupyter notebook and manually configure the monitors |

## Compatability

This workshop has been tested on the following platforms:

* **macOS**: Mojave (10.14), Catalina (10.15)

## About Cloud Pak for Data

Cloud Pak for Data represents an all-in-one platform for all your data needs. Cloud Pak for data tries to eliminate silos between Architect, Data Scientist, Developer, and Data Stewards. Cloud Pak for Data helps to streamline work by creating a pipeline for collecting, organizing, analyzing, and consuming data.

![Cloud Pak for Data pipeline](.gitbook/assets/images/generic/cp4data.png)

### A few other noteworthy mentions

Cloud Pak for Data:

* ... has a [new CP4D 2.5 version](https://www.ibmbigdatahub.com/blog/announcing-cloud-pak-for-data-2-5)
* ... is installed on Red Hat OpenShift providing an enterprise quality container platform
* ...you can choose the services that you want to run on Cloud Pak for Data. This means you are running only the services that are important for your line of business.
* ...you can extend the functionality of IBM Cloud Pak for Data by installing services and by integrating Cloud Pak for Data with other applications.
* ... added [Services](http://rhea.svl.ibm.com:9081/support/knowledgecenter/SSQNUZ_2.5.0/cpd/svc/services.html) include:
  * Watson Assistant
  * Watson OpenScale
  * R Studio
  * Data Virtualization
  * any many more
* ... can be deployed on any major cloud provider (IBM, AWS, Azure, GCP)
* ... provides a free 7-day trial -- [Cloud Pak Experience](https://www.ibm.com/cloud/garage/cloud-pak-experiences/)

![Cloud Pak for Data stack](.gitbook/assets/images/generic/cpd-stack.png)

## Credits

This workshop was primarily written by [Scott D'Angelo](https://github.com/scottdangelo) and [Steve Martinelli](https://github.com/stevemar). Many other IBMers have contributed to help shape, test, and contribute to the workshop. Special thanks to [Rick Buglio](rbuglio@us.ibm.com) and team for the great Watson Knowledge Catalog demo.

* [Omid Meh](https://github.com/omidmeh)
* [Javier Torres](https://github.com/jrtorres)
* [Samaya Madhavan](https://github.com/samayamadhavan)
* [Rick Buglio](rbuglio@us.ibm.com)
