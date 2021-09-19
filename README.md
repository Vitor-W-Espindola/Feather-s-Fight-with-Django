<div align="center">
<img alt="Read an Article" src="https://lh3.googleusercontent.com/V8MOxOcFMQhgg3ES5uMok_hPZNzKKJQf-E_QOIUIEwfiIQSQzlIeCRsZCO745tyBuTA3jY76I1zvcTnBsrWFCAMEm2aKew7686eUrvX18CXcuLtlwMG0rg8jK8nuxx5rUJENJWQG67ExZksxNgazR6Znj8wV-i4u_ob4eXBPiGMtOCgkbda1kC1LE-vByZEaMAQ4bTdTeJcvZsgL4Ks_KW7jvpbP-oCLWBcx6EJ6QUFl68YOvZGBEU3zX1z3a938WkKJbroaNBOBlx_EX1fsCZeNocYq_aBE2R5IeIyEhKWa8j0uTumz0cqjRHqFiNW7WWOXkpz49uutx29uPE_AUaQgIqY80mrzZZJZg8zkXmdtVhyWliLQVI-LpL3FIYXaJnoFIixfACQv0RfiQ6p8tC6YUUis2qC3pmqnpNjpdfwOI7hybufOoigIh5KXnHSxV8AMYdtvDanqeJ7plWX7k4OaeMD_ONoAItjCejBz9dJmLjOWwXTF0gV8VPRnba6FfHxx_flJ_96XeQSMngJRnouxaCs_XAdG2bEd58S6FeoyIOaDdRjrYy1Ik2Wm1ipu_3YqWsb3wi4fbDc9oHR9DtOma3tb-IGa0v5Nno13EW2the2paKww8zHV_hguIpv7wBJGOc7J-JAWeoDSlOGJAgLNnmvX2L_DUQpG91FxPS5nrFmEiumvZZucqiz1Gy2v0Bu1W4qxAq8aHU-FP3svcQ=w571-h156-no?authuser=1" />
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
<img alt="Read an Article" width=500 src="https://lh3.googleusercontent.com/YIXuW_lLbjrg33xKv_75M4ISgsMfcocOkVmP_bAZcnYy8FVatfp0o3Ry0-tfpXCAsF3xvd2xm_x9_DzwycVTd90H9suJAe0MgAVRW4OR-DsIdfTqGsVmBFKL2eLBjR1vjH6Z6bUsMB2WKcKIjIdYgsVq4s_VMDe0B2zRr7Jcx3bk9pq1K7xeC5MFTmvHkpYN-W41ACmE9iX2x90o-NXBTKFMbnsJigLI_I0gwNQo5H97sW52i2ONHKUmYgVpzSHHm94MpB0Uw8jpMN_bROu6HmO4_HayNv5arJbQEP2SlPksLGhgMxz1s7Kn0-ylvUxfv7tvl0IsGjaEctmuZJs219r8JC8NIktkRK4RgFckA6e-CX1tDGM-mb1CqhpCUp973EAb3f5e9oG-yg42HFqcM7XXE31Hf0rkC6nsVeURQ5wIT1_83nr0N4BYbXrmPTW0l9hnvV_-kgIFrDWkKJGdrgYsE9DD4CN_t6xpGwty-bTInoVELU1chKv3UDMGJlaXpA0NsD2UzlyiINNK_tIMIxiWYZ3NQ9dsLJB4bv-bqH4_Y82lmW3c58IDsL5H3uA52VtTxNJapLz5DqM781eO9bmw60j6iAepFpnywjztE9-CoAIu0vTR3MOjL02MGRBJxr0XQ_T0bG8L3bYWt0ibmGmMiC7_9RlsT0woaqXZYnBX16u9eLrmOgQXY3KPXugCb5IZMwx_R_IJDoD6V8LDHZc=w1057-h603-no?authuser=1" />
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
<img alt="Read an Article" width=300 src="https://lh3.googleusercontent.com/c8Adei44FmUZOshh5KeaTPnOfLDwUy2SJVrFbG6avWzVZI-juWvWnYYXsiuxkjYKUwKw8nwYImChUf_VSZhdd1qdGjKbgA855C3olqSoHkuCbCSSIKO4LN1rlhK2SLag9wPerBrv4zkj1ihjiZKCetTVHCrrjb_Fo_LTDJaJ4EMUaA1JXAfT1vy54K5vqxMg0Jq72ThuLmfh9vDr6AKxc1kRV9D-TJcTToRNK2VmqGQ7RN85VnRciW6IgIoLOtJAAX_BDMgBnoHEK5rs6pJ4UrDi2baVYG97Vk9snqp1z_uw8Q_xW7BblwUwGpi1ocz0I9buRURI-cALqKRTEucKo8LGOsmGqWvapqr-zufhVTl2raDjo00HXxGVBBYCWbAIU6tO1zuh23habAizUIaJL8_yLuYH65a0ml166MzUwN7MWBumK0fgwiM7y9Ju1WzHdLcn7AgGVw8jSlkY3ikmQ6qTBQvfigzBhSD7-6LWaqRuWoHBGUPiEypeuGM8zHJ2hWghovkRSYKcyCgEXT8Sr27Y07qGNbxtc3CHMMhPrlO5t74ZYMw7H0QmulbehZn2efJhYR5VzuZSUciAduL4OXcanGgKpdCM_L69BbeGT2oC8sWGk4ivLG-alVCbRZ0LU5vfJBuhyUOsV83v0-9nlo9M9VUzWJr-K0JC4DUX0cvunSMS84ep5gsT4i4iXJYWgvI1N8hd7WhAV4ZWxDutCw=w480-h628-no?authuser=1" />
</div>

