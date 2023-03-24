## python开发

[toc]

### 0. 写在前面

教学视频[最新Python的web开发全家桶（django+前端+数据库）_哔哩哔哩_bilibili](https://www.bilibili.com/video/BV1rT4y1v7uQ/?spm_id_from=333.999.0.0&vd_source=f81f71e09eb1ed647995c0e3176fa3ed)

自己会的没有笔记

### 1. 前端开发

##### 1. 快速上手

```python
from flask import Flask
app = Flask(__name__)

#创建了一个网址和函数的对应关系
#若用户访问地址则自动执行index函数
@app.route("/show/info")
def index():
    return "中国联通"

#if __name__ == "__main__":作为脚本直接生效，作为模块导入其他文件则不会生效，常测试使用
#实际运行时要加上/show/info才能访问
#文件会在后台一直运行
if __name__ == "__main__":
    app.run()
```


- **将返回的部分加上前端的标签，就可以使字体样式改变。**

- ==web框架== ：**支持将前端代码写入到文件中**

```python
@app.route("/show/info")
def index():
    #后加文件路径
    return render_template("index.html")
```

**文件默认到项目的`templates` 目录中找**


- 可以自行定义主机名和端口名


```python
app.run(host="",port=8000)
```



##### 2.网络请求

- 在URL写入地址，点击访问
- 浏览器发送数据，本质上是字符串 `"GET /explore http1.1\r\n\host..."` 
- **GET请求：**跳转、向后台传入数据会拼接在URL上，**也可以表单提交** 
- **POST请求：**向后台提交数据，一般是表单，数据不在URL中，数据在`Form Data` 中（请求体中）



#### 2. 用户注册

1. 首先完成一个注册界面

   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
       <meta charset="UTF-8">
       <meta http-equiv="X-UA-Compatible" content="IE=edge">
       <meta name="viewport" content="width=device-width, initial-scale=1.0">
       <title>register</title>
   </head>
   <body>
       <h1>用户注册</h1>
       <div>注册：
           <input type="text" name="" id="">
       </div>
       <div>密码：
           <input type="password" name="" id="">
       </div>
       <input type="submit" value="提交信息">
   </body>
   </html>
   ```

2. **提交** ：可以写在URL（GET）中提交，也可以以POST方式以隐蔽的方式提交

   - ==提交数据需要将需要提交的数据使用**`form`** 包裹==
   - **`<form method="get" action="提交的地址">`** ，**==提交方式和地址==** 
   - **form标签里还应有submit** 

   ```html
   <form method="get" action="提交的地址">
           <div>注册：
               <input type="text" name="" id="">
           </div>
           <div>密码：
               <input type="password" name="" id="">
           </div>
       	<input type="button" value="按钮" onclick="alert('qqqqq')">
           <input type="submit" value="提交信息">
   </form>
   ```

   - **会将输入的值和name结合输入到后台**，故想要提交要**==命名标签==** （便于区分数据，类似于字典）

   ```html
   <div>注册：
       <input type="text" name="uu" id="">
   </div>
   <div>密码：
   	<input type="password" name="pp" id="">
   ```




3. **加入地址，在该地址函数返回注册成功**



4. **接收数据** 

   ```python
   #在后台打印接收数据
   @app.route('/do/reg')
   def do_reg():
       #1. 接收到数据(GET)
       print(request.args)
       #2. 返回结果
       return "注册成功"
   ```

   返回的数据





5. **使用POST提交**：==没有从URL中提交== 

```html
<form method="post" action="/post/reg">
    <div>注册：
    	<input type="text" name="uu" id="">
    </div>
    <div>密码：
    	<input type="password" name="pp" id="">
    </div>
    <input type="submit" value="提交信息">
    <input type="button" value="信息按钮" onclick="alert('qqqqq')">
</form>
```

```python
@app.route('/post/reg',methods = ['POST'])
def post_reg():
    #1. 接收到数据(GET)
    print(request.form)
    #2. 返回结果
    return "注册成功"
```


