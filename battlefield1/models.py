# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Battlefield1Stats(models.Model):
    index = models.BigIntegerField(blank=True, null=True)
    rank = models.BigIntegerField(db_column='Rank', primary_key=True)  # Field name made lowercase.
    gamer = models.TextField(db_column='Gamer', blank=True, null=True)  # Field name made lowercase.
    game_score = models.BigIntegerField(db_column='Game Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    games = models.BigIntegerField(db_column='Games', blank=True, null=True)  # Field name made lowercase.
    platform = models.TextField(db_column='Platform', blank=True, null=True)  # Field name made lowercase.
    score_min = models.BigIntegerField(db_column='Score/min', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kill_ratio = models.FloatField(db_column='Kill Ratio', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    win_percent = models.FloatField(db_column='Win Percent', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    btr_score = models.BigIntegerField(db_column='BTR Score', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    hours_played = models.FloatField(db_column='Hours Played', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    kills = models.BigIntegerField(db_column='Kills', blank=True, null=True)  # Field name made lowercase.
    deaths = models.BigIntegerField(db_column='Deaths', blank=True, null=True)  # Field name made lowercase.
    wins = models.BigIntegerField(db_column='Wins', blank=True, null=True)  # Field name made lowercase.
    losses = models.BigIntegerField(db_column='Losses', blank=True, null=True)  # Field name made lowercase.
    accuracy = models.FloatField(db_column='Accuracy', blank=True, null=True)  # Field name made lowercase.
    flags_captured = models.BigIntegerField(db_column='Flags Captured', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    flags_defended = models.BigIntegerField(db_column='Flags Defended', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    head_shots = models.BigIntegerField(db_column='Head Shots', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'Battlefield1Stats'
