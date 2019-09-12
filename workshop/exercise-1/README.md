# Exercise 1: Data Analysis

## Add a new Data Source connection

1. Go the hamburger menu and click *Connections*

   ![cpd-conn-menu](../.gitbook/assets/images/connections/cpd-conn-menu.png)

1. The overview will appear

   ![conn-1-overview-empty](../.gitbook/assets/images/connections/conn-1-overview-empty.png)

1. Add in details about your Db2 Warehouse connection from the pre-work

   ![conn-2-details](../.gitbook/assets/images/connections/conn-2-details.png)

1. The new connection will be listed

   ![conn-3-overview-db2](../.gitbook/assets/images/connections/conn-3-overview-db2.png)

## Virtualize Db2 data with Data Virtualization

1. Go the hamburger menu and click *Collect -> Virtualized data*.

   ![cpd-dv-menu](../.gitbook/assets/images/dv/cpd-dv-menu.png)

1. See the overview, there are no data sources.

   ![dv-data-sources-1-empty](../.gitbook/assets/images/dv/dv-data-sources-1-empty.png)

1. Add a data source, the one we made in the previous step.

   ![dv-data-sources-2-add](../.gitbook/assets/images/dv/dv-data-sources-2-add.png)

1. Ta-da, now it appears

   ![dv-data-sources-3-shown](../.gitbook/assets/images/dv/dv-data-sources-3-shown.png)

1. Click on the *Virtualize* menu

   ![dv-virtualize-1-menu](../.gitbook/assets/images/dv/dv-virtualize-1-menu.png)

1. Find the `CUSTOMER`, `PRODUCT` and `BILLING` tables. Add them to your cart and click *View Cart*.

   ![dv-virtualize-2-tables](../.gitbook/assets/images/dv/dv-virtualize-2-tables.png)

1. Assign these to your project.

   ![dv-virtualize-3-assign](../.gitbook/assets/images/dv/dv-virtualize-3-assign.png)

1. Virtual tables have been created!

   ![dv-virtualize-4-complete](../.gitbook/assets/images/dv/dv-virtualize-4-complete.png)

1. Before we add that data to our project let's join all the tables so we have a complete picture.

   ![dv-data-join-1-overview](../.gitbook/assets/images/dv/dv-data-join-1-overview.png)

1. Map `customerID` on one table to `customerID` on the other.

   ![dv-data-join-2-columns](../.gitbook/assets/images/dv/dv-data-join-2-columns.png)

1. Review the joined table

   ![dv-data-join-3-review](../.gitbook/assets/images/dv/dv-data-join-3-review.png)

1. Assign it to your project

   ![dv-data-join-4-assign](../.gitbook/assets/images/dv/dv-data-join-4-assign.png)

1. Ta-da it is done!

   ![dv-data-join-5-created](../.gitbook/assets/images/dv/dv-data-join-5-created.png)

1. Repeat this again for the third table. Going back to your project you should see a data set that has all three tables.

   ![dv-project-data-all](../.gitbook/assets/images/dv/dv-project-data-all.png)

## Visualize data with Cognos Dashboards

Instructions go here

## (Optional) Business glossary

Instructions go here

## (Optional) Data Refinery

Instructions go here

## (Optional) Knowledge Catalog

Instructions go here
