import datetime

from mongoengine import Document, fields, EmbeddedDocument


class User(EmbeddedDocument):
    user_agent = fields.StringField(required=True)
    ip_address = fields.StringField(required=True)
    datetime = fields.DateTimeField()


class Trap(Document):
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(primary_key=True, max_length=96)
    target_url = fields.URLField()
    memo = fields.StringField()
    expire = fields.DateTimeField()
    users = fields.ListField(fields.EmbeddedDocumentField(User))
