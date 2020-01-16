# Watson Knowledge Catalog

This exercise demonstrates how to solve the problems of enterprise data governance using Watson Knowledge Catalog on the Cloud Pak for Data platform. We'll explain how to use governance, data quality and active policy management in order to help your organization protect and govern sensitive data, trace data lineage and manage data lakes. This knowledge will help users quickly discover, curate, categorize and share data assets, data sets, analytical models and their relationships with other members of your organization. It serves as a single source of truth for data engineers, data stewards, data scientists and business analysts to gain self-service access to data they can trust.

This section is comprised of the following steps:

1. [Set up Catalog and Data](#1-set-up-catalog-and-data)
1. [Add collaborators and control access](#2-add-collaborators-and-control-access)

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
