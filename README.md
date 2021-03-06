# twitteridgrabber
Uses sixohsix's twitter API library to harvest follower IDs from twitter accounts

Example:

```python
>>> from twitteridgrabber import get_chunkList
>>> l = get_chunkList('djm000')
>>> l
[1330715556, 826311415, 425486512, 177488625, 69991609, 292139488, 412020405, 36
6403598, 15961385, 300639080, 101244995]
```

## Function Reference

### get_chunkList(**screen name**, _api object, initial cursor, reference to list_)

Recursive function that returns a list of twitter user ids as integers. Takes a string containing twitter username. Other optional arguments:


api object: Use this argument if you are dealing with multiple parallel API connections to twitter.

cursor: Twitter returns paginated sets of results at 5000 ids per page. Typically you want to start from the beginning, but if for some reason you want to omit the earlier pages, set this argument to the integer value of the cursor id where you would like to begin.

reference to list: If you already have a list instantiated and want to append twitter ids to it, pass it in here. By default this is just an empty list, or [].

### get_chunkCSV(***screen name***, _api object_, _initial cursor_)

Similar function although there is no list involved. Filename of the csv file will be _screenname_ follower_ids.csv.

## Authentication
Authentication is easy. Register an app with twitter on their developer site, and paste your API keys into credentials.py as shown. Or, declare a dict in the global namespace called parameters with key/value pairs that correspond to twitter's requirements.