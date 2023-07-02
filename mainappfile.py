
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

'''

@app.route('/')
def afunc():
    return "test get request was success on endpoint port from requreiements.txt., usually 5000"

if __name__=='__main__':
    app.run()
'''
##@app.route('/funcs_for_hampton_nutrition', methods=["POST"])
class Add(Resource):
    def post(self):
        ##get the inputs, use import jsonify and request as well
        postedData = request.get_json()
        x = postedData["x"]
        ##aaa = x
        aaa={x:450}
        bbb=[aaa, {x:500}]
        ccc=[x,500]
        if x == 'fresh squeezed orange juice':
            aaa1=aaa[x]
        elif x == 'smoothie':
            aaa1=ccc[1]
        else:
            aaa1=150
        y =4700
        z = ['banana', 'fresh squeezed orange juice', 'smoothie']
        ##x = int(x)
        ##y = int(y)
        ret = aaa1
        ##ret = aaa[x]
        retMap = {
            'From the menu items you chose these are the mg of potassium you have or will consume': ret,
            'Status COde': 200,
            'The Percent that was consumed of your recommended daily intake of potassium is ': aaa1/y,
            'The menu item you chose and entered above:': x,
            'THe other menu items you can try are:  (menu items added daily to this api)': z
        }
        return jsonify(retMap)
'''
    dataDict = request.get_json()
    x = dataDct["x"]
    #
    y = 4700
    z= y-x
    #prepare json
    retJSON = {
        "z":z
    }
    #return jsonify map prepared
    return jsonify(retJSON)
'''

api.add_resource(Add, "/funcs_for_hampton_nutrition")

if __name__=='__main__':
    app.run()

x=10
'''
alistofitems = [23,25,24,23]

def checkingevenslist(evenslist):
    evenslist1 = []
    for n in evenslist:
        if n%2 == 0:
            evenslist1.append(n)
        else: pass
    return False
##note let's push from Intlelij so globally need to set that username for the repo:  
git config --global user.name "EduardoContr" ref https://www.jetbrains.com/help/idea/commit-and-push-changes.html

    
'''
