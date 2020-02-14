# django-twitter
This project was made to showcase how a twitter like website might function with the use of the Django web framework. It incorporates
full User functionality as well as Tweets, comments, likes and follows each being interconnected with one another.

# Table of contents
- [Installation](#Installation)
- [Features](#Features)
- [Technologies](#Technologies)
- [Images](#Images)
- [Inspiration](#Inspiration)
- [Contact Me](#ContactMe)

# Installation
- To install, clone the repo `git clone https://github.com/vBubbaa/django-twitter`
- Navigate to the `rootdirectory/twitter` and run
`python manage.py runserver`

# Features
- Users - Full User features including Login, Logout, Signup, and Update profile information (through Django model forms). It
uses the Django `AbstractUser` class to create custom users with custom fields including the default fields (username, password, email)
as well as Bio, Location, Website, and Profile Picutre.

- Tweets - Allows logged in users to "tweet" and is shown in the home feed as well as the users profile overview page.

- Likes - With the use of Ajax we have fully dynamic like buttons that trigger when the tweets heart icon is clicked. When it is clicked it 
associates the logged in user to like the tweet and creates a like object in the model tieing the user to the tweets.

- Comments - Each tweet has a comments section which is also Ajax powered and allows user to post comments on tweets if the session
user is logged in.

- Follows - Lets logged in users Follow/unfollow other users. You can also view the people who are following a given user as well as
see who a user follows.

- Ajax - All submit actions are used via ajax hitting Django url endpoints so that liking tweets, creating tweets, and commenting on 
tweets are refreshed automatically without page refreshing (just as how twitter feels when doing these actions)

- Custom Template tags - Custom template tags are used to check if tweets are already liked, as well as if users are already following a 
given user

# Technologies
- Python 3.7.6
- Django 2.2.7
- Bootstrap 4
- Jquery/ajax 
- Fontawesome

# Images
### Homepage
![Image of homepage](https://github.com/vBubbaa/django-twitter/blob/master/readmeimages/homepage.png)


### Tweet Overview
![Image of tweet overview](https://github.com/vBubbaa/django-twitter/blob/master/readmeimages/tweetoverview.png)


### Followers/following page (they are identical)
![Image of followers](https://github.com/vBubbaa/django-twitter/blob/master/readmeimages/followers.png)

### User Overview
![Image of followers](https://github.com/vBubbaa/django-twitter/blob/master/readmeimages/profileoverview.png)

# Inspiration
I created this project so that I could showcase my raw django skills, and I thought that recreating a twiter like application was a 
good way of doing so! I mainly did this project to showcase my Django backend skills.

# ContactMe
- Linkedin: https://www.linkedin.com/in/michael-james-60b81216b/
- Twitter: https://twitter.com/VBubbaa
