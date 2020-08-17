# Cloudflare Analytics Notification

A python script that sends a daily webhook notification (Discord message) with the most recent Cloudflare analytics for your website.

### Cloudflare API Repo:
- [python-cloudflare](https://www.github.com/cloudflare/python-cloudflare)

### In order for this to work...
- You need to be using Cloudflare on your website
- You need to have a chat app that supports webhooks (i use discord)
- A web server to automate running the script

### Configuring the python script...
you need to change the 3 variables at the bottom of the script
- email (the email of your cloudflare account)
- token (the global API key for your cloudflare account)
- webhook_url (the webhook URL) [I use discord]

#### Accessing your Cloudflare Global API key
- Login to [Cloudflare](https://www.cloudflare.com)
- Head over to My Profile -> API Tokens -> API Keys -> VIEW Global API Key (enter your password and copy key). Make sure to keep this key private, its the password to your account though the API.

#### Creating a Webhook and getting the URL
I will show an example using Discord but this is possible with any app that uses webhooks.
- Login to Discord using on Desktop or Browser (does not work on mobile).
- Click on the Discord server you want to send these messages too.
- Go to Server Settings -> Integrations -> View Webhooks -> either New Webhooks or click on an existing one and copy the Webhook URL

---

### Running the Python script
You can use any computer to run the script on as long as python is installed but to get the most automation out of it I will be running this script on my Linux web server.
- Make sure to pip install any new libraries and know where python is installed. For me python is installed at ```#!/usr/bin/python``` but yours may be different such as ```#!/usr/bin/env/python```. This is line is specified at the top of the python script.

#### On Linux
If you are using a Linux web server and have python installed you just need to upload the configured script to the server make it executable and run it daily. In order to run the script daily I use crontab.

##### Make script executable
- First we need to make the file executable, type: ```'chmod a+x /example/file/path/CloudflareAnalyticsNotification.py```.
- Now run the script by typing in the path of the file to see if it is working properly. ```/example/file/path/CloudflareAnalyticsNotification.py```

##### Configure crontab
- To access crontab type ```crontab -e```
- Start a new line and configure the crontab timing, I chose to run the script once per day at 8pm, use this website [crontab.guru](https://www.crontab.guru/#00_20_*_*_*) if you want to configure it differently.
- After settings the timing enter the path of the python file ```/example/file/path/CloudflareAnalyticsNotification.py```
- Save and exit crontab
- The crontab job should look similar to the picture

```python
00 20 * * * /home/mannix/python/CloudflareAnalyticsNotifications.py
```

---

### Discord Message Example
![DiscordMessageExample](discordMessageexample.jpg | width= 80)
