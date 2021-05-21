import web 

render=web.template.render('app/views/')

class Ubuntu():
    def GET(self):
      try:
        return render.insert()
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)