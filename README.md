<div align="center">
<img alt="Logo" src="https://lh3.googleusercontent.com/V8MOxOcFMQhgg3ES5uMok_hPZNzKKJQf-E_QOIUIEwfiIQSQzlIeCRsZCO745tyBuTA3jY76I1zvcTnBsrWFCAMEm2aKew7686eUrvX18CXcuLtlwMG0rg8jK8nuxx5rUJENJWQG67ExZksxNgazR6Znj8wV-i4u_ob4eXBPiGMtOCgkbda1kC1LE-vByZEaMAQ4bTdTeJcvZsgL4Ks_KW7jvpbP-oCLWBcx6EJ6QUFl68YOvZGBEU3zX1z3a938WkKJbroaNBOBlx_EX1fsCZeNocYq_aBE2R5IeIyEhKWa8j0uTumz0cqjRHqFiNW7WWOXkpz49uutx29uPE_AUaQgIqY80mrzZZJZg8zkXmdtVhyWliLQVI-LpL3FIYXaJnoFIixfACQv0RfiQ6p8tC6YUUis2qC3pmqnpNjpdfwOI7hybufOoigIh5KXnHSxV8AMYdtvDanqeJ7plWX7k4OaeMD_ONoAItjCejBz9dJmLjOWwXTF0gV8VPRnba6FfHxx_flJ_96XeQSMngJRnouxaCs_XAdG2bEd58S6FeoyIOaDdRjrYy1Ik2Wm1ipu_3YqWsb3wi4fbDc9oHR9DtOma3tb-IGa0v5Nno13EW2the2paKww8zHV_hguIpv7wBJGOc7J-JAWeoDSlOGJAgLNnmvX2L_DUQpG91FxPS5nrFmEiumvZZucqiz1Gy2v0Bu1W4qxAq8aHU-FP3svcQ=w571-h156-no?authuser=1" />
</div>
<br></br>

**Feather's Fight** is a simple journalistic web page. Authors write about fighting culture among various styles and new discoveries around the world.

It was developed using **Python** and  **Django** framework.

This documentation aims to present a quick guide about its construction and usage.
<br></br>


