#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class ViewFromOrganizzazione(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('denominazione')
        r.fieldcell('indirizzo')

    def th_order(self):
        return 'denominazione'

    def th_query(self):
        return dict(column='denominazione', op='contains', val='')



class FormFromOrganizzazione(BaseComponent):

    def th_form(self, form):
        tc = form.center.tabContainer(margin='2px')
        fb = tc.contentPane(title='Informazioni sede',datapath='.record').formbuilder(cols=4, border_spacing='4px',colswidth='auto',
                                                        width='750px',fld_width='100%')
        fb.field('denominazione',colspan=4)
        fb.geoCoderField('^.$indirizzo_completo', 
                     colspan=4,
                     lbl='Cerca indirizzo',
                     selected_street_address_eng='.indirizzo',
                     selected_locality='.localita',
                     selected_postal_code='.cap',
                     selected_administrative_area_level_2 ='.provincia',
                     selected_country='.nazione',
                     #selected_position='.geocoords',
                     ghost='Indirizzo localita  provincia',
                     speech=True)     
        fb.field('indirizzo',colspan=3)
        fb.field('cap')
        fb.field('localita',colspan=2)
        fb.field('provincia',hasDownArrow=False)
        fb.field('nazione')
        fb.field('email',colspan=2)
        fb.field('telefono',colspan=2)
        fb.field('note',editor=True,height='150px',colspan=4)
        tc.contentPane(title='Staff').dialogTableHandler(relation='@membri_staff',pbl_classes=True,margin='2px',viewResource='ViewFromSede')

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='780px')