<br></br>

As said, since user can only read articles, there is no really advantage in being a registered user (yet xD).


## Log in
With a beautiful feather displayed on screen, the Log In Page requires user's username and password. 
:D



<div align="center">
<img alt="Read an Article" width=300 src="https://lh3.googleusercontent.com/uENFKzfzSVPrBEjLj-Fc0yTRWgTypIjcsffE9nHxC3_8hdbSRLjb5xr5Fydb_35S1BB4DABJraH__QmN6bAszT0IRNJeWf_6dh8pOaRWwNIh09IPfy4ZM9U4qat1q7MEfOaQ8FdqndKtZShbJpD7ErbMuZy00FQAt_ZRky9adMbVetM8Urq2lJO9Vj6EdnVequ7yFUbUDiCXekRAqC8kw7BDE6gCvwJbfefdkmn2KEqHU9NkqD_VrVhBMvw2xFUwbxFeVMhX4nGl__HYENb8D16fqxOsxQS6ge2y5Hy9HZ7I3wtbbj0pZcoFMeITZ5ZJVS564ll8wCitVOQIoh3PPAwPyUnDKUXVnb6RyEOKk6dlouF-F1hYtonMd2estkdFGuAxVu1iVTg9mVk-0pkvQA4gvkKO0y0PK4EJY0mb7Pr5mNMJWszbnH-ilQCKKZuKsFcb-Z2az-JHzzl_HYoe_vRsZbHw9Zmbqh1JhgO4J6S-mlP-ukBAXx32Pa-AM5U6Dx-41YzJqQXpdrwoemHJ1i9UAEuH-3lw821zVV5pTP4Zi2gdUuAc4GZ2nyugQI9Pgsx4Mvp8ABP6btaSTTd2ENqQyR7kW5PG8sN2vz6EKrf6lPHA2tWJuc7dQG-1jK8oXtpZSHg6vouzXdbY3C4NCY6pDqhsXw4Gjm4QqA1_kMmMJBnPFYR1CsnCXpowoE95Y2kCOD00Su_5Xwwx9YG6PQ=w484-h552-no?authuser=1" />
</div>

## Become an author

<p></p>

This is the page which gives an ordinary user some powerful features.

<br></br>

