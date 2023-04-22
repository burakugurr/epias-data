# Run API Server

```bash
$ uvicorn api:app --host 0.0.0.0 --port 8000 --reload
```

# Create Service

Add the epas.service file to the linux service files

if you are start manually the service, you can use the following command:

```bash
$ sudo systemctl start epas.service
```

other starter commands:

```bash
$ python3 -m main.py

## NOTE 

Apache airflow kullanılarak oluşturulmuş bir dag ile veri çekilip veritabanına kaydedilebilirdi ancak apache airflow kurulumu ve kullanımı için fazla zaman harcanacağından dolayı bu yöntem tercih edilmedi.

istenirse dag file şuna benzer:

```python

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
import requests

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2022, 4, 22),
    'email': ['example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    }

dag = DAG(
    'epas',
    default_args=default_args,
    description='EPAS DAG',
    schedule_interval=timedelta(days=1),
    )

def get_data():
    requests.get('http://localhost:8000/market/mcp')


```