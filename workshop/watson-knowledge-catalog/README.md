# Watson Knowledge Catalog

This exercise demonstrates how to solve the problems of enterprise data governance using Watson Knowledge Catalog on the Cloud Pak for Data platform. We'll explain how to use governance, data quality and active policy management in order to help your organization protect and govern sensitive data, trace data lineage and manage data lakes. This knowledge will help users quickly discover, curate, categorize and share data assets, data sets, analytical models and their relationships with other members of your organization. It serves as a single source of truth for data engineers, data stewards, data scientists and business analysts to gain self-service access to data they can trust.

This section is comprised of the following steps:

1. [Set up Catalog and Data](#1-set-up-catalog-and-data)
1. [Add collaborators and control access](#2-add-collaborators-and-control-access)
1. [Add Business terms](#3-add-business-terms)

## 1. Set up Catalog and Data

First we'll create a catalog and load some data

### Create the catalog

Open Watson Knowledge Catalog by clicking the *Services* icon at the top right of the home page:

![click services icon](../.gitbook/assets/images/wkc/wkc-click-services-icon.png)

Under the *Data Governance* section, click the 3 horizontal dots and click `Open`:

![open wkc](../.gitbook/assets/images/wkc/wkc-open-service.png)

From the *Your catalogs* page, click either `Create catalog` or `New Catalog`:

![create WKC catalog](../.gitbook/assets/images/wkc/wkc-create-catalog.png)

Give your catalog a name and optional description, and click `create`:

![name and create wkc catalog](../.gitbook/assets/images/wkc/wkc-name-describe-create.png)

### Add data assets

Under the *Browse Assets* tab, below "Now you can add assets!" click `here` to add your data:

![click here to add assets](../.gitbook/assets/images/wkc/wkc-add-data-asset.png)

*OR* you can click `+ Add to catalog` in the top right and choose `Local files`:

![add local files to catalog](../.gitbook/assets/images/wkc/wkc-add-to-catalog-local-files.png)

Browse to the `/data/merged/Telco-Customer-Churn.csv` file and double-click or click `Open`. Add an optional description and click `Add`:

![click add for local files to catalog](../.gitbook/assets/images/wkc/wkc-file-selected-now-add.png)

>NOTE: Stay in the catalog until loading is complete! If you leave the catalog, the incomplete asset will be deleted.

The newly added *Telco-Customer-Churn.csv* file will show up under the *Browse Assets* tab of your catalog:

![newly added data in catalog](../.gitbook/assets/images/wkc/wkc-browse-assets.png)

## 2. Add collaborators and control access

Under the *Access Control* tab you can click `Add Collaborator` to give other users access to your catalog:

![give users access to the catalog](../.gitbook/assets/images/wkc/wkc-access-control-add-collaborator.png)

You can search for a user, click on the name to select them, and click `Add`:

![search for user and add as collaborator](../.gitbook/assets/images/wkc/wkc-choose-user-and-add.png)

You can choose a role for the user - Admin, Editor, or Viewer:

![choose role for collaborator](../.gitbook/assets/images/wkc/wkc-user-roll-choice.png)

To access data in the catalog, click on the name of the data:

![click data name to open](../.gitbook/assets/images/wkc/wkc-click-data-name-to-open.png)

A preview of the data will open, with metadata and the first few rows:

![preview of data](../.gitbook/assets/images/wkc/wkc-data-preview.png)

You can click the `Review` tab and rate the data, as well as comment on it, to provide feedback for your teammates:

![review data](../.gitbook/assets/images/wkc/wkc-review-data.png)

## 3. Add Business terms

You can use [Business terms](https://dataplatform.cloud.ibm.com/docs/content/wsj/governance/dmg16.html) to standardize definitions of business concepts so that your data is described in a uniform and easily understood way across your enterprise.

From the upper-left (☰) hamburger menu, choose `Organize` -> `Data and AI Governance` -> `Business terms`:

![organize Data Business terms](../.gitbook/assets/images/wkc/wkc-organize-data-business-terms.png)

Click on the upper-right `+ Create Business term` button:

![create business term](../.gitbook/assets/images/wkc/wkc-create-business-term)

Give the new Business term a name such as *Billing* and optional description, and click `Save as draft`. NOTE that others on the platform will be creating a business term for this workshop, so perhaps pre-pend your term with something unique, i.e *scottda-Billing*:

![name new business term](../.gitbook/assets/images/wkc/wkc-name-new-business-term.png)

A window will come up once the term is created. You can see a rich set of options for creating related terms and adding other metadata. For now, click `Publish` to make this term available to users of the platform:

![publish business term](../.gitbook/assets/images/wkc/wkc-publish-business-term.png)

Add an optional comment and click `Publish` in the new window:

![verify publish business term](../.gitbook/assets/images/wkc/wkc-click-publish.png)

Now go back to your Telco catalog and open it up to the column view ((☰) hamburger menu `Organize` -> `All catalogs` and choose `Telco catalog`). Under the *Browse assets* tab, click on the data set *Telco-Customer-Churn.csv* to get the column/row preview. Scroll right to get to the *TotalCharges* column and click the *Column information* icon (looks like an "eye"):

![choose TotalCharges column information](../.gitbook/assets/images/wkc/wkc-totalcharges-column-information.png)

In the window that opens, click the *edit* icon (looks like a "pencil") next to *Business terms* :

![edit business terms](../.gitbook/assets/images/wkc/wkc-assign-terms-to-column.png)

Enter *Billing* (or your uniquely named term such as *scottda-Billing*) under *Business terms* and the term will be searched for. Click on the `Billing` term that is found, and click `Apply`:

![edit business terms](../.gitbook/assets/images/wkc/wkc-search-billing-to-assign-term.png)

Close that window once the term has been applied.
Now, do the same thing to add the *Billing* Business term to the *MonthlyCharges* column.

You will now be able to search for these terms from within the platform. For example, going back to your top level *Telco Catalog*, in the search bar with the comment "What assets are you searching for?" enter your unique *<unique_string>Billing* term:

![search using business terms](../.gitbook/assets/images/wkc/wkc-search-business-terms.png)

The *Telco-Customer-Churn.csv* data set will show up, since it contains columns tagged with the *Billing* business term.
