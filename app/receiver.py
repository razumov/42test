from django.db.models.signals import post_save, post_delete
from models import Request, Person, LogModel


def log(sender, **kwargs):
    if sender not in (Request, Person):
        return
    log_model = LogModel(model=str(sender))
    if 'created' in kwargs:
        log_model.action = ('Created', 'Changed')[int(kwargs['created'])]
    else:
        log_model.action = "Deleted"
    log_model.save()


post_save.connect(log)
post_delete.connect(log)