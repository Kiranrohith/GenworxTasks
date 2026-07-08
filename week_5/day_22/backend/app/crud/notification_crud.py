from sqlalchemy.orm import Session

from app.models.models import Notifications
from app.schemas.notifications_schemas import notification_create


def get_notification(db: Session):
    return db.query(Notifications).order_by(Notifications.created_at.desc()).first()


def create_notification(db: Session, notification_data: notification_create):
    notifications = Notifications(
        title=notification_data.title,
        server_message=notification_data.server_message,
        not_type=notification_data.not_type,
    )
    db.add(notifications)
    db.commit()
    db.refresh(notifications)
    return notifications