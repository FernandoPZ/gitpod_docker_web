import web

urls = (
    '/', 'app.controllers.index.Index',
    '/docker', 'app.controllers.docker.Docker',
    '/ubuntu', 'app.controllers.ubuntu.Ubuntu',
)
app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()
