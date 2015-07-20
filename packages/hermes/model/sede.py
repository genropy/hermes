# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('sede',pkey='id',name_long='Sede',name_plural='Sedi',caption_field='denominazione')
        self.sysFields(tbl)
        tbl.column('denominazione',name_long='Denominazione')
        tbl.column('organizzazione_id',size='22',name_long='Organizzazione',group='_').relation('organizzazione.id',relation_name='sedi', onDelete='raise')
        tbl.column('indirizzo',name_long='Indirizzo')
        tbl.column('localita',name_long='Localita')
        tbl.column('nazione',size='2',name_long='Nazione',default='IT').relation('glbl.nazione.code',mode='foreignkey')
        tbl.column('provincia',size='2',name_long='Provincia').relation('glbl.provincia.sigla',mode='foreignkey')
        tbl.column('cap',name_long='Cap')
        tbl.column('telefono',name_long='Telefono')
        tbl.column('email',name_long='Email')
        tbl.column('note',name_long='Note')