<div align="center">
<img alt="Read an Article" width=300 src="https://lh3.googleusercontent.com/mmsQ2qt7kENZiX9P49zZOeLLfaUnMQCb3ozHahmUX2CEj5O0yezbyAzNXj5-fUHB60aGAGEB2SO3pLyqmDarvxkOvB822gdXGVPhCWpNw220U5MFA3tNnHIdnFSxn6uD56x4VQkKv_GHdBeZoYi7RJZQN_l61RQGQWIu1USSlBTbbIQqLgLUpDGDBhEmDJZcXPGJWcyCC2yf_kHeb7Hkw2Ck4tMnLmWkwbUxBj_iDyoH0Df_fY6fmUTm_Sannr0cbTZevCa1dJONCUM695aTNL_C4Up4HmyJ7jMK_PH2D6i7ecdgDbUiEoa2K-99trL4btGu0fB0cx8Eh8jmiMHMFpqtqVp8pfqT_yd8JDW-r0tI3pVvUxTNKJ2ajYxGbU1Ex1hhzod19u_xOha9c_7rJuGoYvruea49MwbOA7v8GjBSsI0ONyTEffqogX8zQKCNiet4-JkipC8xDrcPNuTy749wAFvwZodn2_89wA2O29rlYex65nPNDgI-V1F6U7OKWw27tjhV55gG9IIvCdUnGlQ7F7LmzWxtNNn7Cqiv74ZfjmvoC6znCZEeXOSwbuHSXUk2U9W9tcrHBxPtTb4ikdcOzb-Jd3QLZ8v7OQWveRWVvssHhpE8DQCK50ciGKfeoWrUdQ5kSyutxTso__NlOtOWN9V47HUe6Z_xJ6RlBsYg5HCbdEr2rGgWhsAPipiQ7f-nnlkmq_Bt0IenT-f1iQ=w464-h636-no?authuser=1" />
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
<img alt="Read an Article" width=500 src="https://lh3.googleusercontent.com/YOusjDTbh9drbFwzoOBQc29otAc-XpgVidwSiM1kwP_bYfee7AGkF9RqsyBMJt1kZ68Sjxhlj3KPOOPrV7fgb_BT9lOibY-6RooMZLyd2dkx96VMdCB4Dp3g1Zk2IVftBYKTDcF-ObyrxlLXomLNZWjm_aecZXusFuzuBWMem5qveU9ENa187zoKcml7iiHUDg6ptF63P6ZOyYdyJnytdrZLGNWriGC6SUiJrjPgx5tp88_2ZZ57f4OgVkcLSXlNpIUyCC4WbbUVFiX98xpzfo539jp-49NvvFZ9vGv05YrfISTBuwpwpeJulFrdtopB_P2BpAGT_DMyDZDYw_EctKsFYx1kCVOiN26j4XPySOlzo3sOSeiRmM6UDkd4WJtsFwviUQCsMjdpCtjcscfX094qwVdPESPHykhlj02W45Bp5_fWh5U8WtGKL7X7jokJKZN6qyeL-fZOW9RNDQTAXSP6rXfHOt7-s2XlZIBhn6p0php4mYOUAz5MXOWwwZ7fOBKs1gJozC1XTm_bYyjMkAfKkaHVjfJUSOn98OggfTauuyDtgXsnSXdpaAMN7ClTXQhamBtwU3iaRV3vDeRNcuRNLSQQKRMET3FaFWq5pPiihlozAhtygzldD9nwBibc6jXFniNSh2ejjUgahnw1DPOPNO0O-XrOo2-K2Os0PLXr6tiKmPcYPUgJKFMsfX0XfhsRHpvtiDKQRWpIWGLUPw=w1032-h681-no?authuser=1" />
</div>


<br></br>

An Author grows the webpage up. They have their own dashboard. 

As an Author, it is possible to create a new article, edit it, save it, and, finally, submit it. 

Submit an article doesn't mean it will suddenly show up at the home page. An admin still need to approve it (or not) - we'll cover that in "As Admin" section.
 


## Dashboard

