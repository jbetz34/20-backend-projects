# Personal Blogging Platform API
*Difficulty:* Easy

*Skills and technologies used:* CRUD for main operations, databases (SQL or NoSQL), server-side RESTful API.

![blog api diagram](/docs/images/project1-blog_api_diagram.png)

Let’s start with a very common one when it comes to backend projects.

This is a RESTful API that would power a personal blog. This implies that you’d have to create a backend API with the following responsibilities:

- Return a list of articles. You can add filters such as publishing date, or tags.
- Return a single article, specified by the ID of the article.
- Create a new article to be published.
- Delete a single article, specified by the ID.
- Update a single article, again, you’d specify the article using its ID.

And with those endpoints you’ve covered the basic CRUD operations (*C*reate, *R*ead, *U*pdate and *D*elete).

As a recommendation for techstack, you could use Fastify as the main backend framework if you’re going with Node, or perhaps Django for Python or even Ruby on Rails or Sinatra for Ruby. As for your database, you could use MongoDB if you want to try NoSQL or MySQL if you’re looking to get started with relational databases first.

---

# Planning

*Expected Functionalities:*
- Return a list of articles. You can add filters such as publishing date, or tags.
  - Expecting a GET command here. Probably to a /articles link
  - Should allow filters: (as parameters in the body or in the link? can I do both? )
  - Equality tags are easy, can I do '>' '<' or 'in'? What fields support what? 
- Return a single article, specified by the ID of the article.
  - This one is easy, just use the flask variable
- Create a new article to be published.
  - POST command here, to the article path
- Delete a single article, specified by the ID.
  - DELETE command here, to the article path with flask variable
- Update a single article, again, you’d specify the article using its ID.
  - POST command here, to the article path with flask variable

*Database schema*
Tables/Columns:
- articles
  - id (primary key) (not null)
  - created_at (not null) 
  - updated_at (not null) 
  - title
  - author
  - body
- article_tags
  - article_id (not null)
  - tag (not null)

*Query Strategies*
need a joining strategy of some sort. kms

For now I will ignore tags and come back to them. Especially with the API filter strategy up in the air
Another thing - I only will only parse non-primary-key key/values from the body of the request instead of url

---

# Learnings

- DELETE & PUT commands
- Filtering on multivalue columns
