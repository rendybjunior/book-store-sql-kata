# Book Store SQL Kata

Simple SQL clean code kata on **BigQuery dialect**. Using Python for testing, and Jinja for table name templating.

## Preparation

### Data Loading

* Load data in `data` folder to BigQuery, see [this simple guideline](https://cloud.google.com/bigquery/docs/loading-data-local).
* Choose upload and auto-detect schema
* OR ask your trainer, in case the data is already exist somewhere.
* Configure `config.yaml` and ensure table mapping is correct and you have necessary access

### Environment Prep

This repo is using Python for testing, and Jinja for table name templating.
To run the exercise requires some dependencies, it is recommended to:

* Create a new virtualenv, if you use virtualenv wrapper: `mkvirtualenv --python=python3 book-store-sql-kata`
* Install requirements, do `pip install -r requirements.txt`
* Ensure you can access the BigQuery table, see [this to use service account](https://cloud.google.com/bigquery/docs/reference/libraries#setting_up_authentication) and [this to use gcloud sdk](https://cloud.google.com/sdk/gcloud/reference/auth/login) (the later is more recommended since it is more secure, no need to have private key)

## How to

Refactor the initial sql code so that the code reflects clean code principles.

* Readable, easy to understand
* Extensible, easy to add new feature

The exercise steps:

* Ensure the data preparation step and environment prep has been done, including the auth access
* Create your own branch using pattern `kata/<github username>`
* Refactor the SQLs in `sql` folder to reflect clean code principle, ask your team on SQL style guideline being used
* Run `pytest` to ensure your code is running correctly
* Create a Pull Review and request for review

Note:

* It is fine to change the test variables, if it is required to rename variable to be better in the SQL

Bonus:

* Spot and fix inefficient query
* Make testing more readable and cover more cases

## Disclaimer

The data, including name and email, are randomly generated and created by the help of [Mockaroo](https://mockaroo.com/). They should not reflect real name and emails, and if it does it should be an unintended coincident.
