We will explore Facebook graph API in this project.


TODO:
1) Graph API returns post created date in UTC. I am converting it to EST (America/New York). For precise analytics like what time a user posts, location information for the post 
should be used to figure the time zone where the post was posted.
2) Graph API has a modifier 'limit'. Currently, if we do not specify it, we get 10 posts, and then under pagination we have links to next page. For this implementation, I am passing limit
as 1000000 (I know my posts are less than that). In future, implement a generator to retrieve all posts using pagination.