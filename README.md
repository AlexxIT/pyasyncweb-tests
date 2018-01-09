# pyasyncweb-tests

**Problem**: python web frameworks with [uvloop] perform a query with higher 
priority than return the result of active requests. Active requests accumulate 
and the result to the user is delayed.

There is no problem with the standard loop.

[uvloop]: https://github.com/MagicStack/uvloop 

**Note:**

japronto works only with uvloop <= 0.8.1

**Install:**

```
sudo pip3 install -r requirements.txt
```

**Run tests:**

`python3 test.py` or `google-chrome test.html`

## Test results (test.py)

aiohttp (good)

```
5.01238489151001
10.014051675796509
15.02192735671997
20.02768564224243
```

aiohttp_uvloop (bad)

```
5.012973785400391
20.03240466117859
20.03162956237793
20.031569719314575
```

japronto (bad)

```
5.012808561325073
20.0286066532135
20.029279708862305
20.03039288520813
```

sanic (bad)

```
5.01204514503479
20.024916887283325
20.024645805358887
20.02467703819275
```

sanic default loop (good)

```
5.012679100036621
10.018367290496826
15.025014400482178
20.030269861221313
```