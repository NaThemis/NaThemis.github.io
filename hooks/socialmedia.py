from textwrap import dedent

from urllib import parse

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://facebook.com/sharer/sharer.php"


def on_page_markdown(markdown, **kwargs):
    page = kwargs.get("page")
    config = kwargs.get("config")

    if page.meta.get("template") != "blog-post.html":
        return markdown

    page_url = config.site_url + page.url
    page_title = parse.quote(page.title + "\n\n")

    return markdown + dedent(f"""
    <div class="social-media" markdown="1">  
    [Share on :simple-x:](https://x.com/intent/tweet?text={page_title}&url={page_url})
    [Share on :simple-facebook:](https://facebook.com/sharer/sharer.php?u={page_url})
    </div>
    """)
