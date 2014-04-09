h-factor calculator
===================

hfactorcalc.py is a Python 3 module that calculates h-factors from a list of publication titles (or DOI) by quering Google Scholar information.

Any feedback is welcome!

email: joly.simon@gmail.com<br/>
[Twitter](http://twitter.com/simjoly)

Features
--------

* Calculates h-factor and 5 years h-factor for a list of publications.

Note
----

* hfactorcalc.py is a python3 script and it won't work with python 2.
* Note that if you make too many rapid queries to Google Scholar, they might block you from accessing their site. I have added a random lag between each query, but I haven't test how effective this is, especially with long publication lists. Unfortunately, this slows down donsiderably the search.
* Publications titles (or DOI) should be in a file with one publication per line.
* Type $python3 hfactorcalc.py -h for all available options.
* Note that hfactorcalc appears most retreive the right publication most of the time, but there is no guaranty. The h-factor obtained may not be completely exact. For greater accuracy, I suggest you use DOI instead of publication titles.

Example
-------

$python3 hfactorcalc.py -q test_list.csv

Credits
-------

hfactorcalc.py uses the very useful scholar.py script by Christian Kreibich (github/ckreibich) to query and parse Google Scholar data. 

License
-------

Copyright (c) 2014, Simon Joly<br/>
All rights reserved.<br/>
hfactorcalc.py is using the standard [BSD license](http://opensource.org/licenses/BSD-2-Clause).
