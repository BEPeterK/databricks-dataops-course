# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Run DLT pipeline
# MAGIC
# MAGIC The DLT notebooks for producing the output data has already been developed.
# MAGIC Your next task is to run the notebooks yourself.
# MAGIC
# MAGIC To run it, you shall now to manually setup a pipeline run.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC
# MAGIC ## In and out data
# MAGIC
# MAGIC ### Incoming data
# MAGIC
# MAGIC - A sample of NYC Taxi data, from Unity Catalog (UC) path `training.taxinyc_trips.yellow_taxi_trips_curated_sample`
# MAGIC - NYC population data
# MAGIC
# MAGIC ### Outgoing data product
# MAGIC
# MAGIC We produce a data product called revenue. For now it contains the following outgoing data sets:
# MAGIC
# MAGIC 1. `revenue_by_tripmonth`
# MAGIC 2. `revenue_by_borough`
# MAGIC 3. `revenue_per_inhabitant`
# MAGIC
# MAGIC `borough_population` is an intermediate internal dataset.
# MAGIC
# MAGIC In production, the data product will be written as the UC schema `acme_transport_taxinyc.dltrevenue`.

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Task: Set up at DLT pipeline run.
# MAGIC
# MAGIC For each notebook, connect to the UC Shared Cluster you have been assigned, and run through the cells. Study the cells as you run them.
# MAGIC
# MAGIC ### Setup the database schema where we will write data
# MAGIC
# MAGIC 1. Go to `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dltrevenue/setupdb`
# MAGIC 2. Run the notebook
# MAGIC 3. Copy the database name, which will be something like `dev_paldevibe_dataopsv2_e88409f3_dltrevenue`
# MAGIC
# MAGIC ### Run the DLT pipeline
# MAGIC
# MAGIC 1. Go to `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dltrevenue/revenue`
# MAGIC 2. Study the code, and compare to the corresponding pyspark pipelines in `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dltrevenue/`.
# MAGIC 3. Go to the Delta Live Tables menu under Data Engineering on the right side menu
# MAGIC 4. Press `Create pipeline`
# MAGIC     1. `Pipeline name`: `dltrevenue_[your username]_manual_test`
# MAGIC     2. `Product edition`: `Advanced`
# MAGIC     2. `Source code`: Lookup the `orgs/acme/domains/transport/projects/taxinyc/flows/prep/dltrevenue/revenue` notebook
# MAGIC     3. `Destination`: Unity Catalog
# MAGIC     4. `Catalog`: acme_transport_taxinyc
# MAGIC     5. `Target schema`: Select the name of the schema/database you created in the setupdb notebook
# MAGIC     6. Don't add any other options, or set any policies
# MAGIC 5. Press `Start` to run the pipeline

# COMMAND ----------

