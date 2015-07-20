# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('profilo',pkey='id',name_long='Profilo',name_plural='Profili',caption_field='cognome_nome')
        self.sysFields(tbl)
        tbl.column('nome',name_long='Nome')
        tbl.column('cognome',name_long='Cognome')
        tbl.column('indirizzo',name_long='Indirizzo')
        tbl.column('localita',name_long='Localita')
        tbl.column('nazione',size='2',name_long='Nazione',default='IT').relation('glbl.nazione.code',mode='foreignkey')
        tbl.column('provincia',size='2',name_long='Provincia').relation('glbl.provincia.sigla',mode='foreignkey')
        tbl.column('cap',name_long='Cap')
        tbl.column('telefono',name_long='Telefono')
        tbl.column('email',name_long='Email')
        tbl.column('note',name_long='Note')

        tbl.formulaColumn('cognome_nome',"$cognome || ' ' ||$nome ",name_long='Cognome e nome')