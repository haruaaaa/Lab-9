from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask('Step Tracker')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///steps.db'
db = SQLAlchemy(app)

class StepRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String(10), nullable=False) 
    steps = db.Column(db.Integer, nullable=False)

@app.route('/')
def main():
    records = StepRecord.query.order_by(StepRecord.date.desc()).all()
    return render_template('task_veb.html', records_list=records)

@app.route('/add', methods=['POST'])
def add_record():
    data = request.json
    new_record = StepRecord(date=data['date'], steps=data['steps'])
    db.session.add(new_record)
    db.session.commit()
    return jsonify({'status': 'success', 'id': new_record.id})

@app.route('/clear', methods=['DELETE'])
def clear_records():
    try:
        db.session.query(StepRecord).delete()
        db.session.commit()
        return jsonify({'status': 'success'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)