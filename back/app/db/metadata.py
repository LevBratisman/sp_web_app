# Import all the models, so that Base has them before being
# imported by Alembic

from app.common import model  # noqa
from app.common.model.base import Base  # noqa