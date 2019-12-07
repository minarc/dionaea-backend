import datetime

from mongoengine import Document, fields, EmbeddedDocument


class Prey(Document):
    user_agent = fields.StringField(required=True)
    ip_address = fields.StringField(required=True)
    geo_point = fields.GeoPointField()
    region_name = fields.StringField()
    city = fields.StringField()
    accessed_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(required=True, max_length=12)


class Trap(Document):
    created_at = fields.DateTimeField(default=datetime.datetime.now)
    shorten_key = fields.StringField(primary_key=True, max_length=96)
    target_url = fields.URLField()
    memo = fields.StringField()
    expire = fields.DateTimeField()
    # users = fields.ListField(fields.EmbeddedDocumentField(Prey), default=[])


class Test(EmbeddedDocument):
    test = fields.StringField()


class Maker(Document):
    email = fields.EmailField(unique=True)
    traps = fields.ListField(fields.EmbeddedDocumentField(Test))
