# Exercise 1: Data Analysis

This section is broken up into the following steps:

1. [Add a new Data Source connection](#1-add-a-new-data-source-connection)
1. [Virtualize Db2 data with Data Virtualization](#2-virtualize-db2-data-with-data-virtualization)
1. [Visualize data with Cognos Dashboards](#3-visualize-data-with-cognos-dashboards)

## 1. Add a new Data Source connection

For Cloud Pak for Data to read our Db2 Warehouse data we need to add a new *Data Source* to Cloud Pak for Data. This requires inputting the usual JDBC details.

To add a new data source, go to the (☰) menu and click on the *Connections* option.

![(☰) Menu -> Collections](../.gitbook/assets/images/connections/cpd-conn-menu.png)

At the empty overview, click *Add connection*.

![No connections, yet.](../.gitbook/assets/images/connections/conn-1-overview-empty.png)

Start by giving your new *Connection* a name and select *Db2 Warehouse on Cloud* as your connection type. More fields should apper. Fill the new fields with the same credentials for your own Db2 Warehouse connection from the previous section (or ask your instructor for shared credentials).

![Add a Db2 Warehouse on Cloud connection](../.gitbook/assets/images/connections/conn-2-details.png)

The new connection will be listed in the overview.

![Connection has been added!](../.gitbook/assets/images/connections/conn-3-overview-db2.png)

> **IMPORTANT**: A note to the instructors of this workshop. At this point go to the *Virtualized Data* option and grant at least *Steward* access to all users participating in the workshop.

![Grant access to the data virtualization tool](../.gitbook/assets/images/dv/dv-0-grant-access.png)

## 2. Virtualize Db2 data with Data Virtualization

For this section we'll now use the Data Virtualization tool to import the data from Db2 Warehouse, which is now exposed as an Connection in Cloud Pak for Data.

### Add a Data Source to Data Virtualization

To launch the data virtualization tool, go the (☰) menu and click *Collect* and then *Virtualized data*.

![(☰) Menu -> Collect -> Virtualized data](../.gitbook/assets/images/dv/cpd-dv-menu.png)

At the empty overview, click *Add* and choose *Add remote connector*.

![No data sources, yet](../.gitbook/assets/images/dv/dv-data-sources-1-empty.png)

Select the data source we made in the previous step, and click *Next*.

![Add the Db2 Warehouse connection](../.gitbook/assets/images/dv/dv-data-sources-2-add.png)

The new connection will be listed as a data source for data virtualization.

![Db2 Warehouse connection is now associated with Data Virtualization](../.gitbook/assets/images/dv/dv-data-sources-3-shown.png)

### Start virtualizing data

In this section, since we now have access to the Db2 Warehouse data, we can virtualize the data to our Cloud Pak for Data project. Click on the *Menu* button and choose *Virtualize*.

![Menu -> Virtualize](../.gitbook/assets/images/dv/dv-virtualize-1-menu.png)

Several tables will appear (many are created as sample data when a Db2 Warehouse instance is provisioned) in the table. Find the tables you created earlier, the instructions suggested naming them: `CUSTOMER`, `PRODUCT` and `BILLING`. Once selected click on *Add to cart* and then on *View Cart*.

![Choose the tables to virtualize](../.gitbook/assets/images/dv/dv-virtualize-2-tables.png)

The next panel prompts the user to choose which project to assign the data to, choose the project you created in the previous exercise. Click *Virtualize* to start the process.

![Add virtualized data to your project](../.gitbook/assets/images/dv/dv-virtualize-3-assign.png)

You'll be notified that the virtual tables have been created! Let's see the new virtualized data from the Data Virtualization tool by clicking *View my data*.

![Ta da! We've got virtualized data](../.gitbook/assets/images/dv/dv-virtualize-4-complete.png)

### Join the virtualized data

Now we're going to **join** the tables we created so we have a merged set of data. It will be easier to do it here rather than in a notebook where we'd have to write code to handle three different data sets. Click on any two tables (`PRODUCTS` and `BILLING` for instance) and click the *Join view* button.

![Choose to join two tables](../.gitbook/assets/images/dv/dv-data-join-1-overview.png)

To join the tables we need to pick a key that is common to both data sets. Here we choose to map `customerID` from the first table to `customerID` on the second table. Do this by clicking on one and dragging it to another. When the line is drawn click on *Join*.

![Map the two customerID keys](../.gitbook/assets/images/dv/dv-data-join-2-columns.png)

In the next panel we'll give our joined data a name, I chose `billing+products`, then review the joined table to ensure all columns are present and only one `customerID` column exists. Click *Next* to continue.

![Review the proposed joined table](../.gitbook/assets/images/dv/dv-data-join-3-review.png)

Next we choose which project to assign the joined view to, choose the project you created in the previous exercise. Click *Create view* to start the process.

![Add joined data tables to your project](../.gitbook/assets/images/dv/dv-data-join-4-assign.png)

You'll be notified that the join has succeeded! Click on *View my data*. to repeat this again so we have all three tables.

![The data join succeeded!](../.gitbook/assets/images/dv/dv-data-join-5-created.png)

**IMPORTANT** Repeat the same steps as above, but this time choose to join the new joined view (`billing+products`) and the last virtualized table (`CUSTOMERS`), to create a new joined view that has all three tables, let's call it `billing+products+customers`. Switching to our project should show all three virtualized tables, and two joined tables. Do not go to the next section until this step is performed.

![Our data sets at the end of this section](../.gitbook/assets/images/dv/dv-project-data-all.png)

## 3. Visualize data with Cognos Dashboards

The Cognos Dashboards tool provides intuitive options to building visualization quickly. In this part of the workshop we'll use Cognos Dashboards to create a few graphs and charts that help us summarize our data.
