Features
1). Programmatically extract data about our posts on facebook using the Graph API.
2). Build views on that data to answer queries.
3). Using 1 and 2, generate statistics, plots and interesting insights from our posts.

Wish-list Features (to-do)
1). Wrap up the output from the script and post on the user's facebook page.

Using the script
1). You should have Python 3.0+. I used Anaconda 3.6. 
2). I used facepy package to access Facebook's Graph API and used pip to install on my machine (https://github.com/jgorset/facepy).
3). I created a dummy facebook app to get a user access token which lets you call the Graph API. The user access token is temporary and needs to be regenerated every 2-3 hours.
Follow the steps in this link to create an app: https://developers.facebook.com/docs/apps/register. 
Follow steps in this link to generate user access token: https://developers.facebook.com/docs/apps/register
4). To run, copy and paste the user access token to a local file on your machine. Then in the script my_posts.py, modify the variable TOKEN_FILE_NAME with the path to that file. 
For example, I have my user access token stored at "C:\\Users\\TarunJoshi\\FB_ACCESS_TOKENS\\token1.txt" and hence I have:  
    TOKEN_FILE_NAME = "C:\\Users\\TarunJoshi\\FB_ACCESS_TOKENS\\token1.txt"
5). Now just run the script: python my_posts.py.

BUG-BUG:
1) Graph API returns post created date in UTC. I am converting it to EST (America/New York). For precise analytics like what time a user posts, location information for the post 
should be used to figure the time zone where the post was posted.

2) Graph API has a modifier 'limit'. Currently, if we do not specify it, we get 10 posts, and then under pagination we have links to next page. For this implementation, I am passing limit
as 1000000 (I know my posts are less than that). In future, implement a generator to retrieve all posts using pagination.

3) __pycache__ and .pydev project files have been checked in. Remove them.

4) Reorganize the code structure, add tests, and documentation etc conforming to git guidelines.

5) The plots should have an as-of date in the title of the plot.

6) "Distribution of reactions" should have the x-axis labeled.