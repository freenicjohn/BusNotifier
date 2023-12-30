# BusNotifier
Posts upcoming bus times in a Slack channel

## Deploy Lambda
1) Zip all py files with
```
zip result.zip *.py
```
2) Upload the zipped file via the aws console
3) Layers hold dependency libs and only need to be uploaded if changed


## Run locally
```
python notify.py
```

## Secrets
Secrets contain user-specific information needed to hit the CTA's public API and other configuration parameters. I'm using another private repo to hold these secrets. On aws, they should be entered as environment variables. Locally, they can be stored at the path shown in the ```load_secrets()``` method.