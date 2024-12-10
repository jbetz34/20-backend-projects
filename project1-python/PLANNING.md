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
