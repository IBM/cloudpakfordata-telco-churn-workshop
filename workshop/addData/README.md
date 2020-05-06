# Importing data in your projects

There are many ways to bring your data into your project, in this section we'll cover using from the following data sources:

* Using virtualized data

## Using Virtualized Data

For this section we'll now use the Data Virtualization tool to import the data from Db2 Warehouse, which is now exposed as an Connection in Cloud Pak for Data.

### Assign the data to your project

From the upper-left (☰) hamburger menu, click on *Collect* -> *Data Virtualization*, you'll be brought to the *My data* section. Here you should see the data you can access (or that the administrator has assigned to you). Choose the data sets available and click *Assign* to start importing it to your project.

> _Note: The name of the data assets to select may vary based on names chosen during data virtualization. The default names to select are: BILLING, PRODUCTS, CUSTOMERS, BILLINGPRODUCTS AND BILLINGPRODUCTSCUSTOMER_

![Select the data you want to import](../.gitbook/assets/images/dv/dv-8-select-data.png)

From here, choose the project you previously created.

![Assign the data to a project](../.gitbook/assets/images/dv/dv-9-assign.png)

Switching to our project should show the original virtualized tables, and joined tables. Do not go to the next section until this step is performed.

![Our data sets at the end of this section](../.gitbook/assets/images/dv/dv-project-data-all.png)
