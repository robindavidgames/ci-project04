Setup project with the I Think Therefore I Blog example.

Using django. Installed at beginning of project using 

    pip3 install Django==3.2 gunicorn


Using User stories to guide development

![User Stories](/assets/readme_images/user_stories.png)

deployment at the start of the project following I Think Therefore I Blog example. Refer to the [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit).

Create env.py to hold secret keys
Hook up Heroku and ensure that it is holding my secret key and database URL
Connect Cloudinary and ensure those setting are also in the Heroku variables
In Heroku, connect to the GitPod respository for this project and click deploy for the main branch.
THEN BUILD PROJECT
before final deployment, make sure the debug flag in settings.py is set to false.
Also X_FRAME_OPTIONS = 'SAMEORIGIN' so that summernote can run in the deployed version.
remove DISABLE_COLLECTSTATIC config var in Heroku.
Deploy branch again in Heroku.


From the I Think Therefore I Blog tutorial, installed Summernote to provide a WYSIWYG editor in Django dashboard. Using 

    pip3 install django-summernote


Installed Bootstrap using guidance from https://getbootstrap.com/docs/5.1/getting-started/introduction/

Using this colour palette from Coolors. https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557
![Colour Palette](/assets/readme_images/colour_palette.png)


BUGS

Unable to post comments with django commenting about a null field. Turns out I had mistyped a variable in my model, which I was then not correctly referring to in my view.

I couldn't get my base.html file to recognise my style.css file. Referring to my own styles did not update the contents of the page. I searched through Stack Overflow, Slack, Student Support and the answer was... I needed to clear my cache!

Bootstrap was applying colours to elements that did not match the colour scheme of my site and attempts to fix this were inelegant. After reading this StackOverflow post https://stackoverflow.com/questions/20721248/how-can-i-override-bootstrap-css-styles, I understood that I could reference the Boostrap class names directly in my style.css file. Thus, I added this piece of code:

    .btn-primary {
        background-color: red;
        border: none;
    }


AUTOMATED TESTING

Guidance for automated testing taken from https://docs.djangoproject.com/en/3.0/intro/tutorial05/

CREDITS
All images are Public Domain or Creative Commons.
Salad placeholder image: https://www.photosforclass.com/download/pb_2834549
Kid Friendly Grilled Skewers
    Image: https://www.photosforclass.com/download/pb_417994
    Text: My own.