from django.db import models

from symposion.proposals.models import ProposalBase


class PyConProposalCategory(models.Model):

    name = models.CharField(max_length=100)
    slug = models.SlugField()
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = "PyCon proposal category"
        verbose_name_plural = "PyCon proposal categories"


class PyConProposal(ProposalBase):
    
    AUDIENCE_LEVEL_NOVICE = 1
    AUDIENCE_LEVEL_EXPERIENCED = 2
    AUDIENCE_LEVEL_INTERMEDIATE = 3
    
    AUDIENCE_LEVELS = [
        (AUDIENCE_LEVEL_NOVICE, "Novice"),
        (AUDIENCE_LEVEL_INTERMEDIATE, "Intermediate"),
        (AUDIENCE_LEVEL_EXPERIENCED, "Experienced"),
    ]

    category = models.ForeignKey(PyConProposalCategory)
    audience_level = models.IntegerField(choices=AUDIENCE_LEVELS)

    class Meta:
        abstract=True


class PyConTalkProposal(PyConProposal):
    
    DURATION_CHOICES = [
        (0, "No preference"),
        (1, "I prefer a 30 minute slot"),
        (2, "I prefer a 45 minute slot"),
    ]
    
    extreme = models.BooleanField(
        default=False,
        help_text = "'Extreme' talks are advanced talks with little or no introductory material. See <a href='http://us.pycon.org/2012/speaker/extreme/' target='_blank'>http://us.pycon.org/2012/speaker/extreme/</a> for details."
    )
    duration = models.IntegerField(choices=DURATION_CHOICES)
    
    class Meta:
        verbose_name = "PyCon talk proposal"


class PyConTutorialProposal(PyConProposal):
    class Meta:
        verbose_name = "PyCon tutorial proposal"


class PyConPosterProposal(PyConProposal):
    class Meta:
        verbose_name = "PyCon poster proposal"