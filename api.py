from main import api,app
from Controller.UserApi import UserApi
from Controller.ScoreBoardApi import ScoreBoardApi

api.add_resource(ScoreBoardApi,"/scoreboard/<string:userguid>")
api.add_resource(UserApi,"/user")
if __name__ == '__main__':
    app.run(debug=True)