#!/usr/bin/python
# -*- coding: UTF-8 -*-

def config(root,application=None):
    hermes = root.branch('Hermes')
    hermes.thpage('Organizzazioni',table='hermes.organizzazione')
    hermes.thpage('Profili',table='hermes.profilo')
    hermes.thpage('Sedi',table='hermes.sede')
    hermes.thpage('Staff',table='hermes.staff')
