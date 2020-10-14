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
dvc remote add -d s3remote url s3://adornes-dvc-test/
```

disable analytics (optional)

```sh
dvc config core.analytics false
```

## DVC Pipeline

Load raw data

```sh
dvc run -f assets/raw_data.dvc \
    -d src/load_raw_data.py \
    -o assets/raw_data \
    python src/load_raw_data.py
```

Prepare data

```sh
dvc run -f assets/prepared_data.dvc \
    -d src/prepare_data.py \
    -d assets/raw_data \
    -o assets/prepared_data \
    python src/prepare_data.py
```

Enrich data

```sh
dvc run -f assets/enriched_data.dvc \
    -d src/enrich_data.py \
    -d assets/prepared_data \
    -o assets/enriched_data \
    python src/enrich_data.py
```


Train model

```sh
dvc run -f assets/models.dvc \
    -d src/train_model.py \
    -d assets/enriched_data \
    -o assets/models \
    python src/train_model.py
```

Evaluate the model and save metrics

```sh
dvc run -f assets/evaluate.dvc \
    -d src/evaluate_model.py \
    -d assets/enriched_data \
    -d assets/models \
    -M assets/metrics.json \
    python src/evaluate_model.py
```

Check the metrics for your current model:

```sh
dvc metrics show -T
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
dvc metrics show -T
```
