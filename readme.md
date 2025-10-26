# install requirements
```
pip install pycaw comtypes flask

pip uninstall pycaw -y
pip install pycaw==20230407
```

# run server
```
python server.py
```

# available after run

```
http://TU_IP_LOCAL:8080/mute
http://TU_IP_LOCAL:8080/unmute
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