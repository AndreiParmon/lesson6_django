from django.db import models
from random import choice


class HeadsAndTailsModel(models.Model):
    SIDE = ['heads', 'tails']

    side = models.CharField(max_length=10, default=choice(SIDE))
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Монета упала стороной "{self.side}"'

    @staticmethod
    def get_info(n):
        info = HeadsAndTailsModel.objects.all()[-n:]
        head_count = sum(i.side == 'heads' for i in info)
        tail_count = n - head_count
        return {'head_count': head_count, 'tail_count': tail_count}
