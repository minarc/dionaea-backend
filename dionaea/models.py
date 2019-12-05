import datetime

from mongoengine import Document, fields, EmbeddedDocument


class User(EmbeddedDocument):
    user_agent = fields.StringField(required=True)
    ip_address = fields.StringField(required=True)
    datetime = fields.DateTimeField()


class Meta(EmbeddedDocument):
    og_image = fields.URLField()
    og_title = fields.StringField()


class Trap(Document):
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(primary_key=True, max_length=96)
    target_url = fields.URLField()
    memo = fields.StringField()
    expire = fields.DateTimeField()
    users = fields.ListField(fields.EmbeddedDocumentField(User), default=[])


class Test(Document):
    user_agent = fields.StringField(required=True)
    ip_address = fields.StringField(required=True)
    geo_point = fields.GeoPointField()
    region_name = fields.StringField()
    city = fields.StringField()
    accessed_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(required=True, max_length=96)