Guide:
- [As User](#as-user)
  - [Read an Article](#read-an-article)
  - [Sign up](#sign-up)
  - [Log in](#log-in)
  - [Become an author](#become-an-author)
- [As Author](#as-author)
  - [Dashboard](#dashboard)
  - [New Publication](#new-publication)
  - [Publications,  requests and saves](#publications--requests-and-saves)
- [As Admin](#as-admin)
  - [Admin Dashboard, Publications and Requests](#admin-dashboard-publications-and-requests)

<br></br>
 

# As User
<p></p>

<div align="center">
<img alt="Read an Article" width=500 src="https://live.staticflickr.com/65535/51491912049_242ddff341_b.jpg" />
</div>


User is the simplest you can be in Feather's Flight.
Fortunately, Django offers an **User** model and also **authentication tools**.

Furthermore, Django provides a **Group** model too - this is used to differ users from authors. 

It becomes easy to manipulate those roles, as explained later on.
<br></br>


## Read an Article

<br></br>

<div align="center">
<img alt="Read an Article" src="https://media.giphy.com/media/LEo0WKMgQ621y0mjje/giphy.gif?cid=790b76116b46572d560b15945fb69c168345dd7afb70889b&rid=giphy.gif&ct=g" />
</div>

<br></br>

**Read an Article** turns to be the **<3** of **Feather's Fight**.

Every single user has the permission to browse through the pages and choose to see any available article.
The user is redirected to the page where the article is displayed. It is available to see its **Title**, **Text**, **Publication Date and Time**, and also the **Author's Username**, as shown in the picture below.

At the moment, user is limited to only read the article and further information.
*Future releases* will allow users to **rate the article** and also **comment and share opinion**.


## Sign up
Here is a very hospitable **Sign Up** Page.
<br></br>

<div align="center">
<img alt="Sign up" width=300 src="https://live.staticflickr.com/65535/51491201576_4248dcf2b8_z.jpg" />
</div>

As said, since user can only read articles, there is no really advantage in being a registered user (yet xD).


## Log in
With a beautiful feather displayed on screen, the Log In Page requires user's username and password. 
:D


<div align="center">
<img alt="Log in" width=300 src="https://live.staticflickr.com/65535/51492129010_41c691f907.jpg" />
</div>

## Become an author

<p></p>

This is the page which gives an ordinary user some powerful features.

<br></br>

<div align="center">
<img alt="Become an author" width=300 src="https://live.staticflickr.com/65535/51492129055_96ed041398.jpg" />
</div>

<br></br>

At the moment, this page allows everyone to become an author (being added to the Authors group).

It is required an **username**, an **email** and a **password** (*and its confirmation*).
If the username or email is already registered, or if passwords do not match, an error is displayed.

In futures releases, when various actions are provided to ordinary users, becoming an author will not be that easy ! >:(


<br></br>
# As Author
"With great power, comes great responsibilities." 

(Maybe this sentence should have been written in the "As Admin" section, but, from now on, an author can already have some special power)

<br></br>

<div align="center">
<img alt="As Author" width=500 src="https://live.staticflickr.com/65535/51491912139_d1f6480518.jpg" />
</div>

An Author grows the webpage up. They have their own dashboard. 

As an Author, it is possible to create a new article, edit it, save it, and, finally, submit it. 

Submit an article doesn't mean it will suddenly show up at the home page. An admin still need to approve it (or not) - we'll cover that in "As Admin" section.
 


## Dashboard

Here is where authors enjoy their free time. (Beautiful, isn't it ?)

<br></br>

<div align="center">
<img alt="Dashboard" src="https://media.giphy.com/media/rBja6oxIU7hjO9rB2x/giphy.gif?cid=790b761150a5338df12e27f7772bef1cfcb63ed3cab74fbb&rid=giphy.gif&ct=g" />
</div>

<br></br>

The Dashboard shows all author's publications, pending requests, and saved publications. 


## New Publication

Every time an author wants to publish a new article, the first thing to do is to click on "**New Publication**" (:O).

This leads the author to a friendly New Publication page, where will be written **title and content of the new article**.

<br></br>

<div align="center">
<img alt="New Publication" width=550 height=439 src="https://live.staticflickr.com/65535/51491201586_d0be78cd01.jpg" />
</div>

<br></br>

## Publications,  requests and saves

As you can see in the last picture, at bottom of the page, **the author can choose one of the follow items**:

- Submit - when author's work is ready to become a publication, this turns the new article into a **request** and redirect author to dashboard.
- Save  - this creates or replace a **save** in author's dashboard and the author can keep writing.
- Save and Return to Dashboard - this creates or replace a **save** in author's dashboard and redirect author to dashboard.
- Return to Dashboard  - as the name says.

*Very intuitive, right ?* :p

The **submit button** is very important. Once the author submit an article, in order to write a new article, he/she needs to **wait until an admin approve or decline it**.

<br></br>

# As Admin
Being an author is good, but being an admin is **wonderful** (*and dangerous*).

<br></br>

![Image of home page as admin](https://live.staticflickr.com/65535/51491201616_4e459a7c07.jpg)

<br></br>

An admin has **full control** of requests and publications.
In order to become an admin, it is necessary to contact other admin - there is no interface for this.


## Admin Dashboard, Publications and Requests
The Admin Dashboard allows an admin to visualize all current requests and if they are going to the home page, or come back to an author's dashboard.


- If the admin **approves** it, then this article will **show up at the home page** and **at author's dashboard as a publication**. 
- If the admin **declines** it, this article will **return to author's dashboard as a save**.

This dashboard also shows all current articles in the home page, and allows the admin to visualize and delete any, if needed.

<br></br>

![Image of Admin Dashboard](https://lh3.googleusercontent.com/b8EXwV7dkK9PoAQQPG7JfYyrXz20ZoxgPTMkWZITahUl-QNS4-lV--8be2IfrWhU04E1UWBppfhlqdf0I2TarYbnNVBnOkewiS0GiqOeR4e9tYHes-r2zh9k3RZCOLZnhpFJmPpn2T7dj0aep55hkaRgzxWMHtyYpVvgLSlLGfpNgwL9ZVlrqOk8QFmdrLhxCIj6vpweiFqOoTZhe4wo5-sF_gVK_01COyGjOjOAcwwNSSr0KjY5q9mWhvxCkzH67AOPS-1hDVB3UWg1aNqcaxgnXDjQQ-8DptQ6q0apAWalamPSaGGQwBO48QgKqcf6KD0AAb_ZaNpSzenyXDVuSBu19bzBZ8OgSjfGuDtAKPzN-3YHDfrWNIjpkPG5B_Y7lX2vwa4B0seAZqrVzRD1f3TEkMOUH9-LbBnCNGUrsdXUc9h0T_am_5JrzwLErK3tqNrdSproCatjdcJHmqrM3RE15QvkOZFlNBM2CBNsfwvUBcRiXHMkvJdHihIwiBj_-lXKtkHk3WQeRMjLlezqPuJ9mia0_g132CAlsZZqwNZ1TSeX5JL_jrZKsBYqmshD6j_IW_c-Qt3b50uMue8qhZNMQMMMhuHASTdZ1Xrxljt_5Y8OXLzFjmK0iKp8JGmLAL6tiKSLxppQ6wtToYMZfL-HqceFc8hqtLMbKa3Vft-x3C8nFeQP2dvHg5Ae_O9J5i0G4jyQteDbvnXOzNQHhQ=w1300-h811-no?authuser=1)


