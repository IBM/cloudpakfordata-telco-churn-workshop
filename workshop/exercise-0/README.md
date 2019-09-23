# Pre-work

This section is broken up into the following steps:

1. [Clone the repo](#1-clone-the-repo)
1. [About the data set](#2-about-the-data-set)
1. [(Optional) Seeding our Db2 Warehouse database](#3-optional-seeding-our-db2-warehouse-database)
1. [Creating a new Cloud Pak for Data project](#4-creating-a-new-cloud-pak-for-data-project)

## 1. Clone the repo

Various parts of this workshop will require the attendee to upload files or run scripts that we've stored in the repository. So let's get that done early on, you'll need [`git`](https://git-scm.com) on your laptop to clone the repository directly, or access to [GitHub.com](https://github.com/) to download the zip file.

Either run the following command:

```bash
git clone https://github.com/IBM/cloudpakfordata-telco-churn-workshop
cd cloudpakfordata-telco-churn-workshop
```

Alternatively, if `git` is not supported, go to the [GitHub repo for this workshop](https://github.com/IBM/cloudpakfordata-telco-churn-workshop) and download the archived version of the workshop and extract it on your laptop.

![download workshop zip](../.gitbook/assets/images/generic/cp4d-telco-workshop-git-zip-download.png)

## 2. About the data set

The data set used for this workshop is originally from Watson Analytics and was used on a [Kaggle](https://www.kaggle.com/blastchar/telco-customer-churn) project, it contains information about customer churn for a Telecommunications company. The data is split into three CSV files and are located in the [data](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/tree/master/data/split) directory of this repository.

### **[billing.csv](../../data/split/billing.csv)**

This file has the following attributes:

* Customer ID
* Contract *(Month-to-month, one year, two year)*
* Paperless Billing *(Yes, No)*
* Payment Method *(Bank transfer, Credit card, Electronic check, Mailed check)*
* Monthly Charges *($)*
* Total Charges *($)*
* Churn *(Yes, No)*

### **[customer-service.csv](../../data/split/customer-service.csv)**

* Customer ID
* Gender *(Male, Female)*
* Senior Citizen *(1, 0)*
* Partner *(Yes, No)*
* Dependents *(Yes, No)*
* Tenure *(1-100)*

### **[products.csv](../../data/split/products.csv)**

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

## 3. (Optional) Seeding our Db2 Warehouse database

We'll need a place to store our data. For this workshop we've opted to use Db2 Warehouse on IBM Cloud for a few reasons: it simulates a realistic enterprise database, a free tier is provided by IBM Cloud, and we can easily load our data set.

> **NOTE** If you do not wish to perform this step, your instructor will provide you credentials for a Db2 Warehouse instance.

### Log in and provision a Db2 Warehouse database

Log into (or sign up for) [IBM Cloud](https://cloud.ibm.com).

![IBM Cloud login](../.gitbook/assets/images/generic/ibm-cloud-sign-up.png)

From the dashboard click on the *Create resource* button to go to the *Catalog*.

![IBM Cloud Dashboard](../.gitbook/assets/images/generic/ibm-cloud-dashboard.png)

Find the [Db2 Warehouse](https://cloud.ibm.com/catalog/services/db2-warehouse) tile from the *Database* section.

![Db2 Warehouse in the Catalog](../.gitbook/assets/images/db2/db2-0-catalog.png)

Choose the `Entry` plan as it is compatible with a `Lite` account.

> **NOTE**: There may be a message indicating the service will be charged, please disregard that message as there is no charge for staying under 1 GB of data.

![Entry level plan](../.gitbook/assets/images/db2/db2-0-pricing.png)

Once the Db2 Warehouse service is created click on *Open Console*.

![A Db2 Warehouse instance has been provisioned](../.gitbook/assets/images/db2/db2-1-cloud-launch.png)

You'll be directed to a Db2 web console dashboard where you can load data by clicking the *Load* button.

### Load the Db2 Warehouse database

![The Db2 Warehouse console](../.gitbook/assets/images/db2/db2-2-console-overview.png)

Select the [`billing.csv`](../../data/split/billing.csv) file in the [data](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/tree/master/data/split) folder.

![Find data to load](../.gitbook/assets/images/db2/db2-3-csv-find.png)

On the next panel we configure where the data will go in the database. We'll use the schema that was created for our database, it'll look like *DASHXXXX* where *XXXX* is a randomly generated number. Select that and click `+ New Table` and give it the name `Billing` to create a new table.

![Select a table name](../.gitbook/assets/images/db2/db2-4-csv-config.png)

Accept the defaults on the next screen and click `Next`.

![Keep all defaults](../.gitbook/assets/images/db2/db2-keep-defaults.png)

On the next panel click *Begin Load* to start loading the data.

![Begin loading the data](../.gitbook/assets/images/db2/db2-5-csv-preload.png)

Verify all the rows were loaded. Click `Load More Data` to continue.

![Data has been loaded!](../.gitbook/assets/images/db2/db2-6-csv-loaded.png)

Repeat the process for [`products.csv`](../../data/split/products.csv) and [`customer-service.csv`](../../data/split/customer-service.csv), call these tables `PRODUCTS` and `CUSTOMERS`. Note that there will be an additional panel to configure data, the defaults are accetable.

![Repeat the process for the other data sets](../.gitbook/assets/images/db2/db2-8-csv-config-products.png)

### Jot down the credentials

Before we go to Cloud Pak for Data, we need to create credentials for our Db2 Warehouse by going back to our service, clicking on the *Service credentials* button, and creating a new credential. Copy these down somewhere as we'll need them in the next section.

![Db2 Warehouse credentials](../.gitbook/assets/images/db2/db2-cloud-credentials.png)

```yaml
{
  "hostname": "dashdb-entry-yp-dal09-08.services.dal.bluemix.net",
  "password": "c4Fn_Pl_B7jG",
  "https_url": "https://dashdb-entry-yp-dal09-08.services.dal.bluemix.net:8443",
  "port": 50000,
  "ssldsn": "DATABASE=BLUDB;HOSTNAME=dashdb-entry-yp-dal09-08.services.dal.bluemix.net;PORT=50001;PROTOCOL=TCPIP;UID=dash100239;PWD=c4Fn_Pl_B7jG;Security=SSL;",
  "host": "dashdb-entry-yp-dal09-08.services.dal.bluemix.net",
  "jdbcurl": "jdbc:db2://dashdb-entry-yp-dal09-08.services.dal.bluemix.net:50000/BLUDB",
  "uri": "db2://dash100239:c4Fn_Pl_B7jG@dashdb-entry-yp-dal09-08.services.dal.bluemix.net:50000/BLUDB",
  "db": "BLUDB",
  "dsn": "DATABASE=BLUDB;HOSTNAME=dashdb-entry-yp-dal09-08.services.dal.bluemix.net;PORT=50000;PROTOCOL=TCPIP;UID=dash100239;PWD=c4Fn_Pl_B7jG;",
  "username": "dash100239",
  "ssljdbcurl": "jdbc:db2://dashdb-entry-yp-dal09-08.services.dal.bluemix.net:50001/BLUDB:sslConnection=true;"
}
```

## 4. Creating a new Cloud Pak for Data project

At this point of the workshop we will be using Cloud Pak for Data for the remaining steps.

### Log into Cloud Pak for Data

Launch a browser and naviate to your Cloud Pak for Data deployment

> **NOTE** Your instructor will provide a URL and credentials to log into Cloud Pak for Data!

![Cloud Pak for Data login](../.gitbook/assets/images/manage/cpd-login.png)

### Create a new project

Go the (☰) menu and click *Projects*

![(☰) Menu -> Projects](../.gitbook/assets/images/manage/cpd-projects-menu.png)

Click on *New project*

![Start a new project](../.gitbook/assets/images/manage/cpd-new-project.png)

Create a new project, choose `Analytics project`, give it a unique name, and click *OK. Click `Create` on the next screen.

![Pick a name](../.gitbook/assets/images/manage/cpd-new-project-name.png)
