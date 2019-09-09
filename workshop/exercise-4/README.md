# Exercise 4: Monitor the model with OpenScale

## Configure OpenScale in the Jupyter Notebook

###  Use free internal DB or Create a Databases for PostgreSQL DB


#### If you wish, you can use the free internal Database with Watson OpenScale. To do this, make sure that the cell for `KEEP_MY_INTERNAL_POSTGRES = True` remains unchanged.

#### If you have or wish to use a paid `Databases for Postgres` instance, follow these instructions:

> Note: Services created must be in the same region, and space, as your Watson Studio service.

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

  ![](https://github.com/IBM/pattern-images/blob/master/watson-studio/add_service.png)

* Search for `Machine Learning`, Verify this service is being created in the same space as the app in Step 1, and click `Create`.

  ![](https://raw.githubusercontent.com/IBM/pattern-images/master/machine-learning/create-machine-learning.png)

* Alternately, you can choose an existing Machine Learning instance and click on `Select`.

  ![](https://raw.githubusercontent.com/IBM/pattern-images/master/watson-studio/watson-studio-add-existing-ML.png)

* The Watson Machine Learning service is now listed as one of your `Associated Services`.

* In a different browser tab go to [https://cloud.ibm.com/](https://cloud.ibm.com/) and log in to the Dashboard.                                                          

* Click on your Watson Machine Learning instance under `Services`, click on `Service credentials` and then on `View credentials` to see the credentials.

  ![](https://raw.githubusercontent.com/IBM/pattern-images/master/machine-learning/ML-service-credentials.png)

* Save the credentials in a file. You will use them inside the notebook.


### 
> NOTE: At this time (3/27/19) you must use an instance of Watson OpenScale deployed in the `Dallas` region. This is currently the only region that sends events about scoring requests to the message hub, which is read by OpenScale to populate the payload logging table.

* Using the [IBM Cloud Dashboard]() create a [Watson OpenScale](https://cloud.ibm.com/catalog/services/ai-openscale) service.
* You will get the Watson OpenScale instance GUID when you run the notebook using the [IBM Cloud CLI](https://cloud.ibm.com/catalog/services/ai-openscale)



Congratulations! You have completed the workshop!
