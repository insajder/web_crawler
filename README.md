## Run crawler file
- create DB Schema `webcrawler` in MySQL and then configure DB URI in `model.py` at line 6 with according MySQL username and password
- in root directory run `python spider.py` and it will fill DB with data

## Run Flask app
- `cd application`
- configure DB URI in `main.py` at line 8
- `$env:FLASK_APP = "main"` for Windows and `export FLASK_APP=main` for MacOS and Linux
- `flask run`