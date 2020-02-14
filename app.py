from flask import Flask
import time
import utility

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello,Folks the application is deployed in k8s cluster"

@app.route("/api/v1/truncatableprime/<inputNumber>")
def truncatableprime_controller(inputNumber):
   enteredTime = time.time()
   try:
       inputNumber=int(inputNumber)
       hasZeroOrCount = utility.checkZeroOrLenghth(inputNumber)
       if (type(hasZeroOrCount) == bool and bool(hasZeroOrCount)==True) or hasZeroOrCount<1:
           completionTime=time.time()
           return {"Status": "OK", "ExecutionTimeMs": (completionTime - enteredTime), "Result": str(False)  }
       else:
           result= utility.checkTrucatablePrime(inputNumber,hasZeroOrCount)
           completionTime=time.time()
           return {"Status": "OK", "ExecutionTimeMs": (completionTime - enteredTime), "Result": str(result)  }
       
   except :
       return {"Status": "OK", "Result": "Please enter Valid Input"  }

if __name__ == "__main__":
    app.run()
