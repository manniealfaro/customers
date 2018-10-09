# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Cliente(models.Model):
	id = models.IntegerField(primary_key=True)

	class Meta:
		verbose_name = "Cliente"
		verbose_name_plural = "Clientes"

	def __str__(self):
		pass
    