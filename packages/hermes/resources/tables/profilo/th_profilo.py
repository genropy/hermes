#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('cognome_nome')
        r.fieldcell('email')
        r.fieldcell('indirizzo')
        r.fieldcell('localita')
        r.fieldcell('provincia')
        r.fieldcell('cap')
        r.fieldcell('telefono')

    def th_order(self):
        return 'nome'

    def th_query(self):
        return dict(column='nome', op='contains', val='')



class Form(BaseComponent):

    def th_form(self, form):
        pane = form.record
        fb = pane.div(margin_right='20px').formbuilder(cols=4, border_spacing='4px',colswidth='auto',width='750px',fld_width='100%')
        fb.field('nome',validate_case='c',validate_notnull=True,colspan=2)
        fb.field('cognome',validate_case='c',validate_notnull=True,colspan=2)
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
        fb.field('indirizzo',colspan=4)
        fb.field('localita',cospan=3)
        fb.field('cap')
        fb.field('provincia',colspan=2)
        fb.field('nazione',colspan=2)
        fb.field('email',colspan=3)
        fb.field('telefono')
        fb.field('note',editor=True,height='150px',colspan=4)


    def th_options(self):
        return dict(dialog_height='400px', dialog_width='600px')
