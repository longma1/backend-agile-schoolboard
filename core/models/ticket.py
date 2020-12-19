from django.db import models

from core.models import Board


class Ticket(models.Model):
    TODO = 'TD'
    PROGRESS = 'IP'
    DONE = 'DN'
    SUBMITTED = 'SB'
    RETURNED = 'RT'
    TICKET_STATE_CHOICES = (
        (TODO, 'To Do'),
        (PROGRESS, 'In Progress'),
        (DONE, 'Done'),
        (SUBMITTED, 'Submitted'),
        (RETURNED, 'Returned')
    )
    ticket_id = models.UUIDField(primary_key=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(
        max_length=2,
        choices=TICKET_STATE_CHOICES,
        default=TODO,
    )