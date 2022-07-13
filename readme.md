## This project runs on Linux



# Prepare

#### Clone the code

```
git clone git@github.com:Muddypond/daka.git
```

#### Configuring the environment

```
pip install -r requirements.txt
```

#### Revised the ID and password in template_main.py and rename it as main.py



# Set up timed tasks

#### Find the file /etc/crontab, add a new line

```
11 8 * * 0-6 root python /home/daka/main.py; 
```

#### The log of the cron is in /var/log/cron



# Now all is done

