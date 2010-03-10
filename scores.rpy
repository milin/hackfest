from twisted.web import resource
import teams

class Scores(resource.Resource):
    def render_GET(self, request):
        teamsjs = []
        for t in teams.teams:
            teamsjs.append(t.json() + '\n')
        s = '[' + ', '.join(teamsjs) + ']'
        return s

    def render_POST(self, request):
        return request.content.getvalue()

resource = Scores()
