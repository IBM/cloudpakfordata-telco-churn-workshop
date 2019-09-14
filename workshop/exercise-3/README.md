# Exercise 3: Monitoring models

This section is broken up into the following steps:

1. [Configure OpenScale in a Jupyter Notebook](#1-configure-openscale-in-a-jupyter-notebook)
1. [Setup OpenScale to utilize the dashboard](#1-setup-openscale-to-utilize-the-dashboard)

## 1. Configure OpenScale in a Jupyter Notebook

We'll use a Jupyter notebook to configure OpenScale.

For this part of the exercise we're going to build a model with a Jupyter notebook, by importing our data, and creating a machine learning model by using a Random Forest Classifier.

### Import the notebook

At the project overview click the *New Asset* button, and choose *Add notebook*.

![Add a new asset](../.gitbook/assets/images/wml/wml-1-add-asset.png)

On the next panel select the *From URL* tab, give your notebook a name, provide the following URL, and choose the Python 3.6 environment:

```bash
https://raw.githubusercontent.com/IBM/cloudpakfordata-telco-churn-workshop/master/notebooks/ConfigureOpenScale.ipynb
```

> The notebook is hosted in the same repo as [the workshop](https://github.com/IBM/cloudpakfordata-telco-churn-workshop).
>
> * **Notebook**: [ConfigureOpenScale.ipynb](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/blob/master/notebooks/ConfigureOpenScale.ipynb)
> * **Notebook with output**: [with-output/ConfigureOpenScale.ipynb](https://github.com/IBM/cloudpakfordata-telco-churn-workshop/blob/master/notebooks/with-output/ConfigureOpenScale.ipynb)

<!-- TODO update -->
![Add notebook name and URL](../.gitbook/assets/images/wml/wml-2-add-name-and-url.png)

When the Jupyter notebook is loaded and the kernel is ready then we can start executing cells.

<!-- TODO update -->
![Notebook loaded](../.gitbook/assets/images/wml/wml-3-notebook-loaded.png)

<!-- TODO after this line -->

### Run the notebook

Spend an minute looking through the sections of the notebook to get an overview. You will run cells individually by highlighting each cell, then either click the `Run` button at the top of the notebook. While the cell is running, an asterisk (`[*]`) will show up to the left of the cell. When that cell has finished executing a sequential number will show up (i.e. `[17]`).

### Update credentials

* Enter the `AIOS_GUID` and `CLOUD_API_KEY` in the next cell for the `AIOS_CREDENTIALS`.
* Add the [Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) credentials for the service that you created in the next cell as `WML_CREDENTIALS`.

## 2. Setup OpenScale to utilize the dashboard

Now that you have created a machine learning model, you can utilize the OpenScale dashboard to gather insights.
[Follow the steps to configure the OpenScale dashboard](https://cloud.ibm.com/docs/services/ai-openscale?topic=ai-openscale-gs-obj#gs-confaios)
