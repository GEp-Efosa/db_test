from .models import DbTest
from .extensions import ma
from marshmallow import post_load

class DbTestInputSchema(ma.SQLAlchemySchema):
    """risk assessment inut schema"""
    
    class Meta:
        model = DbTest

    @post_load
    def create_load(self, data, **kwargs):
        return DbTest(**data)
    

class DbTestResponse(ma.SQLAlchemySchema):
    """risk assessment response schema"""

    class Meta:
        model = DbTest
    
    float_field = ma.auto_field(dump_only=True)
    string_field = ma.auto_field(dump_only=True)
    integer_field = ma.auto_field(dump_only=True)