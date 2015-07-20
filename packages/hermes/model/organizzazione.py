# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('organizzazione',pkey='id',name_long='Organizzazione',name_plural='Organizzazioni',caption_field='denominazione')
        self.sysFields(tbl)
        tbl.column('codice',size=':10',name_long='Codice')
        tbl.column('denominazione',size=':100',name_long='Denominazione')
