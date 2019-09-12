# Pre-work

## Setting up a project

> **IMPORTANT** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

Log into Cloud Pak for Data.

![](../.gitbook/assets/manage/cpd-login.png)

Go the hamburger menu and click *Projects*

![](../.gitbook/assets/manage/cpd-projects-menu.png)

Click on *New project*

![](../.gitbook/assets/manage/cpd-new-project.png)

Create a new project, give it a unique name.

![](../.gitbook/assets/manage/cpd-new-project-name.png)

## About the data set

The data set used for this workshop is derived from [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn). It is originally from Watson Analytics, and looks at customer churn for a Telecommunication company. The data is split into three CSV files and are located in the [data](../../data) directory of this repository.

**[billing.csv](billing.csv)**

This file has the following attributes:

* Customer ID
* Amount $

**[customer-service.csv](customer-service.csv)**

* Customer ID
* Senior, Y/N

**[products.csv](products.csv)**

* Customer ID
* Has cable, Y/N

## (Optional) Seeding our Db2 database

> **NOTE** If you do not wish to perform this step, your instructor will provide you credentials for a Db2 Warehouse instance.

Log into (or sign up for) [IBM Cloud](https://cloud.ibm.com).

![](../.gitbook/assets/images/generic/ibm-cloud-dashboard.png)

Create a [Db2 Warehouse](https://cloud.ibm.com/catalog/services/db2-warehouse) service on IBM Cloud. Choose the `Entry` plan as it is compatible with a `Lite` account.

![](../.gitbook/assets/images/db2/db2-1-provision.png)

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
  | ![](../.gitbook/assets/images/db2/db2-8-csv-config-products.png) |

Back on IBM Cloud, check credentials

  ![](../.gitbook/assets/images/db2/db2-cloud-credentials.png)
