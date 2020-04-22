
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

## Agenda

|   |   |
| - | - |
| [Pre-work](pre-work/README.md) | Creating a project, downloading the data set, seeding a database |
| [Import Data to Project](addData/README.md) | Import the data into your project |
| [Data Connection and Virtualization for Admins](db-connection-and-virtualization/README.md) | Creating a new connection, virtualizing the data, importing the data into the project |
| [Data Visualization with Data Refinery](data-visualization-and-refinery/README.md) | Refining the data, vizualizing and profiling the data |
|  [Enterprise data governance for Viewers using Watson Knowledge Catalog](watson-knowledge-catalog-user/README.md) | Use and Enterprise data catalog to search, manage, and protect data |
|  [Enterprise data governance for Admins using Watson Knowledge Catalog](watson-knowledge-catalog/README.md) | Create new Categories, Business terms, Policies and Rules in Watson Knowledge Catalog |
| [Machine Learning with Jupyter](machine-learning-in-Jupyter-notebook/README.md) | Building a model with Spark, deploying the model with Watson Maching Learning, testing the model with a Python Flask app |
|  [Machine Learning with AutoAI](autoai/README.md) | Use AutoAi to quickly generate a Machine Learning pipeline and model |
| [Monitoring models with OpenScale GUI](monitoring-models-with-openscale-gui/README.md) | Use the OpenScale tool to monitor deployed machine learning models |
* [Fastpath Monitoring models with OpenScale GUI](openscale-fastpath/README.md) | Quickly deploy an OpenScale demo with FastPath |
* [(Optional) Run OpenScale notebook code](openscale-notebook/README.md) | See the OpenScale APIs in a Jupyter notebook and manually configure the monitors |

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

This workshop was primarily written by [Scott D'Angelo](https://github.com/scottdangelo) and [Steve Martinelli](https://github.com/stevemar). Many other IBMers have contributed to help shape, test, and contribute to the workshop.

* [Omid Meh](https://github.com/omidmeh)
* [Javier Torres](https://github.com/jrtorres)
* [Samaya Madhavan](https://github.com/samayamadhavan)
