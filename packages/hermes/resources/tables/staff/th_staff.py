#!/usr/bin/python
# -*- coding: UTF-8 -*-

from gnr.web.gnrbaseclasses import BaseComponent
from gnr.core.gnrdecorator import public_method

class View(BaseComponent):

    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('profilo_id')
        r.fieldcell('sede_id')
        r.fieldcell('user_id')

    def th_order(self):
        return 'profilo_id'

    def th_query(self):
        return dict(column='profilo_id', op='contains', val='')

    def th_options(self):
        return dict(widget='dialog')

class ViewFromSede(BaseComponent):
    def th_struct(self,struct):
        r = struct.view().rows()
        r.fieldcell('profilo_id')
        r.fieldcell('user_id')

    def th_order(self):
        return 'profilo_id'



class Form(BaseComponent):

    def th_form(self, form):
        bc = form.center.borderContainer(datapath='.record')
        bottom = bc.borderContainer(region='bottom',height='120px')
        bottom.contentPane(region='left',width='50%').linkerBox('user_id',label='Informazioni Utente',
                                                                formUrl='/adm/user_page',dialog_height='400px',
                                                                 dialog_width='680px',validate_notnull=True,
                                                                 validate_notnull_error='!!Richiesto',
                                                                 default_firstname='=#FORM.record.@profilo_id.nome',
                                                                 default_lastname='=#FORM.record.@profilo_id.cognome',
                                                                 default_email='=#FORM.record.@profilo_id.email',
                                                                 default_status='C',margin='2px',
                                                                 openIfEmpty=True)
        bottom.contentPane(region='center').linkerBox('sede_id',validate_notnull=True,
                                                        validate_notnull_error='!!Richiesto',
                                                        margin='2px',openIfEmpty=True)
        fb = bc.roundedGroup('Profilo',region='center').div(margin_right='20px').formbuilder(cols=4, border_spacing='4px',colswidth='auto',
                                                        width='750px',fld_width='100%')
        fb.field('@profilo_id.nome',validate_case='c',validate_notnull=True,colspan=2)
        fb.field('@profilo_id.cognome',validate_case='c',validate_notnull=True,colspan=2)
        fb.geoCoderField('^.$indirizzo_completo', 
                     colspan=4,
                     lbl='Cerca indirizzo',
                     selected_street_address_eng='.@profilo_id.indirizzo',
                     selected_locality='.@profilo_id.localita',
                     selected_postal_code='.@profilo_id.cap',
                     selected_administrative_area_level_2 ='.@profilo_id.provincia',
                     selected_country='.@profilo_id.nazione',
                     #selected_position='.geocoords',
                     ghost='Indirizzo localita  provincia',
                     speech=True)     
        fb.field('@profilo_id.indirizzo',colspan=3)
        fb.field('@profilo_id.cap')
        fb.field('@profilo_id.localita',colspan=2)
        fb.field('@profilo_id.provincia',hasDownArrow=False)
        fb.field('@profilo_id.nazione')
        fb.field('@profilo_id.email',colspan=2)
        fb.field('@profilo_id.telefono',colspan=2)

        fb.field('@profilo_id.note',editor=True,height='150px',colspan=4)

    def th_options(self):
        return dict(dialog_height='500px', dialog_width='780px')
