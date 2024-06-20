from flask import Flask,request,jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgresql://postgres:Abhi%402001@localhost:5432/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db = SQLAlchemy(app)

class Item(db.Model):
    __tablename__='login'

    id=db.Column(db.Integer , primary_key=True)
    phone=db.Column(db.Integer,unique=True)
    password= db.Column(db.String(120),unique=True)

    def __repr__(self):
        return f'<Item {self.id}>'

    def myfun(self):
        return{
            'id':self.id,
            'phone':self.phone,
            'password':self.password

        }

@app.route('/items',methods=['GET'])
def getitems():
    items=Item.query.all()
    return jsonify([item.myfun() for item in items])


@app.route('/items/<int:id>',methods=['GET'])
def itemsid(id):
    item=Item.query.get_or_404(id)
    return jsonify(item.myfun())

# @app.route('/senditem', methods=['POST'])
# def postit():
#     data = request.get_json()  
#     if not data:
#         return jsonify({"message": "No input data provided"}), 400

#     newitem = Item(phone=data['phone'], password=data.get('password'))
#     try:
#         db.session.add(newitem)
#         db.session.commit()
#         return jsonify(newitem.myfun()), 200
#     except IntegrityError:
#         db.session.rollback()
#         return jsonify({"message": "Item with that phone already exists"}), 409

# @app.route('/del/<int:id>',methods=['DELETE'])
# def deletei(id):
#     item = Item.query.get_or_404(id)
#     db.session.delete(item)
#     db.session.commit()

#     return "item deleted" ,204




if __name__=="__main__":
    app.run()
