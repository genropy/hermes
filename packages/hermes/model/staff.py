# encoding: utf-8

class Table(object):
    def config_db(self,pkg):
        tbl =  pkg.table('staff',pkey='id',name_long='Staff',name_plural='Staff',caption_field='id')
        self.sysFields(tbl)
        tbl.column('profilo_id',size='22',name_long='Profilo',group='_').relation('profilo.id',mode='foreignkey', one_one=True)
        tbl.column('sede_id',size='22',name_long='Sede',group='_').relation('sede.id',relation_name='membri_staff', onDelete='raise')
        tbl.column('user_id',size='22',name_long='User',group='_').relation('adm.user.id',one_one=True)
