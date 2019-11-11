from invoke import Collection, task
from tasks import db, aave, currencies

namespace = Collection(db, aave, currencies)