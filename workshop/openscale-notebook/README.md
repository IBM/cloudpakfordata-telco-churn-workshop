# Configure OpenScale in a Jupyter Notebook

There are several ways of configuring Watson OpenScale to monitor machine learning deployments, including the automatic configuration, using the GUI tool, a more manual configuration using the APIs, and some combintation of these. For this exercise we're going to configure our OpenScale service by running a Jupyter Notebook. This provides examples of using the OpenScale Python APIs programatically.

This lab is comprised of the following steps:

1. [Open the notebook](#1-open-the-notebook)
2. [Update credentials](#2-update-credentials)
3. [Run the notebook](#3-run-the-notebook)
4. [Get transactions for Explainability](#4-get-transactions-for-explainability)

## 1. Open the notebook

If you [Created the Project](https://ibm-developer.gitbook.io/cloudpakfordata-telco-workshop/getting-started/pre-work#2-create-a-project-and-deployment-space) using the [Customer-Churn-Project.zip](https://github.ibm.com/IBMDeveloper/cp4d-workshop-telco-churn/tree/master/projects/Customer-Churn-Project.zip) file, your notebook will be present in that project, under the `Assets` tab:

![Project from zip assets tab](../images/aios/aios-notebook-zip-file-asset.png)

You may now skip to the next step [Update credentials](#2-update-credentials)

## Import the notebook (If you are not using the Project Import pre-work steps)

> NOTE: You should probably not need this step, and should only perform it if instructed to.

If, for some reason, you have not followed the [Create a Project and Deployment Space](https://ibm-developer.gitbook.io/cloudpakfordata-telco-workshop/getting-started/pre-work#2-create-a-project-and-deployment-space) step in the Pre-work to import [Customer-Churn-Project.zip](https://github.ibm.com/IBMDeveloper/cp4d-workshop-telco-churn/tree/master/projects/Customer-Churn-Project.zip), then you will need to import the notebook file by itself. Use the following steps for that.

At the project overview click the *Add to project* button, and choose *Notebook* or click *New notebook* option next to the Notebooks section.

![Add a new asset](../images/wml/wml-1-add-asset.png)

On the next panel select the *From URL* tab, give your notebook a name, provide the following URL, and choose the Python 3.6 environment:

```bash
https://raw.githubusercontent.com/IBM/cloudpakfordata-telco-churn-workshop/master/notebooks/openscale-full-configuration.ipynb
```

> The notebook is hosted in the same repo as [the workshop](https://github.com/IBM/cloudpakfordata-telco-churn-workshop).
>
> * **Notebook**: [openscale-full-configuration.ipynb](https://raw.githubusercontent.com/IBM/cloudpakfordata-telco-churn-workshop/master/notebooks/openscale-full-configuration.ipynb)
> * **Notebook with output**: [openscale-full-configuration-with-output.ipynb](https://raw.githubusercontent.com/IBM/cloudpakfordata-telco-churn-workshop/master/notebooks/with-output/openscale-full-configuration-with-output.ipynb)

![Add notebook name and URL](../images/wml/wml-2-add-name-and-url.png)

When the Jupyter notebook is loaded and the kernel is ready then we can start executing cells.

![Notebook loaded](../images/aios/OpenScaleNotebook.png)

### 2. Update credentials

* In the notebook section 1.2 you will add your ICP platform credentials for the `WOS_CREDENTIALS`.
* For the `url` field, change `https://w.x.y.z` to use the URL your ICP cluster, i.e something like: `"url": "https://zen-cpd-zen.omid-cp4d-v5-2bef1f4b4097001da9502000c44fc2b2-0001.us-south.containers.appdomain.cloud"`.
* For the `username`, use your login username.
* For the `password`, user your login password.

### 3. Run the notebook

> **Important**: *Make sure that you stop the kernel of your notebook(s) when you are done, in order to prevent leaking of memory resources!*

![Stop kernel](../images/wml/JupyterStopKernel.png)

Spend an minute looking through the sections of the notebook to get an overview. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook. While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

### 4. Get transactions for Explainability

Under `8.9 Identify transactions for Explainability` run the cell. It will produce a series of UIDs for indidvidual ML scoring transactions. Copy one or more of them to examine in the next section.
