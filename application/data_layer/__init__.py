from .models import RealEstate
from .dao import RealEstateDAO
from .unit_of_work import UnitOfWork
from application import db

uow = UnitOfWork(db.session)
