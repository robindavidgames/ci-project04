# Eat Something!
This project is built with Django, CSS, HTML, Python, and Javascript.

## Features

### Front page
This shows the various recipes available on the website. Each recipe has a photo and some details, which the user can click into. Recipe posts are paginated, showing 6 per page.

![Front Page](/assets/readme_images/frontpage.png)

### Navigation
The nav bar always displays at the top of the page and lets the user return home. If they are not logged in, a log in/register option is available.

![Navigation with login button](/assets/readme_images/navlogin.png)
![Navigation with logout button](/assets/readme_images/navlogout.png)

### Alerts
An alert pops up when a user logs in or logs out. This alert times out after 3 seconds.

![Logout alert](/assets/readme_images/alert.png)

### Registration
Users can register new accounts on the website so that they may leave comments and like posts.

### Recipe Page
This shows the recipe in more detail.

![Recipe page](/assets/readme_images/recipepage.png)

### Recipe Images
Each recipe can have an image attached, which is used in the recipe preview and on the recipe page as the hero image. If no image is attached to a recipe, a placeholder image is used instead.

#### Custom Recipe Image

![A recipe card with a custom image](/assets/readme_images/customimage.png)

#### Default Recipe Image

![A recipe card with the default image](/assets/readme_images/defaultimage.png)

### Likes
Posts can be liked and unlikes by users that are logged in. Posts always show the total amount of likes they have received.

![A counter for a post's likes](/assets/readme_images/likes.png)

### Comments
Users that are logged in can leave comments. All users can read comments. Comments must be approved by an administrator before they go live on the webpage.

![Example comments](/assets/readme_images/comments.png)

### Data Model
Comments are created dependent on posts. Deleting a post will also delete all associated comments.

### Responsive Design
Thanks to the use of Bootstrap, the website is fully responsive to mobile devices.

![The page shown on a mobile screen.](/assets/readme_images/responsive.png)

### Footer
The page footer contains social media links and copyright information.

![Page footer](/assets/readme_images/footer.png)

## Setup and Deployment

To setup the project, I folled the example in the I Think Therefore I Blog module.

Django was installed at beginning of project using the command: 

    pip3 install Django==3.2 gunicorn

deployment at the start of the project following I Think Therefore I Blog example. Refer to the [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit).

1. Create env.py to hold secret keys
2. Hook up Heroku and ensure that it is holding my secret key and database URL
3. Connect Cloudinary and ensure those setting are also in the Heroku variables
4. In Heroku, connect to the GitPod respository for this project and click deploy for the main branch.
5. THEN BUILD PROJECT
6. before final deployment, make sure the debug flag in settings.py is set to false.
7. Also X_FRAME_OPTIONS = 'SAMEORIGIN' so that summernote can run in the deployed version.
8. remove DISABLE_COLLECTSTATIC config var in Heroku.
9. Deploy branch again in Heroku.


From the I Think Therefore I Blog tutorial, I installed Summernote to provide a WYSIWYG editor in Django dashboard. Using the command:

    pip3 install django-summernote


I installed Bootstrap using guidance from https://getbootstrap.com/docs/5.1/getting-started/introduction/

## Styling
Using this colour palette from Coolors. https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557
![Colour Palette](/assets/readme_images/colour_palette.png)

I used Bootstrap for most of this project, using guidance from https://getbootstrap.com/docs/5.1/getting-started/introduction/

In addition, I used my own custom CSS file, to create smaller and more specific styling effects.

## User Stories
I used User stories to guide development

![User Stories](/assets/readme_images/user_stories.png)

## Bugs

Unable to post comments with django commenting about a null field. Turns out I had mistyped a variable in my model, which I was then not correctly referring to in my view.

I couldn't get my base.html file to recognise my style.css file. Referring to my own styles did not update the contents of the page. I searched through Stack Overflow, Slack, Student Support and the answer was... I needed to clear my cache!

Bootstrap was applying colours to elements that did not match the colour scheme of my site and attempts to fix this were inelegant. After reading this StackOverflow post https://stackoverflow.com/questions/20721248/how-can-i-override-bootstrap-css-styles, I understood that I could reference the Boostrap class names directly in my style.css file. Thus, I added this piece of code:

    .btn-primary {
        background-color: red;
        border: none;
    }

Login, Registration, Logout pages, etc, were using an ugly unstyled page, which didn't fit the wider site styling. Upon closer inspection, I noticed that the templates created by AllAuth used this line:

    {% extends "account/base.html" %}

which simply needed to be changed to:

    {% extends "base.html" %}

Upon which I could begin to style them as normal, with bootstrap, CSS, etc.

## Automated Testing

Guidance for automated testing taken from https://docs.djangoproject.com/en/3.0/intro/tutorial05/

## Credits
- The basic structure of the website is inspired by the I Think Therefore I Blog tutorials. Parts of the page logic are also inspired by this and are marked as such in the comments. 
- All images are Public Domain or Creative Commons.
- Salad placeholder image source: https://www.photosforclass.com/download/pb_2834549
- Kid Friendly Grilled Skewers
    - Image: https://www.photosforclass.com/download/pb_417994
    - Text: My own.
- Bluberry cookies 
    - Image: https://www.photosforclass.com/download/pb_1835414
    - Text: My own.
- Sugar cookies
    - Image: https://www.photosforclass.com/download/pb_1051884
    - Text: My own.
- Pasta
    - Image: https://www.photosforclass.com/download/pb_527286
    - Text: My own.
- Cupcakes
    - Image: https://www.photosforclass.com/download/pb_2285209
    - Text: My own.
- Egg breakfast
    - Image: https://www.photosforclass.com/download/pb_456351
    - Text: My own.
- Pancakes
    - Image: https://www.photosforclass.com/download/pb_2020863
    - Text: My own.
- Pizza
    - Image: https://www.photosforclass.com/download/pb_2068272
    - Text: My own.
- Berries
    - Image: https://www.photosforclass.com/download/pb_2277
    - Text: My own.
- Blueberry favicon from https://favicon.io/emoji-favicons/blueberries/