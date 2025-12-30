from flask import Flask 
app = Flask(__name__)

@app.route('/') 
def hello(): 
    return '<h1> 上傳成功 Hello, World! </h1>'

if __name__ == '__main__':
    app.run(debug=True)

# 註冊 @app 有個實體方法叫 route 當有人訪問 / 時就會執行function 叫hello 
# 回傳 hello world
#<h1> </h1>是html的方式，h1為最大標題字
# http:://127.0.01 代表本機的ip位置;
# port 5000之類的數字代表不同的應用程式埠號 ;
# 目前用8000的port服務