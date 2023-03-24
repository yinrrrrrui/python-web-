from flask import Flask,render_template
app = Flask(__name__)

#创建了一个网址和函数的对应关系
#若用户访问地址则自动执行index函数
@app.route("/show/info")
def index():
    #后加文件路径
    return render_template("index.html")

#注意不同页面的函数名不能相同
@app.route("/table")
def student():
    return render_template("student.html")

@app.route("/input")
def input():
    return render_template("input.html")
#if __name__ == "__main__":作为脚本直接生效，作为模块导入其他文件则不会生效，常测试使用
#实际运行时要加上/show/info才能访问
#文件会在后台一直运行
if __name__ == "__main__":
    app.run()
