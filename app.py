from flask import Flask, send_from_directory

app = Flask(__name__, static_url_path='')
appContext = app.app_context()
appContext.push()

# 配置环境
from Commons.PathParser import proPath, devPath
from Config.MyConfig import MyConfig

MyConfig.initConfig(proPath)

# 注册蓝图
from Routes.wxRouter import wxRouter
from Routes.scriptRouter import scriptRouter

app.register_blueprint(blueprint=wxRouter, url_prefix='/wx')
app.register_blueprint(blueprint=scriptRouter, url_prefix='/script')

appContext.pop()


@app.route('/')
def defaultPage():
    return 'this is a flask project'


# 设置icon
@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.svg')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=MyConfig.myPort, debug=MyConfig.debug)
