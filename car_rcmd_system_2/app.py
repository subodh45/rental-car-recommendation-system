from flask import *
import pickle

app = Flask(__name__)
@app.route("/" ,methods=["GET","POST"])
def home():
      if request.method=="POST":
          f = open("CRP.model", "rb")
          model = pickle.load(f)
          f.close()  
 
          num=float(request.form["num"])
          if ((num >=9) or (num<=0)):
              return render_template("home.html", m="No. of person must be between 0 to 8 :")
          else: 
            
              budget=float(request.form["budget"])
              if budget<=299:
                    return render_template("home.html", m="budget must be greater than 300:")
              else:
                    fuel=request.form["fuel"]                      
                    if fuel == "Petrol":
                          d=[[num,budget,0,0,1]]
                    elif fuel == "Electrical":     
                          d=[[num,budget,0,1,0]]
                    else :
                          d=[[num,budget,1,0,0]]
              
                    result=model.predict(d)
                    if result == "budget is low":
                         return render_template("home.html", m= result[0] + ", for 8 seater car minimum budget is 1000")  
                    else:
                         return render_template("home.html", m="Best Car for you is " + result[0])   
      else:
          return render_template("home.html")
if __name__ == "__main__":
  app.run(debug =True, use_reloader=True)