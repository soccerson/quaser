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


def create_tables():
    db.create_all()


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

if __name__ == '__main__':
   # データベースのテーブルを作成
    with app.app_context():
        create_tables()

    # Flaskアプリケーションの実行
    app.run(debug=True)
