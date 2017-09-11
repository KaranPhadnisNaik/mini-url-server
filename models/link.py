import sqlite3
from db import db

class LinksModel(db.Model):
    """
    LinksModel: SQLAlchemy Model for links table

    CREATE TABLE links (
        id INTEGER NOT NULL,
        url VARCHAR(200),
        hash_id INTEGER NOT NULL,
        hash VARCHAR(10),
        hits INTEGER,
        PRIMARY KEY (id)
    )
    """

    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    hash_id = db.Column(db.Integer)
    url = db.Column(db.String(200))
    hash = db.Column(db.String(10))
    hits = db.Column(db.Integer)

    #store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))
    #store = db.relationship('StoreModel')

    def __init__(self, url, hits, hash):
        #self.id = _id
        self.url = url
        self.hits = hits
        self.hash = hash

    def json(self):
        return {'url': self.url, 'hash': self.hash, 'hits': self.hits, 'id': self.id, 'hash_id': self.hash_id }

    @classmethod
    def find_by_url(cls, url):
        return cls.query.filter_by(url=url).first()

    @classmethod
    def find_by_hash(cls, hash):
        return cls.query.filter_by(hash=hash).first()

    @classmethod
    def hash_id_exists(cls, hash_id):
        return cls.query.filter_by(hash_id=hash_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
