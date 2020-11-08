Simple parser to let me know whether my document is ready to collect.

I used BeautifulSoup library to parse the html. <br> 
It is installable following the command below: <br>
```sudo pip3 install beautifulsoup4```

I use it simply by adding it to my aliases on linux cl.<br>
```alias per="python3 path/to/script/main.py"``` <br>
This lets me to type "per" and the script starts to run and shows the result. <br>
But to permanently keep it among your aliases so that every time by opening up a new terminal there's no need to set the alias again is to modify the .bashrc file:
```nano .bashrc```
and add the same line like before (```alias per="python3 path/to/script/main.py"```) to this file and save it. you are all set!
