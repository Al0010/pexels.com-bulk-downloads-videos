# Pexels.com bulk downloads videos script 

With this script, you can download bulk video resources from www.pexels.com and save a huge amount of time. 
The operation of the script is very simple, you only have to set the keyword and the number of videos you want to download. 

Install Pexels library: `pip3 install pexelsPy`

# 1. Create the API for Pexels.com
Creating the API for Pexels is very easy, all you have to do is create a profile on Pexels and follow the steps required by the site.
Follow the information on this link: https://help.pexels.com/hc/en-us/articles/900004904026-How-do-I-get-an-API-key-

REMEMBER: Do not abuse the API. By default, the API is rate-limited to 200 requests per hour and 20,000 requests per month. 

# 2. Enter your API
Enter the script and add your API inside the commas, then save the script.

# 3. Script configuration

A. Adding page number in `pageNumbers`

B. Adding the number of videos that would download in `resultsPage` 

C. Adding the keyword in `api.search_videos`

D. Save for updating

Following the default parameters, the script will automatically download the first 5 videos on page number 1 with the keyword 'Sea'.
All resources are automatically downloaded into the folder containing the script.

# 4. Run the script and download
