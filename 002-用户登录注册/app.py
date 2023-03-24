from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/register',methods=['GET'])
def register():
    return render_template("register.html")

@app.route('/do/reg',methods=['GET'])
def do_reg():
    #1. 接收到数据(GET)
    print(request.args)
    #2. 返回结果
    return "注册成功"

@app.route('/post/reg',methods = ['POST'])
def post_reg():
    #1. 接收到数据(GET)
    print(request.form)
    #2. 返回结果
    return "注册成功"

if __name__ == '__main__':
    app.run()