Here is where authors enjoy their free time. (Beautiful, isn't it ?)

<br></br>

<div align="center">
<img alt="Read an Article" src="https://media.giphy.com/media/rBja6oxIU7hjO9rB2x/giphy.gif?cid=790b761150a5338df12e27f7772bef1cfcb63ed3cab74fbb&rid=giphy.gif&ct=g" />
</div>

<br></br>

The Dashboard shows all author's publications, pending requests, and saved publications. 


## New Publication

Every time an author wants to publish a new article, the first thing to do is to click on "**New Publication**" (:O).

This leads the author to a friendly New Publication page, where will be written **title and content of the new article**.

<br></br>

<div align="center">
<img alt="Read an Article" width=550 height=439 src="https://lh3.googleusercontent.com/WaJTjYc3yA7ZUoFhc6wahpo6t6Ti242DNXomldRl1QNtEQXsMnjdrxGfFEqyw_jPUK8e0640DyI2y4qLQ1Y3UPb5wUXcs5Zg-SYFlZJVyWdUkqh_JjFoazlulOjFqgeb85PbPZ4rJWe1jU0UxKaSTotsEJq0NmF3fSzbtL3gOzPEJtHMy2j-GNR47PJv10UU5HsCECV_sLdtvGWmGhxb7QhPpHerOMzQOSrXIqvR0LB_rfTQ4bh6RowJDZU26J4yTmsvv3yzA2vVFyVU_n2woNqx4B6Nh4ff1Chl44llBUBLjN-1Rle6TNRzkYImJT0-v9eST7c7Ofw9unkF5L3lSVzU1CPOflylB6tToTTZYOS0cs332fld1FtiZUdteawwwDG4detsR150OuhfRML6ywOGxbRhN5iaOc8lKxY9bYULifwWIDjodIoVi8wDcEq-qJ2Jxe2I_I8MgHCQv0zi3lQpc8Cb_6G975RHoUb1YUcu-rsL2T4TOuHfazbtwDumJfKSpBdtxLFAk6xA_54PsOfEgca-EEh_O-UwtG1nO0XW5hvm9mx_dc-zhS6UNO3s4Zl4EkDNlXSEjTm8k5G6OQsLRsjk5WdIwRmuy7CvRQ8G94EykJBE2fiOfqK8oGJeY0a6RprgZLl_t005i71pEY7GysPpp3pLhS2WTr0LjSOO65nfTXEjxOn5jI6U2Q9oG5iete0JGyy8LaEzxPPe0g=w1101-h879-no?authuser=1" />
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

![Image of home page as admin](https://lh3.googleusercontent.com/kIaMqARCIPTuw4Wwrr7WhLBdkxuezGn1Sw0MiFle_CMaEC5uIuXddRtRmrBTvo5Wwk8utZFHycYYmV6WL1o_PErtkZ17mLFU937Kw3RN6d7dBpLWBypid7Nzcdi-XQ2GUttyQVA3HtYmLJPfZADOQMWg2JlDkrnLgxVE4EAXCFRP0iqRlRyZo2lbAwtE6-xNbcFAkWINTct2lT_QtwoUUPX1olBVs4QUA4eufRvJuPe3qRveBc5ndj7qs7WINpU52hGucfgT8Pev48rnOrN83JDj21C0F9pHceO1xXUt2_EDnv02MG4XqELf77ImpdpTl7rM2Vk06IapKTQYLMcLk5dQeF-d3zMCNeT_GwGIsdSxTVmvJbmuN01r63X9wUCUnCOh2d9FtOV-XSBlz0lAlTUxqJ-xHddFloTjQL_YjTq2nQuLDEM4lCjikuvwKTk5oUWUsWwnyK0XnZPEAd5q23NG_9OxMmB_u_bM42rSzZXpFFt8I1I_8p177F3OU7DpNlgqn8WW5Q3d6Qt-BqXy6abgC1o94sxrcStfI6LJWsHl8pWthqRBaItF_DKh1uUNLQfRlO5Qg4zEmvr3pDk5UAarwc-5yORudmmbw0mQxmR2WoTGXcC8fUXyR2OE8SA467xxouXmR9BA2ptWTW07_dduJHg-bBK5V6aF005JPNzAIanzoEfRNwIEepf_2YUcI7VVDUfB56lsz4Eoj9YocQ=w1074-h704-no?authuser=1)

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


