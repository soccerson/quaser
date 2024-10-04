from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# データベースのURIを設定
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Job テーブルのモデル定義
class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    job_description = db.Column(db.String(255), nullable=False)
    num_of_people = db.Column(db.Integer, nullable=True)
    work_location = db.Column(db.String(255), nullable=False)
    budget = db.Column(db.String(50), nullable=False)
    payment_type = db.Column(db.String(50), nullable=False)
    deadline = db.Column(db.String(50), nullable=False)
    benefits = db.Column(db.String(255), nullable=False)

class School(db.Model):
    schoolName = db.Column(db.String(255), nullable=False)
    lat = db.Column(db.Integer, nullable=False)
    lng = db.Column(db.Integer, nullable=False)
    match_number = db.Column(db.Integer, nullable=False)
    winRate = db.Column(db.Integer, nullable=False)
    LostPointRate = db.Column(db.Integer, nullable=False)
    GetPointRate = db.Column(db.Integer, nullable=False)

def create_tables():
    db.create_all()
    insert_initial_data()


# 仕事を追加するエンドポイント
@app.route('/api/jobs', methods=['POST'])
def add_job():
    try:
        data = request.get_json()
        new_job = Job(
            job_description=data['jobDescription'],
            num_of_people=data['numpeople'],
            work_location=data['workLocation'],
            budget=data['budget'],
            payment_type=data['paymentType'],
            deadline=data['deadline'],
            benefits=data['benefits']
        )
        db.session.add(new_job)
        db.session.commit()
        return jsonify({"message": "仕事が追加されました"}), 201
    except Exception as e:
        print(f"Error occurred: {e}")
        return jsonify({"error": "内部サーバーエラーが発生しました"}), 500
 

# 仕事一覧を取得するエンドポイント
@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    result = [{"id": job.id, "title": job.title, "format": job.format, "category": job.category.name} for job in jobs]
    return jsonify(result)

@app.route('/api/school', methods=['GET'])
def get_school():
    schools = School.query.all()
    result = [{"schoolName": school.schoolName, "lan": school.lan, "lng": school.lng, "match_number": school.match_number, "winRate": school.winRate, "LostPointRate": school.LostPointRate, "GetPointRate": school.GetPointRate} for school in schools]
    return jsonify(result)

if __name__ == '__main__':
   # データベースのテーブルを作成
    with app.app_context():
        create_tables()

    # Flaskアプリケーションの実行
    app.run(debug=True)


def insert_initial_data(): 
    if not School.query.first(): 
        # データがない場合のみ初期データを挿入 
        user1=School(schoolName='横浜創英高校', lat=35.4908426, lng=139.6381515, match_number=1, winRate=0.85, LostPointRate=0.2, GetPointRate=1.8)
        user2=School(schoolName='千葉県立柏高校', lat=35.8932629, lng=139.9864032, match_number=2, winRate=0.80, LostPointRate=0.3, GetPointRate=1.7)
        user3=School(schoolName='桐光学園高校', lat=35.6026613, lng=139.469791, match_number=4, winRate=0.75, LostPointRate=0.35, GetPointRate=1.6)
        user4=School(schoolName='青森山田高校',lat=40.8039102, lng=140.7465038, match_number=5, winRate=0.75, LostPointRate=0.35, GetPointRate=1.6)
        user5=School(schoolName='前橋育英高校', lat=36.369293, lng=139.0620111, match_number=3, winRate=0.78, LostPointRate=0.25, GetPointRate=1.5)
        db.session.add(user1) 
        db.session.add(user2) 
        db.session.add(user3) 
        db.session.add(user4) 
        db.session.add(user5) 
        db.session.commit()