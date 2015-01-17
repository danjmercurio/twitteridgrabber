# twitteridgrabber
Uses sixohsix's twitter API library to harvest follower IDs from twitter accounts

Example:

```python
>>> from twitteridgrabber import auth, get_chunkList
>>> from credentials import parameters
>>> l = get_chunkList(auth(),'djm000',-1,[])
>>> l
[1330715556, 826311415, 425486512, 177488625, 69991609, 292139488, 412020405, 36
6403598, 15961385, 300639080, 101244995]
>>>
```