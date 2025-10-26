# install requirements
```
pip install pycaw comtypes flask

```

## (optional) if pycaw don't work at first
```
pip uninstall pycaw -y
pip install pycaw==20230407
```

# run server
```
python server.py
```

# set ngrok config

```
ngrok config add-authtoken 34aBGAwfRSNTZPFrODCfWLBWIix_Ego74FgjEKX1PJ3oceKU
```

# open tunel
```
ngrok http 8080
```

e.g. final
```
https://nondefunct-unlopped-staci.ngrok-free.dev/
```

# available after run

```
http://TU_IP_LOCAL:8080/mute
http://TU_IP_LOCAL:8080/unmute
```


# when all is setup
just run
```
run.bat
```

is equivalent to run those 2
```
python server.py
ngrok http 8080
```

