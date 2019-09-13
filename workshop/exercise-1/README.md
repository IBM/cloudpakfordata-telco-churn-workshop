# Exercise 1: Data Analysis

## Add a new Data Source connection

Go the (☰) menu and click *Connections*

![](../.gitbook/assets/images/connections/cpd-conn-menu.png)

The overview will appear

![](../.gitbook/assets/images/connections/conn-1-overview-empty.png)

Add in details about your Db2 Warehouse connection from the pre-work

![](../.gitbook/assets/images/connections/conn-2-details.png)

The new connection will be listed

![](../.gitbook/assets/images/connections/conn-3-overview-db2.png)

## Virtualize Db2 data with Data Virtualization

Go the (☰) menu and click *Collect -> Virtualized data*.

![](../.gitbook/assets/images/dv/cpd-dv-menu.png)

See the overview, there are no data sources.

![](../.gitbook/assets/images/dv/dv-data-sources-1-empty.png)

Add a data source, the one we made in the previous step.

![](../.gitbook/assets/images/dv/dv-data-sources-2-add.png)

Ta-da, now it appears

![](../.gitbook/assets/images/dv/dv-data-sources-3-shown.png)

Click on the *Virtualize* menu

![](../.gitbook/assets/images/dv/dv-virtualize-1-menu.png)

Find the `CUSTOMER`, `PRODUCT` and `BILLING` tables. Add them to your cart and click *View Cart*.

![](../.gitbook/assets/images/dv/dv-virtualize-2-tables.png)

Assign these to your project.

![](../.gitbook/assets/images/dv/dv-virtualize-3-assign.png)

Virtual tables have been created!

![](../.gitbook/assets/images/dv/dv-virtualize-4-complete.png)

Before we add that data to our project let's join all the tables so we have a complete picture.

![](../.gitbook/assets/images/dv/dv-data-join-1-overview.png)

Map `customerID` on one table to `customerID` on the other.

![](../.gitbook/assets/images/dv/dv-data-join-2-columns.png)

Review the joined table

![](../.gitbook/assets/images/dv/dv-data-join-3-review.png)

Assign it to your project

![](../.gitbook/assets/images/dv/dv-data-join-4-assign.png)

Ta-da it is done!

![](../.gitbook/assets/images/dv/dv-data-join-5-created.png)

Repeat this again for the third table. Going back to your project you should see a data set that has all three tables.

![](../.gitbook/assets/images/dv/dv-project-data-all.png)

## Visualize data with Cognos Dashboards

Instructions go here

## (Optional) Data Refinery

Instructions go here
