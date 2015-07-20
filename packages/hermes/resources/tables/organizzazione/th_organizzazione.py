#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('codice')
        r.fieldcell('denominazione')

    def th_order(self):
        return 'codice'

    def th_query(self):
        return dict(column='codice', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer()
        fb = bc.contentPane(region='top',datapath='.record').formbuilder(cols=2, border_spacing='4px')
        fb.field('codice')
        fb.field('denominazione')
        bc.contentPane(region='center').dialogTableHandler(relation='@sedi',viewResource='ViewFromOrganizzazione',
                                                            formResource='FormFromOrganizzazione',pbl_classes=True,margin='2px')


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
