import web 

render=web.template.render('app/views/')

class Index():
    def GET(self):
      try:
        return render.index()
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)