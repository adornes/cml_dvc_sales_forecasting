## Intro

An adaptation of [a sales forecasting example](https://www.mariofilho.com/how-to-predict-multiple-time-series-with-scikit-learn-with-sales-forecasting-example/) for demonstrating a Continuous Machine Learning (CML) approach with [DVC](https://dvc.org/).

## Setup

```sh
pipenv install --dev
```

## DVC

Initialize DVC

```sh
dvc init
```

and add remote storage

```sh
dvc remote add -d s3remote s3://adornes-dvc-test/sales-example
```

disable analytics (optional)

```sh
dvc config core.analytics false
```

## DVC Pipeline

Load raw data

```sh
dvc run -n load_raw_data \
    -d src/load_raw_data.py \
    -o assets/raw_data \
    python src/load_raw_data.py
```

Prepare data

```sh
dvc run -n prepare_data \
    -d src/prepare_data.py \
    -d assets/raw_data \
    -o assets/prepared_data \
    python src/prepare_data.py
```

Enrich data

```sh
dvc run -n enrich_data \
    -d src/enrich_data.py \
    -d assets/prepared_data \
    -o assets/enriched_data \
    python src/enrich_data.py
```


Train model

```sh
dvc run -n train_model \
    -d src/train_model.py \
    -d assets/enriched_data \
    -o assets/models \
    python src/train_model.py
```

Evaluate the model and save metrics

```sh
dvc run -n evaluate_model \
    -d src/evaluate_model.py \
    -d assets/enriched_data \
    -d assets/models \
    -M assets/metrics.json \
    python src/evaluate_model.py
```

Check the metrics for your current model:

```sh
dvc metrics show
```

Check the how metrics evolved:

```sh
dvc metrics diff
```

And you can also visualize the DAG (Directed Acyclic Graph) for your pipeline:

```sh
dvc dag
```

Which outputs something like this:

```
              +---------------+
              | load_raw_data |
              +---------------+
                       *
                       *
                       *
               +--------------+
               | prepare_data |
               +--------------+
                       *
                       *
                       *
               +-------------+
               | enrich_data |
               +-------------+
              ***            ***
            **                  ***
          **                       **
+-------------+                      **
| train_model |                    **
+-------------+                 ***
              ***            ***
                 **        **
                   **    **
              +----------------+
              | evaluate_model |
              +----------------+
```

## Evolving your model

### Suggestions

* Add more lags and differences to second last week and third last week.
* Change model hyperparameters

### Step-by-step

1) Checkout a new branch:

```sh
git checkout xyz-experiment
```

2) Change your code (any script)

3) Let DVC automatically infer what to reexecute in your pipeline: 

```sh
dvc repro assets/evaluate.dvc
```

4) Check the differences in the metrics

```sh
dvc metrics diff
```

## References

* https://www.mariofilho.com/how-to-predict-multiple-time-series-with-scikit-learn-with-sales-forecasting-example/
* https://dvc.org/
* https://www.curiousily.com/posts/reproducible-machine-learning-and-experiment-tracking-pipiline-with-python-and-dvc/

## License

MIT