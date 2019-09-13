# Pre-work

This section is broken up into the following steps:

1. [Setting up a project](#setting-up-a-project)
1. [About the data set](#about-the-data-set)
1. [(Optional) Seeding our Db2 database](#optional-seeding-our-db2-database)

## Setting up a project

> **NOTE** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

Log into Cloud Pak for Data.

![](../.gitbook/assets/images/manage/cpd-login.png)

Go the hamburger menu and click *Projects*

![](../.gitbook/assets/images/manage/cpd-projects-menu.png)

Click on *New project*

![](../.gitbook/assets/images/manage/cpd-new-project.png)

Create a new project, give it a unique name.

![](../.gitbook/assets/images/manage/cpd-new-project-name.png)

## About the data set

The data set used for this workshop is derived from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). It is originally from Watson Analytics, and looks at customer churn for a Telecommunication company. The data is split into three CSV files and are located in the [data](../../data) directory of this repository.

**[billing.csv](billing.csv)**

This file has the following attributes:

* Customer ID
* Contract *(Month-to-month, one year, two year)*
* Paperless Billing *(Yes, No)*
* Payment Method *(Bank transfer, Credit card, Electronic check, Mailed check)*
* Monthly Charges *($)*
* Total Charges *($)*
* Churn *(Yes, No)*

**[customer-service.csv](customer-service.csv)**

* Customer ID
* Gender *(Male, Female)*
* Senior Citizen *(1, 0)*
* Partner *(Yes, No)*
* Dependents *(Yes, No)*
* Tenure *(1-100)*

**[products.csv](products.csv)**

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

## (Optional) Seeding our Db2 database

> **NOTE** If you do not wish to perform this step, your instructor will provide you credentials for a Db2 Warehouse instance.

Log into (or sign up for) [IBM Cloud](https://cloud.ibm.com).

![](../.gitbook/assets/images/generic/ibm-cloud-sign-up.png)

From the dashboard click on the catalog button.

![](../.gitbook/assets/images/generic/ibm-cloud-dashboard.png)

Find the [Db2 Warehouse](https://cloud.ibm.com/catalog/services/db2-warehouse) tile from the *Database* section.

![](../.gitbook/assets/images/db2/db2-0-catalog.png)

Choose the `Entry` plan as it is compatible with a `Lite` account.

![](../.gitbook/assets/images/db2/db2-0-pricing.png)

Once created click on *Open Console*.

![](../.gitbook/assets/images/db2/db2-1-cloud-launch.png)

overview

![](../.gitbook/assets/images/db2/db2-2-console-overview.png)

Load csv

![](../.gitbook/assets/images/db2/db2-3-csv-find.png)

config?

![](../.gitbook/assets/images/db2/db2-4-csv-config.png)

start loading

![](../.gitbook/assets/images/db2/db2-5-csv-preload.png)

loaded

![](../.gitbook/assets/images/db2/db2-6-csv-loaded.png)

extra options with customers and products

|   |   |
| - | - |
| ![](../.gitbook/assets/images/db2/db2-8-csv-config-products.png) | ![](../.gitbook/assets/images/db2/db2-8-csv-config-customers.png) |

Back on IBM Cloud, check credentials

![](../.gitbook/assets/images/db2/db2-cloud-credentials.png)
