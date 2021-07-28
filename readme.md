## Threaded Comment System Design
### Initial setup
```sh
- git clone https://github.com/yashahmad/ThreadedComment
- cd ThreadedComment
- pipenv install
- cd Commentsytem
- python manage.py runserver
```

### Task
- Get a list of all comments made on a page with a given URL.
- Add a new comment on a page with a given URL.
- Add a new sub-comment on an already existing comment as a reply.
- Edit an existing comment.
- Delete a single comment or an entire comment thread using the comment's identifier.

### REST API
> To acesss REST API http://localhost:8000/api/
> To use interactive playground for REST API Interface http://localhost:8000/docs/

### Routes
```sh
#Task 1- Get a list of all comments made on a page with a given url
http://localhost:8000/api/page/<uuid:pk>/all/
Pass the page id as uuid (primary key)

# Task 2- Add a new comment on a page with a given url
http://localhost:8000/api/page/<uuid:pk>/comment/
Pass the page id as uuid (primary key)

# Task 3- Add a new sub comment on an already existing comment as a reply
http://localhost:8000/api/page/<uuid:pk>/comment/<uuid:cpk>/subcomment
Pass the page id as uuid and comment id as another uuid (cpk)

# Task 4- Edit an existing comment
# Task 5- Delete a single comment or an entire comment thread using comment's identifier
[http://localhost:8000/api/comment/<uuid:pk>]
Pass the uuid for the comment
```

#### If you want to access uuid for any entity like page, comment, subcomment, then just access the below routes for GET, POST verbs
> http://localhost:8000/api/page/ for Pages
> http://localhost:8000/api/comment/ for Comments
> http://localhost:8000/api/subcomment/ for Subcomments

#### If you want to access CRUD for the routes
> http://localhost:8000/api/page/<uuid:pk> for Pages
> http://localhost:8000/api/comment/<uuid:pk> for Comments
> http://localhost:8000/api/subcomment/<uuid:pk> for Subcomments
###### id is automatically populated , just type name/description leave id as blank
