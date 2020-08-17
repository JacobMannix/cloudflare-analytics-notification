#!/usr/bin/python

# Jacob Mannix [08-17-2020]

# Import Dependencies
import CloudFlare # To access Cloudflare data through its API
import re # Regex for formatting analytics data
import requests # Used by discordMessage Function

# Function to call CloudFlare API
def uniqueVisitors(email, token, webhook_url):
    cf = CloudFlare.CloudFlare(email=email, token=token)
    zones = cf.zones.get(params = {'per_page':100})
    for zone in zones:
        zone_id = zone['id']
        zone_name = zone['name']
        
    uniques = []
    settings_analytics = cf.zones.analytics.dashboard.get(zone_id)
    analytics_status = settings_analytics['timeseries']
    
    # Dashboard Variable will hold the most recent Analytics for website (not effiecently but will do)
    for i in analytics_status:
        dashboard = i
#         print(dashboard) # uncomment this to see the different analytics Cloudflare API offers through the zone specified above in cf.zone. ...
#     print(i['uniques'])
    
    # Assigning variables to the specific analytics I want to message
    todays_uniques = dashboard['uniques']['all'] # Number of unique requests today
    todays_date = re.split("T", dashboard['since'])[0] # Todays Date
    todays_requests = dashboard['requests']['all'] # Total Service Requests today
    
    countries = [] 
    for i in dashboard['requests']['country']:
        countries.append(i)
    todays_countries = countries # Country Code for countries who sent service requests today


    # Formatting what to say in message
    str_uniques = str(todays_uniques)
    str_date = str(todays_date)
    str_requests = str(todays_requests)
    str_countries = str(u', '.join(todays_countries))
                        
    # OPTIONAL - Edit message_content to send a different style of message using the formatted str variables.
    message_content = "{}, {} unique visitors. {} total service requests from these countries {}.".format(str_date, str_uniques, str_requests, str_countries)
    # Alternate Message style.
#     message_content = "There were {} unique visitors on {} with a total number of service requests of {} from these countries: {}.".format(str_uniques, str_date, str_requests, str_countries)
    
    # Discord Function to send 'message_content' from above
    def discordMessage(webhook_url, message_content):
        Message = {"content": message_content}
        requests.post(webhook_url, data=Message)
    
    discordMessage(webhook_url, message_content)

# Running the Cloudflare uniqueVisitors Function
# CHANGE email, token and webhook_url
email = 'email_of_Cloudflare_account'
token = 'global_API_Key_for_Cloudflare_account'
webhookurl = 'webhook_URL_to_send_message(i_use_Discord)'

uniqueVisitors(email, token, webhook_url)