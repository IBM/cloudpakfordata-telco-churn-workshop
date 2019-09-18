# Exercise 1: Data Analysis

This section is broken up into the following steps:

1. [Add a new Data Source connection](#1-add-a-new-data-source-connection)
1. [Assign virtualized data to your project](#2-assign-virtualized-data-to-your-project)
1. [Use Data Refinery to visualize and clean data](#3-use-data-refinery-to-visualize-and-clean-data)

## 1. Add a new Data Source connection

For Cloud Pak for Data to read our Db2 Warehouse data we need to add a new *Data Source* to Cloud Pak for Data. This requires inputting the usual JDBC details.

To add a new data source, go to the (☰) menu and click on the *Connections* option.

![(☰) Menu -> Collections](../.gitbook/assets/images/connections/cpd-conn-menu.png)

At the overview, click *Add connection*.

![Overview page](../.gitbook/assets/images/connections/conn-1-overview-empty.png)

Start by giving your new *Connection* a name and select *Db2 Warehouse on Cloud* as your connection type. More fields should apper. Fill the new fields with the same credentials for your own Db2 Warehouse connection from the previous section (or ask your instructor for shared credentials). Click `Test Connection` and, after that succeeds, click `Add`.

![Add a Db2 Warehouse on Cloud connection](../.gitbook/assets/images/connections/conn-2-details.png)

The new connection will be listed in the overview.

![Connection has been added!](../.gitbook/assets/images/connections/conn-3-overview-db2.png)

> **IMPORTANT**: A note to the instructors of this workshop. At this point go to the [Admin Guide](../admin-guide/README.md#virtualize-db2-data-with-data-virtualization) and follow the `Virtualize Db2 data with Data Virtualization` section.

## 2. Assign virtualized data

For this section we'll now use the Data Virtualization tool to import the data from Db2 Warehouse, which is now exposed as an Connection in Cloud Pak for Data.

### Assign the data to your project

From the menu click on *Collections -> Virtualized Data*, you'll be brought to the *My data* section. Here you should see the data that the administrator has assigned to you. Choose the three data sets available and click *Assign* to start importing it to your project.

![Select the data you want to import](../.gitbook/assets/images/dv/dv-8-select-data.png)

From here, choose the project you previously created.

![Assign the data to a project](../.gitbook/assets/images/dv/dv-9-assign.png)

Switching to our project should show all three virtualized tables, and two joined tables. Do not go to the next section until this step is performed.

![Our data sets at the end of this section](../.gitbook/assets/images/dv/dv-project-data-all.png)

## 3. Use Data Refinery to visualize and clean data

Before we build our model we're going to take a quick detour to the *Data Refinery* tool. Data Refinery can quickly filter and mutate data, create quick visualizations, and do other data cleansing tasks from an easy to use user interface.

### Load the *BILLING* data table into data refinery

From the *Project* home, click on *Data sets*, *TABLE*, and choose the *USER123.BILLING* table.

![Launch the BILLING table](../.gitbook/assets/images/dr/dr-1-launch-billing.png)

Data Refinery should launch and open the data like the image below:

![Data Refinery view of the BILLING table](../.gitbook/assets/images/dr/dr-2-view-billing.png)

The *Operation* button can perform many tasks related to data cleansing such as: substituting values, removing and renaming columns, converting column types, etc.

![Data Refinery operations](../.gitbook/assets/images/dr/dr-3-operations.png)

Clicking on the *Profile* tab will bring up a quick view of several histograms about the data.

![Data Refinery Profile tab](../.gitbook/assets/images/dr/dr-4-profile.png)

Clicking on the *Visualizations* tab will bring up an option to choose which columns to visualize. In this case, we'll pick *TotalCharges*. Click on *Visualize data* when ready.

![Use Data Refinery to visualize data](../.gitbook/assets/images/dr/dr-5-visualize.png)

We can quickly see the data in a histogram by default, switching between different chart types in seconds.

![See the visualization in seconds](../.gitbook/assets/images/dr/dr-6-chart.png)
