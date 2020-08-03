from app import *
from models.user import User
from models.recipe import Recipe
from extensions import db
app = create_app()





def my_function():
    with app.app_context():
        user = User.query.filter_by(username='GMParyani').first()
        partha = Recipe(name='Best Pizza Paratha', description='AMI Favorite', num_of_serving=60,
                       cook_time=30, directions='Ask AMI about it.', user_id=user.id)
        db.session.add(partha)
        db.session.commit()

        biryani = Recipe(name='Mutton Biryani', description='Papa Loves It.', num_of_serving=60,
                       cook_time=60, directions='Ask AMI about it.', user_id=user.id)
        db.session.add(biryani)
        db.session.commit()






my_function()