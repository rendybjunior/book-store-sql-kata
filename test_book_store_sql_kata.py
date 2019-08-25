import yaml
from jinja2 import Template

from google.cloud import bigquery

def test_simple_count():
    count = 0
    with open("config.yaml", 'r') as f:
        config = {}
        try:
            config = yaml.safe_load(f)
        except yaml.YAMLError as exc:
            print(exc)

        with open("sql/simple_count.sql", 'r') as f:
            t = Template(f.read())
            query = t.render(config)
            print(query)
            client = bigquery.Client()
            query_job = client.query(query)
            results = [row for row in query_job]
            count = results[0].x
            
    assert count == 1000