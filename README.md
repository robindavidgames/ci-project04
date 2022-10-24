# Eat Something
Eat Something is a website that allows an enduser to read family-friendly recipes, and engage with a community of users through posting their own recipes and leaving comments.

This project is built with Django, CSS, HTML, Python, and Javascript. It uses a custom model (for 'tagging' recipes) and models adapted from the I Think Therefore I Blog examples. It has C.R.U.D. functionality, allowing users to create, read, update, and delete recipe posts. It has both manual and automatic testing. The majority of styling is done through Bootstrap, though there is a custom CSS for for more specific styling.

There are two types of users:
- A superuser that can approve new recipe posts and comments.
- A standard user that can browse the site, submit and update recipes, 'like' recipes, and post comments.

**Click here to visit the [Eat Something](https://ci-eat-something.herokuapp.com/) website.**

![Am I Responsive screenshot](/assets/readme_images/amiresponsive.png)
Screenshot from ami.responsivedesign.is

## Table of Contents

- [Features](#features)
    - [Front Page](#front-page)
    - [Navigation](#navigation)
    - [Alerts](#alerts)
    - [Registration](#registration)
    - [Recipe Page](#recipe-page)
    - [Recipe Images](#recipe-images)
        - [Custom Recipe Image](#custom-recipe-image)
        - [Default Recipe Image](#default-recipe-image)
    - [Likes](#likes)
    - [Comments](#comments)
    - [Comment Moderation](#comment-moderation)
    - [Recipe Tags](#recipe-tags)
    - [Footer](#footer)
    - [Data Model](#data-model)
    - [CRUD Functionality](#crud-functionality)
        - [Create](#create)
        - [Read](#read)
        - [Update](#update)
        - [Delete](#delete)
    - [Responsive Design](#responsive-design)
- [Design](#design)
- [Agile Development/User Stories](#agile-development--user-stories)
- [Accessibility](#accessibility)
- [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
    - [Validator Testing](#validator-testing)
- [Bugs](#bugs)
- [Setup and Deployment](#setup-and-deployment)
- [Technologies Used](#technologies-used)
- [Credits](#credits)

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

![Sign up page](/assets/readme_images/signoutfixed3.png)

### Recipe Page
This shows the recipe in more detail. Note that if the user is logged in and is the author of a given recipe, they have additional options to edit and delete the recipe.

![Recipe page](/assets/readme_images/recipepage.png)

### Recipe Images
Each recipe can have an image attached, which is used in the recipe preview and on the recipe page as the hero image. If no image is attached to a recipe, a placeholder image is used instead.

#### Custom Recipe Image

![A recipe card with a custom image](/assets/readme_images/customimage.png)

#### Default Recipe Image

![A recipe card with the default image](/assets/readme_images/defaultimage.png)

### Likes
Posts can be liked and unliked by users that are logged in. Posts always show the total amount of likes they have received.

![A counter for a post's likes.](/assets/readme_images/likes.png)

### Comments
Users that are logged in can leave comments. All users can read comments.

![Example comments.](/assets/readme_images/comments.png)

### Comment Moderation
Like posts, comments must be approved by an administrator before they go live on the webpage.

![Examples of authorised and unauthorised comments.](/assets/readme_images/commentmoderation.png)

### Recipe Tags
Recipe tags are implemented with a custom many-to-many model. There are many tags and each tag can be applied to many recipes. Tags are called in the RecipeDetail view and then in the recipe_detail.html template. As there is the possibility of many tags, they must be iterated through in the template itself:

    {% for tag in tags %}
    {{ tag }}
    {% endfor %}

Tags appear below each recipe.

![Example of tags in a recipe](/assets/readme_images/tags.png)

Tags are edited in the admin panel.

![Editing tags in the admin panel](/assets/readme_images/tagsadmin.png)

### Footer
The page footer contains social media links and copyright information.

![Page footer](/assets/readme_images/footer.png)

### Data Model
Comments and tags are created dependent on posts. Deleting a post will also delete all associated comments and will remove the respective tags (although, the tags will still exist in relation to other posts).

This project uses a custom model to handle tags on recipes. More details on this model [here.](#recipe-tags)

### CRUD Functionality
#### Create
Recipes can be created through a webform. However, upon submission, they must be set to "Published" by the superuser in the admin panel. This is a simple method to prevent spam and low-quality posts.

![Create functionality.](/assets/readme_images/crud-create.png)

#### Read
Users can read posts and comments.

#### Update
Recipes can be updated through a webform, provided the user that is logged in is the original author of that recipe. The link to update appears on any recipe page that belongs to the logged in user. The update form is autofilled from the existing recipe content.

![Update functionality.](/assets/readme_images/crud-update.png)

#### Delete
Recipes can be deleted through a webform, provided the user that is logged in is the original author of that recipe. The link to delete appears on any recipe page that belongs to the logged in user.

![Delete functionality.](/assets/readme_images/crud-delete.png)

### Responsive Design
Thanks to the use of Bootstrap, the website is fully responsive to mobile devices.

![The page shown on a mobile screen.](/assets/readme_images/responsive.png)

## Design

- I have used [this colour palette from Coolors](https://coolors.co/palette/e63946-f1faee-a8dadc-457b9d-1d3557) to ensure consistency across the site and related components.
![Colour Palette](/assets/readme_images/colour_palette.png)

- I used Bootstrap for most of this project, using guidance from [Bootstrap's Getting Started Documentation.](https://getbootstrap.com/docs/5.1/getting-started/introduction/)

- In addition, I used my own custom CSS file, to create smaller and more specific styling effects. On occasion, I have applied styling to exising Bootstrap classes.

## Agile Development / User Stories
I used User stories to guide development. The site was built using an agile methodology, working in small deliverable chunks. For instance, the tags model was left until the very end of the project, as this provides some value added, rather than being a core feature.

![User Stories](/assets/readme_images/agile.png)

## Accessibility

The entire site is text based, so should work well with screen readers. The exception to this is the external links in the footer, which are given an aria-label, and recipe images, which are given an alt text.

The website uses high-contrast colours between background and text to maintain readability.

## Testing

### Manual Testing

| Function | Expected Outcome | Actual Outcome |
| --- | --- | --- |
| **Any User** |  |  |
| User can open main page. | Display header, index of posts, and footer. | As intended. |
| User can click through paginated post previews. | Clicking through pagination shows additional posts. | As intended. |
| User can follow external links in footer. | External links direct to social media. | As intended. |
| User can click post detail. | Display post with title, image, likes, comments. | As intended. |
| User can register new account. | Clicking Register in header allows user to fill in form for a new account. | As intended. |
| Registration form is validated. | User must submit a username and a valid password. Email is optional. | As intended. |
| Comment counter. | Comment counter shows current number of comments on the page. | As intended. |
| Every page is styled. | CSS styles working for every page, including AllAuth pages. | As intended. |
| Site functions on different browswers. | Site functions on Chrome, Firefox, and Edge. | As expected. |
| Site is responsive. | Site responds to smaller screen sizes and a variety of mobile screen sizes. | As expected. |
| **Registered Users** |  |  |
| User can log in. | Clicking Log In allows user to sign into their account. | As intended. |
| Alerts pop up. | Alerts for signing in and signing out pop up at the top of the page. | As intended. |
| Alerts auto-dismiss. | Alerts dismiss themselves after 3 seconds. | As intended. |
| **Logged In Users** |  |  |
| User can post new recipe. | Clicking Post New Recipe allows the user to submit a form for a new recipe. | As intended. |
| Slug is unique. | Submitting a non-unique slug invalidates the form. | As intended. |
| Title, Slug, Content are required. | Submitting a form without these fields invalidates the form. | As intended. |
| Posts can use default image. | Posts without an image will have a default image applied. | As intended. |
| Submitted posts must be approved. | Superuser must approve the post on the admin site. | As intended. |
| User Recipes have author tools. | Author tools for Edit/Delete appear on any post the user authored. | As intended. |
| Author can edit post. | Clicking Edit Post allows the post author to change post details. | As intended. |
| Author can delete post. | Clicking Delete Post allows the post author to delete the post. | As intended. |
| User can post a comment. | Filling in the comment for will submit a comment under users current username. | As intended. |
| Submitted comments must be approved | Superuser must approve the comment on the admin site. | As intended. |
| User can like a post. | Clicking the heart icon will add a like. | As intended. |
| User can unlike a post. | Clicking the heart icon a second time will remove a like. | As intended. |
| Like counter shows current number of likes. | The like counter increments and deincrements when the user clicks the like icon. | As intended. |
| User can log out. | Clicking Log Out allows the user to sign out. | As intended. |

### Automated Testing

I created some automated tests for the project. Guidance for automated testing was taken from the [Django documentation](https://docs.djangoproject.com/en/3.0/intro/tutorial05/) and further assistance was found in Tutor Support. Specific details of help received is documented in recipes/tests.py.

There are 8 tests, testing the validity of the Recipes model and two of the more important Views. 

In order to run automated tests:

- Comment out current database in settings.py
- Then uncomment other database settings. 
- Revert these two changes after testing.

![Database code related to Automated Testing.](/assets/readme_images/automatedtesting1.png)

The command to run automated tests is: 

    python3 manage.py test recipes

![Output of Automated Testing.](/assets/readme_images/automatedtesting2.png)

### Validator Testing

#### HTML validator

The site passes HTML Validation at https://validator.w3.org/nu/.

![HTML Validation.](/assets/readme_images/htmlvalidation.png)

#### CSS validator

The site passes CSS Validation at https://jigsaw.w3.org/css-validator/.

![CSS Validation.](/assets/readme_images/cssvalidation.png)

#### Lighthouse

The site scores very well on Lighthouse for desktop.

![Lighthouse for desktop.](/assets/readme_images/lighthousedesktop.png)

It scores slightly less well on Lighthouse for mobile, primarily because the image files are too large and increase load time.

![Lighthouse for mobile.](/assets/readme_images/lighthousemobile.png)

#### Pep8

The Python code passes Pep8 validation.

![Pep8 Validation.](/assets/readme_images/pep8validation.png)

## Bugs

### Incorrect Model Variables
I was unable to post comments on the site and django reported an error regarding a null field. I had mistyped a variable in my comments model, which meant that the respective view could not find the appropriate information.

### Custom CSS Not Working
I couldn't get my base.html file to recognise my style.css file. Referring to my own styles did not update the contents of the page. I searched through Stack Overflow, Slack, Student Support and the answer was... I needed to clear my cache!

### Editing Bootstrap Classes in CSS
Bootstrap was applying colours to elements that did not match the colour scheme of my site and attempts to fix this were inelegant. After reading [this StackOverflow post](https://stackoverflow.com/questions/20721248/how-can-i-override-bootstrap-css-styles), I understood that I could reference the Boostrap class names directly in my style.css file. Thus, I added several pieces of CSS that referred to bootstrap classes, such as this:

    .btn-primary {
        background-color: red;
        border: none;
    }

### Unstyled AllAuth Pages
Login, Registration, Logout pages, etc, were using an ugly unstyled page, which didn't fit the wider site styling. 

![Unstyled sign-out page.](/assets/readme_images/signoutbroken.png)

Upon closer inspection, I noticed that the templates created by AllAuth used this line:

    {% extends "account/base.html" %}

which simply needed to be changed to:

    {% extends "base.html" %}

Upon which I could begin to style them as normal, with bootstrap, CSS, etc.

![Styled sign-out page.](/assets/readme_images/signoutfixed2.png)

![Styled sign-out page.](/assets/readme_images/signoutfixed1.png)

![Styled sign-out page.](/assets/readme_images/signoutfixed3.png)

### Deployment Errors

#### Incorrect Config Vars

When the project was finished, I found that the deployed site didn't work. After talking with Student Support and looking in the Heroku logs, we discovered a spelling mistake in my Heroku config vars!

### Updating and Deleting Posts

When creating code to update a recipe, I create a class view with GET and POST methods, in order to create a form, prepopulate it with existing content, and then allow the user to submit the corrections. However, the form continually didn't work. Upon submission, it would check is_valid, and the check would fail because the slug needed to be unique. However, the slug was never unique because the original recipe that is being edited has the same slug. This bug persisted for some time until I went to Student Support, who were about to show me the UpdateView class, as explained [here](https://www.geeksforgeeks.org/class-based-generic-views-django-create-retrieve-update-delete/).

This allowed me to reduce 60 lines of buggy code to:

    class EditRecipe(UpdateView):
        model = Recipe
        form_class = RecipeForm
        template_name = 'edit_post.html'
        success_url = '/'

It also allowed me to use DeleteView to achieve something similar with the code for deleting a recipe.

### Including messages in DeleteView
The class based views for CreateView and EditView both allowed the use of SuccessMessageMixin, to post messages to the user. However, in DeleteView, the messages were not shown. According to [this Stack Overflow thread](https://stackoverflow.com/questions/24822509/success-message-in-deleteview-not-shown), this is because the DeleteView doesn't have a form_valid to trigger the message. That thread also provided an alternative method to trigger the message.

## Setup and Deployment

Django was installed at beginning of project using the command: 

    pip3 install Django==3.2 gunicorn

Deployment at the start of the project following I Think Therefore I Blog example. Refer to the [cheatsheet](https://docs.google.com/document/d/1P5CWvS5cYalkQOLeQiijpSViDPogtKM7ZGyqK-yehhQ/edit) for further details.

1. Create env.py to hold secret keys.
2. Hook up Heroku and ensure that it is holding my secret key and database URL.
3. Connect Cloudinary and ensure those setting are also in the Heroku variables.
4. In Heroku, connect to the GitPod respository for this project and click deploy for the main branch.

At this point, I built the project. Running "git push" would cause the deployed site to automatically update.

5. Before final deployment, I made sure the 'Debug' flag in settings.py was set to 'False'.
6. Also, in the same file, ensure that X_FRAME_OPTIONS = 'SAMEORIGIN' so that summernote can run in the deployed version.
7. Remove DISABLE_COLLECTSTATIC config var in Heroku.
8. Deploy branch again in Heroku.

From the I Think Therefore I Blog tutorial, I installed Summernote to provide a WYSIWYG editor in Django dashboard. Using the command:

    pip3 install django-summernote

I installed Bootstrap using guidance from https://getbootstrap.com/docs/5.1/getting-started/introduction/

## Technologies Used

- Javascript
- Python
- CSS
- HTML
- Django
- AllAuth
- Heroku
- Cloudinary
- GitHub
- GitPod
- GitHub Pages
- Firefox developer tools
- Chrome developer tools
- JSHint
- W3 HTML Validator
- W3 CSS Validator
- favicon.io

## Credits
- The basic structure of the website is inspired by the I Think Therefore I Blog tutorials. Parts of the page logic are also inspired by this and are marked as such in the comments.
- Guidance for working with forms and CRUD functionality from [DjangoProject](https://docs.djangoproject.com/en/4.0/topics/forms/).
- Navbar code modified from a Bootstrap template found on [GetBootstrap](https://getbootstrap.com/docs/5.1/components/navbar/#nav).
- Footer code modified from a Bootstrap template found on [GetBootstrap Examples](https://getbootstrap.com/docs/5.1/examples/footers/).
- Index layout code modified from a Bootstrap template found on [GetBootstrap Examples](https://getbootstrap.com/docs/5.1/examples/album/).
- Recipe detail layout code modified from a Bootstrap template found on [GetBootstrap Examples](https://getbootstrap.com/docs/5.0/examples/blog/).
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