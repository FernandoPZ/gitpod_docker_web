import web 

render=web.template.render('app/views/')

class Docker():
    def GET(self):
      try:
        return render.list()
      except Exception as e:
        return "--E-R-R-0-R--" + str(e.args)