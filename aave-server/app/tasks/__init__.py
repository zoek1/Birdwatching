from invoke import Collection, task
from tasks import db, aave

namespace = Collection(db, aave)