# Auto-commit
Main purpose of this repo is to help people to fill their contributions(graph) on their profile. This python script will automatically commit and push it to github.

##  Configure .env file
- Setup the range of commits and time.
- Add your github information.

## Install python & lib
```
pip install python-dotenv
```

## Automate Excution
### For Linux
*open crontab editor*
```
crontab -e
```
*add the line as below (put your path correctly.)*
```
0 * * * * /usr/bin/python3 /path/to/main.py
```

## For Windows
1. Open Task Scheduler.
2. Create a new task:
    - Trigger: Daily.
    - Action: Start a program → python → Add script path.
3. Save and enable it.