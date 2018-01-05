# Prometheus Pushgateway Demo App

Small python application that sends metrics to the Prometheus push gateway.

## Overview

`pets.py` is emulating a batch job generating pet names (dog, cat) or
raising exceptions. The parameter `job_id` is used to label the metrics.

All metrics generated start with `pet_`

## Running This Application

**Prerequisites**

* [Python](https://www.python.org/)
* [pip](https://pip.pypa.io/en/stable/)
* [prometheus_client](https://github.com/prometheus/client_python)

**Building and running**

Install the `prometheus_client` library with pip:

```bash
$ pip install prometheus_client
```

Run to push one set of metrics:

```bash
usage: pets.py [-h] job_id

$ python pets.py 1
```
