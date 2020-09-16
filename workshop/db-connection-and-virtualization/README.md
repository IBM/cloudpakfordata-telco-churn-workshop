# DB Connection and Virtualization

This section requires a Data Engineer role to be assigned to your user account.

## Virtualize Tables

In this section, since we now have access to the Db2 data store, we will virtualize the data in our Cloud Pak for Data project.

* To launch the data virtualization tool, go the (☰) menu and click `Collect` and then `Data Virtualization`.

  ![(☰) Menu -> Collect -> Data Virtualization](../.gitbook/assets/images/dv/dv-menu.png)

* Click on the *Data sources* pulldown and choose *Virtualize*.

  ![Menu -> Virtualize](../.gitbook/assets/images/dv/dv-virtualize-menu.png)

* Several tables names will be displayed (many of these tables are created as sample data when a Db2 Warehouse instance is provisioned). Find the tables we will be using for this workshop: `CUSTOMER`, `PRODUCT` and `BILLING` (You can search using the Schema name (`NULLIDRA`) for the tables and they should show up). Once selected click on *Add to cart* and then on *View Cart*. :

  ![Choose the tables to virtualize](../.gitbook/assets/images/dv/dv-virtualize-tables.png)

* The next panel prompts the user to select where to assign the virtualized tables. Select the `My virtualized data` radio button. If there is a `Submit to catalog` checkbox on the top right, unselect it and finally click the *Virtualize* button to add the virtualized tables to your data.

  ![Add virtualized data to your project](../.gitbook/assets/images/dv/dv-virtualize-assign.png)

* You'll be notified that the virtual tables have been created. Let's see the new virtualized tables from the Data Virtualization tool by clicking *View my virtualized data* button.

  ![We've got virtualized data](../.gitbook/assets/images/dv/dv-virtualize-complete.png)

## Join the virtualized data

Now we're going to **join** the tables we created so we have a merged set of data. It will be easier to do it here rather than in a notebook where we'd have to write code to handle three different data sets.

* Click on any two tables (`PRODUCTS` and `BILLING` for instance) and click the *Join view* button.

  ![Choose to join two tables](../.gitbook/assets/images/dv/dv-data-join-overview.png)

* To join the tables we need to pick a key that is common to both data sets. Here we choose to map `customerID` from the first table to `customerID` on the second table. Do this by clicking on one and dragging it to another. When the line is drawn click on *Next*.

  ![Map the two customerID keys](../.gitbook/assets/images/dv/dv-data-join-columns.png)

* Next, you have a chance to `Edit column names`. We'll keep them as-is. Click `Next`.

  ![Review the proposed joined table](../.gitbook/assets/images/dv/dv-data-join-review.png)

* In the next panel we'll give our joined data a unique name (to be consistent with SQL standards, pick an all uppercase name), I chose `XXXBILLINGPRODUCTS` (where `XXX` is my *All Upper Case* user ID). Under *Assign to*, we choose where to assign the joined view we created. Select the `My virtualized data` radio button. If there is a `Submit to catalog` checkbox on the top right, unselect it and finally click the *`Create view`* button to add the virtualized aggregate table to your data.

  ![Add joined data tables to your project](../.gitbook/assets/images/dv/dv-data-join-assign.png)

* You'll be notified that the join view creation has succeeded! Click on the *View my virutalized data* button.

  ![The data join succeeded!](../.gitbook/assets/images/dv/dv-data-join-created.png)

* You will need to repeat this again until we have joined all three tables.

* **IMPORTANT** Repeat the same steps as above, but this time choose to join the new joined view (`XXXBILLINGPRODUCTS`) and the last virtualized table (`CUSTOMERS`) to create a new joined view that has all three tables. Let's call it `XXXBILLINGPRODUCTSCUSTOMERS`. Switching to our project should show all three virtualized tables, and two joined tables. Do not go to the next section until this step is performed.

  ![Our data sets at the end of this section](../.gitbook/assets/images/dv/dv-project-data-all.png)

## Conclusion

In this section we learned how to make connection to databases that contain our data, how to virtualize them, and how to allow other to collaborate with us and use the virtualized data. Remember that you can add data from different databases and servers if you need to. Moreover, you can virtualize this data from different sources together as well! The goal is to take care of bringing the data to the platform early on so all the data scientists can use it without reinventing the wheel while you keep full control of who has access to what data.
