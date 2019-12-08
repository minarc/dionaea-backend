import datetime

from mongoengine import Document, fields, EmbeddedDocument


class Prey(Document):
    shorten_key = fields.StringField(required=True, max_length=12)
    user_agent = fields.StringField(required=True)
    ip_address = fields.StringField(required=True)
    geo_point = fields.GeoPointField()
    region_name = fields.StringField()
    city = fields.StringField()
    accessed_at = fields.DateTimeField(default=datetime.datetime.now)


class Trap(Document):
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(primary_key=True, max_length=96)
    target_url = fields.URLField(required=True)
    memo = fields.StringField()
    expire = fields.DateTimeField()


class Maker(Document):
    email = fields.EmailField(unique=True)
