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


BUGS

Unable to post comments with django commenting about a null field. Turns out I had mistyped a variable in my model, which I was then not correctly referring to in my view.


AUTOMATED TESTING

Guidance for automated testing taken from https://docs.djangoproject.com/en/3.0/intro/tutorial05/

