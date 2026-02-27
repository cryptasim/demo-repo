from flask import Flask,request

app=Flask(__name__)

@app.route("/add",methods=["POST"])
def add():
    data=request.json
    a=data.get("a")
    b=data.get("b")
    if a==None or b==None:
        return {"error":"Missing values"},400
    return {"result":a+b}
