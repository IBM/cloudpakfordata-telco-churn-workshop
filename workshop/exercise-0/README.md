# Pre-work

## Setting up a project

> **IMPORTANT** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

1. Log into Cloud Pak for Data.

   ![](../.gitbook/assets/project/login.png)

1. Go the hamburger menu and click *Projects*

1. Create a new project, give it a unique name.

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

1. Log into (or sign up for) [IBM Cloud](https://cloud.ibm.com).

1. Create a [Db2 Warehouse](https://cloud.ibm.com/catalog/services/db2-warehouse) service on IBM Cloud. Choose the `Entry` plan as it is compatible with a `Lite` account.

1. Once created click on *Open Console*.

   ![db2-1-cloud-launch](../.gitbook/assets/db2/db2-1-cloud-launch.png)

1. overview

  ![db2-2-console-overview](../.gitbook/assets/db2/db2-2-console-overview.png)

1. Load csv

  ![db2-3-csv-find](../.gitbook/assets/db2/db2-3-csv-find.png)

1. config?

  ![db2-4-csv-config](../.gitbook/assets/db2/db2-4-csv-config.png)

1. start loading

  ![db2-5-csv-preload](../.gitbook/assets/db2/db2-5-csv-preload.png)

1. loaded

  ![db2-6-csv-loaded](../.gitbook/assets/db2/db2-6-csv-loaded.png)

1. extra options with customers and products

  |   |   |
  | - | - |
  | ![db2-7-csv-config-customers](../.gitbook/assets/db2/db2-7-csv-config-customers.png) | ![db2-8-csv-config-products](../.gitbook/assets/db2/db2-8-csv-config-products.png) |

1. Back on IBM Cloud, check credentials

  ![db2-cloud-credentials](../.gitbook/assets/db2/db2-cloud-credentials.png)
