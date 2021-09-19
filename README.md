
<br></br>

<div align="center">
<img alt="Logo" src="https://live.staticflickr.com/65535/51492129080_082ac41c7b.jpg" />
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
  - [New Article](#new-article)
  - [Publications,  requests and saves](#publications--requests-and-saves)
- [As Admin](#as-admin)
  - [Admin Dashboard, Publications and Requests](#admin-dashboard-publications-and-requests)


<p></p>


# As User


<div align="center">
<img alt="Read an Article" width=500 src="https://live.staticflickr.com/65535/51491912049_242ddff341_b.jpg" />
</div>

<p></p>

User is the simplest you can be in Feather's Fight.

Fortunately, Django offers an **User** model and also **authentication tools**.

Furthermore, Django provides a **Group** model too - this is used to differ users from authors. 

It becomes easy to manipulate those roles, as explained later on.
<br></br>


## Read an Article

<div align="center">
<img alt="Read an Article" src="https://media.giphy.com/media/LEo0WKMgQ621y0mjje/giphy.gif?cid=790b76116b46572d560b15945fb69c168345dd7afb70889b&rid=giphy.gif&ct=g" />
</div>

<p></p>


**Read an Article** turns to be the **<3** of **Feather's Fight**.

Every single user has the permission to browse through the pages and choose to see any available article.
The user is redirected to the page where the article is displayed. It is available to see its **Title**, **Text**, **Publication Date and Time**, and also the **Author's Username**, as shown in the GIF above.

At the moment, user is limited to only read the article and further information.

Future releases will allow users to **rate the article** and also **comment and share opinion**.


## Sign up
Here is a very hospitable **Sign Up** Page.

<div align="center">
<img alt="Sign up" width=300 src="https://live.staticflickr.com/65535/51491201576_4248dcf2b8_z.jpg" />
</div>

<p></p>


As said, since user can only read articles, there is no really advantage in being a registered user (yet xD).


## Log in
With a beautiful feather displayed on screen, the **Log In** Page requires user's username and password. 
:D


<div align="center">
<img alt="Log in" width=300 src="https://live.staticflickr.com/65535/51492129010_41c691f907.jpg" />
</div>

## Become an author



This is the page which gives an ordinary user some powerful features.

<div align="center">
<img alt="Become an author" width=300 src="https://live.staticflickr.com/65535/51492129055_96ed041398.jpg" />
</div>

<p></p>

At the moment, this page allows everyone to become an author (being added to the Authors group).

It is required an **username**, an **email** and a **password** (*and its confirmation*).
If the username or email is already registered, or if passwords do not match, an error is displayed.

In futures releases, when various actions are provided to ordinary users, becoming an author will not be that easy ! >:(

# As Author
"With great power, comes great responsibilities." 

(Maybe this sentence should have been written in the "As Admin" section. But, from now on, an author already have some special power).


<div align="center">
<img alt="As Author" width=500 src="https://live.staticflickr.com/65535/51491912139_d1f6480518.jpg" />
</div>

<p></p>

An Author grows the webpage up. They have their own dashboard. 

As an Author, it is possible to create a new article, edit it, save it, and, finally, submit it. 

Submit an article doesn't mean it will suddenly show up at the home page. An admin still need to approve it (or not) - we'll cover that in the "As Admin" section.
 


## Dashboard

Here is where authors enjoy their free time. (Beautiful, isn't it ?)



<div align="center">
<img alt="Dashboard" src="https://media.giphy.com/media/2Qw8wR0BPMbhTyLtZJ/giphy.gif?cid=790b76114faed042b8c966c815f6c2e45febe4a980a43358&rid=giphy.gif&ct=g" />
</div>

<p></p>

The Dashboard shows author's published articles, pending requests and also saved articles. 


## New Article

Every time an author wants to publish a new article, the first thing to do is to click on "**New Article**" (:O).

This leads the author to a friendly New Article page, where  **title and content** will be written.


<div align="center">
<img alt="New Article" width=530 src="https://live.staticflickr.com/65535/51494742450_ab311028af.jpg" />
</div>

## Publications,  requests and saves

As you can see in the last picture, at bottom of the page, **the author can choose one of the follow items**:

- **Submit** - when author's work is ready to become a published article, this turns it into a new **request** and redirects author to dashboard.
- **Save**  - this creates or replaces a **save** in author's dashboard and the author can keep writing.
- **Save and Return to Dashboard** - this creates or replace a **save** in author's dashboard and redirects author to dashboard.
- **Return to Dashboard**  - as the name says.

*Very intuitive, right ?* :p

The **submit button** is also very important. Once the author has submitted an article, in order to write a new article, he/she will need to **wait until an admin approve or decline it**.

# As Admin
Being an author is good, but being an admin is **wonderful** (*and dangerous*).

<div align="center">
<img alt="Image of Home Page as Admin" width=550 src="https://live.staticflickr.com/65535/51491201616_4e459a7c07.jpg" />
</div>

<p></p>

An admin has **full control** of requests and publications.
In order to become an admin, it is necessary to contact other admin - there is no interface for this.


## Admin Dashboard, Publications and Requests
The Admin Dashboard allows an admin to visualize all current requests and if they are going to the home page, or coming back to an author's dashboard.


- If the admin **approves** it, then the article will **show up at the home page** and **at author's dashboard as a released article**. 
- If the admin **declines** it, then the article will **return to author's dashboard as a save**.

This dashboard also shows all current articles in the home page, and allows the admin to visualize and delete any, if needed.

<div align="center">
<img alt="Image of Admin Dashboard" width=550 src="https://live.staticflickr.com/65535/51491419278_5952335769.jpg" />
</div>
