from flask import Flask,render_template,request,flash,redirect,url_for
app=Flask(__name__)
dict1={}
dictionary={}
users=[]

@app.route('/login')
def login():
    return render_template('log.html')

@app.route('/reg.html')
def register():
    return render_template('reg.html')

@app.route('/reg.html',methods=['POST'])
def getregister():
    error=None
    #taking inputted data
    users=dictionary.keys()
    uname=request.form['user']
    name=request.form['name']
    mail=request.form['emailid']
    pwd=request.form['pass']
    pwd1=request.form['pass1']
    


    if uname in users:
        error="Username already exists"
        return render_template('pass.html',u=error)
    elif len(pwd)<8:
        error="Password length must be minimum 8 characters"
        return render_template('pass.html',u=error)
    elif pwd!=pwd1:
        error="Please enter correct password to confirm"
        return render_template('pass.html',u=error)
    else:
        dictionary[uname]=pwd
        error="Account Created Successfully"
        return render_template('pass.html',u=error)
        
        
        
        
        
    
@app.route('/login',methods=['POST'])
def getvalue():
    error=None
    username=request.form['uname']
    password=request.form['pass']
	
    
    
    
    


        
    users=dictionary.keys()   
    if username in users:
        
        if password==dictionary[username]:
            #login successfully
            error="Login successfully"
            return render_template('pass.html',u=error)

        else:
            #login unsuccessfull
                
            error="Username or password is invalid"
            return render_template('pass.html',u=error)

        
        
    
    
    
    
        
	
    


if __name__=='__main__':
    app.run()

login()
register()
getvalue()
    