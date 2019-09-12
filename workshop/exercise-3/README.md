# Exercise 3: Monitoring models

## Configure OpenScale in the Jupyter Notebook

We'll use a Jupyter notebook to configure OpenScale.

### Download the notebook and add the notebook to the project

* Either clone this repository:

```bash
git clone https://github.com/IBM/cloudpakfordata101
```

or download the notebook directly:

```bash
wget https://raw.githubusercontent.com/IBM/cloudpakfordata101/master/workshop/ConfigureOpenScale.ipynb
```

* Under the `Assets` tab in your project, from the menu on the left, choose `Notebooks` and click `+Add Notebook`.

* Choose the `From file` tab and navigate to where you downloaded the `ConfigureOpenScale.ipynb` notebook, either in `~/Downloads/` or the location where you cloned the repository, in the `cloudpakfordata101/workshop` directory.

### 2. Configure and run the notebook

### Run the notebook

* Run all the cells individually by highlighting each cell by clicking it, then either click the `Run` button at the top of the notebook or `control` + `return` at the same time. While the cell is running, an asterisck will show up in the brackets to the left of the cell `[*]` and when it is done, a sequential number will show up, i.e. `[17]`. Do this for the next steps, with some additional instructions:

### Use free internal DB or Create a Databases for PostgreSQL DB

For this lab, we'll use the free internal DB. Note that this is not GDPR compliant, and this DB is not accessible to the user. For productions purposes, you may wish to use a separate DB , i.e Postgres.

#### Make sure that the cell for `KEEP_MY_INTERNAL_POSTGRES = True` remains unchanged

#### If you have or wish to use a paid `Databases for Postgres` instance, follow these instructions

> Note: Services created must be in the same region, and space, as your Watson Studio service or on the same ICP4D cluster

* Either provision the database in your ICP4D cluster
 **or**
* Using the [IBM Cloud Dashboard](https://cloud.ibm.com/catalog) catalog, search for PostgreSQL and choose the `Databases for Postgres` [service](https://console.bluemix.net/catalog/services/databases-for-postgresql).
* Wait a couple of minutes for the database to be provisioned.
* Click on the `Service Credentials` tab on the left and then click `New credential +` to create the service credentials. Copy them or leave the tab open to use later in the notebook.
* Make sure that the cell in the notebook that has:

```python
KEEP_MY_INTERNAL_POSTGRES = True
```

is changed to:

```python
KEEP_MY_INTERNAL_POSTGRES = False
```

### 4. Create a Watson Machine Learning instance

* Under the `Settings` tab, scroll down to `Associated services`, click `+ Add service` and choose `Watson`:

  ![add_service](https://github.com/IBM/pattern-images/blob/master/watson-studio/add_service.png)

* Search for `Machine Learning`, Verify this service is being created in the same space as the app in Step 1, and click `Create`.

  ![create-machine-learning](https://raw.githubusercontent.com/IBM/pattern-images/master/machine-learning/create-machine-learning.png)

* Alternately, you can choose an existing Machine Learning instance and click on `Select`.

  ![watson-studio-add-existing-ML](https://raw.githubusercontent.com/IBM/pattern-images/master/watson-studio/watson-studio-add-existing-ML.png)

* The Watson Machine Learning service is now listed as one of your `Associated Services`.

* In a different browser tab go to [https://cloud.ibm.com/](https://cloud.ibm.com/) and log in to the Dashboard.

* Click on your Watson Machine Learning instance under `Services`, click on `Service credentials` and then on `View credentials` to see the credentials.

  ![ML-service-credentials](https://raw.githubusercontent.com/IBM/pattern-images/master/machine-learning/ML-service-credentials.png)

* Save the credentials in a file. You will use them inside the notebook.

### Title

> NOTE: At this time (3/27/19) you must use an instance of Watson OpenScale deployed in the `Dallas` region. This is currently the only region that sends events about scoring requests to the message hub, which is read by OpenScale to populate the payload logging table.

* Using the [IBM Cloud Dashboard](http://cloud.ibm.com) create a [Watson OpenScale](https://cloud.ibm.com/catalog/services/ai-openscale) service.
* You will get the Watson OpenScale instance GUID when you run the notebook using the [IBM Cloud CLI](https://cloud.ibm.com/catalog/services/ai-openscale)

* Enter the `AIOS_GUID` and `CLOUD_API_KEY` in the next cell for the `AIOS_CREDENTIALS`.
* Add the [Watson Machine Learning](https://cloud.ibm.com/catalog/services/machine-learning) credentials for the service that you created in the next cell as `WML_CREDENTIALS`.
* Either use the internal Database, which requires *No Changes* or Add your `DB_CREDENTIALS` after reading the instructions preceeding that cell and change the cell `KEEP_MY_INTERNAL_POSTGRES = True` to become `KEEP_MY_INTERNAL_POSTGRES = False`.

* Move your cursor to each code cell and run the code in it. Read the comments for each cell to understand what the code is doing. **Important** when the code in a cell is still running, the label to the left changes to **In [\*]**:.
  Do **not** continue to the next cell until the code is finished running.

## 7. Setup OpenScale to utilize the dashboard

Now that you have created a machine learning model, you can utilize the OpenScale dashboard to gather insights.
[Follow the steps to configure the OpenScale dashboard](https://cloud.ibm.com/docs/services/ai-openscale?topic=ai-openscale-gs-obj#gs-confaios)

Congratulations! You have completed the workshop!
