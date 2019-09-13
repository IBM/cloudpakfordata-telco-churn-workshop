# Exercise 1: Data Analysis

This section is broken up into the following steps:

1. [Add a new Data Source connection](#add-a-new-data-source-connection)
1. [Virtualize Db2 data with Data Virtualization](#virtualize-db2-data-with-data-virtualization)
1. [Visualize data with Cognos Dashboards](#visualize-data-with-cognos-dashboards)

## Add a new Data Source connection

To add a new data source, go the (☰) menu and click on the *Connections* option.

![(☰) Menu -> Collections](../.gitbook/assets/images/connections/cpd-conn-menu.png)

At the empty overview, click *Add connection*.

![No connections, yet.](../.gitbook/assets/images/connections/conn-1-overview-empty.png)

Start by giving your new *Connection* a name and select *Db2 Warehouse on Cloud* as your connection type. More fields should apper. Fill the new fields with the same credentials for your own Db2 Warehouse connection from the previous section (or ask your instructor for shared credentials).

![Add a Db2 Warehouse on Cloud connection](../.gitbook/assets/images/connections/conn-2-details.png)

The new connection will be listed in the overview.

![Connection has been added!](../.gitbook/assets/images/connections/conn-3-overview-db2.png)

## Virtualize Db2 data with Data Virtualization

To launch the data virtualization tool, go the (☰) menu and click *Collect* and then *Virtualized data*.

![(☰) Menu -> Collect -> Virtualized data](../.gitbook/assets/images/dv/cpd-dv-menu.png)

At the empty overview, click *Add* and choose *Add remote connector*.

![No data sources, yet](../.gitbook/assets/images/dv/dv-data-sources-1-empty.png)

Select the data source we made in the previous step, and click *Next*.

![Add the Db2 Warehouse connection](../.gitbook/assets/images/dv/dv-data-sources-2-add.png)

The new connection will be listed as a data virtualization option.

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

TBD
