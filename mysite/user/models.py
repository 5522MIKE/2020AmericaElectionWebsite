from django.db import models


# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=100)
    vote_candidate = models.ForeignKey('vote.Candidate', null=True, blank=True, on_delete=models.SET_NULL)
    state = models.ForeignKey('vote.State', null=True, blank=True, on_delete=models.SET_NULL)

    @property
    def info(self):
        info = {
            'id': self.id,
            'name': self.name,
            'vote_candidate': self.vote_candidate.name,
            'candidate_id': self.vote_candidate.id,
            'state': self.state.name,
            'state_id': self.state.id
        }
        return info
