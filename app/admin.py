from app import app, db
from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin

from app.model import Category, Product

admin = Admin(app=app, name="My Website", template_mode='bootstrap4', url='/admin')



class ProductView(ModelView):
    can_view_details = True
    column_display_pk = True
    can_export = True
    column_searchable_list = ['name', 'description']
    column_filters = ['name', 'description']
    column_exclude_list = ['image']
    column_labels = {
        'name': 'Ten',
    }
    column_sortable_list = ['name', 'id']

admin.add_view(ModelView(Category, db.session))
admin.add_view(ProductView(Product, db.session))
