# Roster Parser 10000

You need to run this script locally for it to work, and you'll need to run the following before running the script:

## Installing Dependencies
`$ pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib`

## Formatting roster.txt
Due to API constaints I can't read the roster directly from the shared sheet, so you'll need to create a roster.txt formatted in the following way:
```txt
DD-MM-YYYY
{{ROSTER}}
```

Where roster is the copy/paste results from highlighting a week's roster like so:

![](https://cdn.paradaux.io/img/5scwi.png)

Hitting Ctrl + C to copy, and then pasting from the next line onwards. It should look like the roster.txt.example provided below. The script handles all the parsing/creation of events from that. It uses the date provided at the top as the starting date, then assumes all the following dates are subsequent days. 

Only run this one week at a time.



After that it's just a matter of running main.py
`$ python3 main.py`

You will be prompted to login to your google account, credentials are saved in token.json but you can either delete this or keep it so you don't need to login next time you go to login.