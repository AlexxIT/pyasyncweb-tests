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

# Test2

default loop

```
$ python3 main_builtin.py 
2018-01-09 19:22:41,834 INFO [__main__] Start connection
2018-01-09 19:22:41,835 INFO [__main__] Receive
2018-01-09 19:22:46,842 INFO [__main__] Write
2018-01-09 19:22:46,842 INFO [__main__] Close
2018-01-09 19:22:46,842 INFO [__main__] After Close
2018-01-09 19:22:46,843 INFO [__main__] Start connection
2018-01-09 19:22:46,844 INFO [__main__] Start connection
2018-01-09 19:22:46,844 INFO [__main__] Receive
2018-01-09 19:22:51,850 INFO [__main__] Write
2018-01-09 19:22:51,851 INFO [__main__] Close
2018-01-09 19:22:51,851 INFO [__main__] After Close
2018-01-09 19:22:51,852 INFO [__main__] Start connection
2018-01-09 19:22:51,853 INFO [__main__] Receive
2018-01-09 19:22:56,860 INFO [__main__] Write
2018-01-09 19:22:56,860 INFO [__main__] Close
2018-01-09 19:22:56,861 INFO [__main__] After Close
2018-01-09 19:22:56,862 INFO [__main__] Receive
2018-01-09 19:23:01,869 INFO [__main__] Write
2018-01-09 19:23:01,870 INFO [__main__] Close
2018-01-09 19:23:01,870 INFO [__main__] After Close
```

```
$ python3 test.py 
2018-01-09 19:22:46,844 INFO [__main__] 5.013042688369751
2018-01-09 19:22:51,852 INFO [__main__] 10.021281003952026
2018-01-09 19:22:56,861 INFO [__main__] 15.030425786972046
2018-01-09 19:23:01,871 INFO [__main__] 20.040003776550293
```

uvloop

```
$ python3 main_builtin_uvloop.py 
2018-01-09 19:25:00,169 INFO [__main__] Start connection
2018-01-09 19:25:00,169 INFO [__main__] Receive
2018-01-09 19:25:05,175 INFO [__main__] Write
2018-01-09 19:25:05,175 INFO [__main__] Close
2018-01-09 19:25:05,176 INFO [__main__] After Close
2018-01-09 19:25:05,176 INFO [__main__] Start connection
2018-01-09 19:25:05,177 INFO [__main__] Start connection
2018-01-09 19:25:05,178 INFO [__main__] Start connection
2018-01-09 19:25:05,178 INFO [__main__] Receive
2018-01-09 19:25:10,185 INFO [__main__] Write
2018-01-09 19:25:10,185 INFO [__main__] Close
2018-01-09 19:25:10,186 INFO [__main__] After Close
2018-01-09 19:25:10,186 INFO [__main__] Receive
2018-01-09 19:25:15,193 INFO [__main__] Write
2018-01-09 19:25:15,193 INFO [__main__] Close
2018-01-09 19:25:15,194 INFO [__main__] After Close
2018-01-09 19:25:15,194 INFO [__main__] Receive
2018-01-09 19:25:20,201 INFO [__main__] Write
2018-01-09 19:25:20,202 INFO [__main__] Close
2018-01-09 19:25:20,202 INFO [__main__] After Close
```

```
$ python3 test.py 
2018-01-09 19:25:05,176 INFO [__main__] 5.0111987590789795
2018-01-09 19:25:20,203 INFO [__main__] 20.038110494613647
2018-01-09 19:25:20,204 INFO [__main__] 20.0389666557312
2018-01-09 19:25:20,204 INFO [__main__] 20.039414167404175
```