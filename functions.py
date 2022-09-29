import json


def load_posts():
    with open("posts.json", "r", encoding='utf-8') as file:
        posts = json.load(file)
        return posts


def search_posts_by_word(word):
    posts = load_posts()
    result = []
    for post in posts:
        if word.lower() in post['content'].lower():
            result.append(post)
    return result


def add_post(post):
    posts = load_posts()
    posts.append(post)
    with open("posts.json", "w", encoding='utf-8') as file:
        json.dump(posts, file)
