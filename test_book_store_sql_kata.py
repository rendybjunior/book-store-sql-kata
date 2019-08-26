import pytest
from jinja2 import Template

CONFIG_FILE_PATH = "config.yaml"
SQL_FILES_PATH = "sql/"

@pytest.fixture
def bigquery_client():
    from google.cloud import bigquery

    return bigquery.Client()

@pytest.fixture
def config():
    config = {}
    import yaml
    with open(CONFIG_FILE_PATH, 'r') as f:
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)
    return config

@pytest.fixture
def sql_files():
    sql_files = {}
    import os
    for root, directories, files in os.walk(SQL_FILES_PATH):
        for file in files:
            if file.endswith('.sql'):
                with open(SQL_FILES_PATH + file, 'r') as f:
                    sql_files[file] = f.read()
    return sql_files

def test_simple_count(bigquery_client, config, sql_files):
    count = 0
    query = Template(sql_files["simple_count.sql"]).render(config)
    query_job = bigquery_client.query(query)
    results = [row for row in query_job]
    count = results[0].x
            
    assert count == 1000