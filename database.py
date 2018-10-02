from flask import Flask, render_template, request, jsonify
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
from marshmallow import Schema, fields


def gen_connection_string():
    # if not on Google then use local MySQL
    if not os.getenv('SERVER_SOFTWARE', '').startswith('Google App Engine/'):
        return 'mysql://root@localhost/admin'
    else:
        conn_name = os.environ.get('CLOUDSQL_CONNECTION_NAME' '')
        sql_user = os.environ.get('CLOUDSQL_USER', 'root')
        sql_pass = os.environ.get('CLOUDSQL_PASSWORD', '')
        conn_template = 'mysql+mysqldb://%s:%s@/admin?unix_socket=/cloudsql/%s'
        return conn_template % (sql_user, sql_pass, conn_name)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = gen_connection_string()
db = SQLAlchemy(app)

# SQLAchemy model
class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.Unicode(80), nullable=False)
    title = db.Column(db.Unicode(255), nullable=False)
    body = db.Column(db.UnicodeText())
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Post %r>' % self.title

# Marshmallow serialization schema
class PostSerializer(Schema):
    id = fields.Integer()
    author = fields.Str()
    title = fields.Str()
    body = fields.Str()
    created_at = fields.DateTime()
