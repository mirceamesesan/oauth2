from fastapi import FastAPI
from app.models import PostSchema

posts = [
    {
        "id": 1,
        "title": "Post Title 1",
        "content": "Post Content 1"
    },
    {
        "id": 2,
        "title": "Post Title 2",
        "content": "Post Content 2"
    }
]

users = []


app = FastAPI()

# ===================
# Get test
# ===================
@app.get("/", tags=["Root"])
async def root():
    return { "message": "Hello World" }


# ===================
# Get posts
# ===================
@app.get("/posts", tags=["Posts"])
async def get_posts():
    return {"data": posts}


# ===================
# Get post by id
# ===================
@app.get("/posts/{post_id}", tags=["Posts"])
async def get_post(post_id: int):

    if post_id > len(posts):
        return { "error": "No post found" }
    
    for post in posts:
        if post["id"] == post_id:
            return { "data": post }


# ===================
# Post a new post
# ===================
@app.post("/posts", tags=["Posts"])
async def create_post(post: PostSchema):
    post.id = len(posts) + 1
    posts.append(post.model_dump())
    return { "info": f"Post: '{post}', added" }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app)