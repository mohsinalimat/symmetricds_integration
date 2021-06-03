# Copyright (c) 2021, AvN Technologies and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from symmetricds_integration.symmetricds_integration.utils import model_insert, model_load_from_db, model_db_update, model_get_list, model_delete_from_table

doctype = 'Symmetric Job'
table_name = 'sym_job'
name_field = 'job_name'
primary_keys = ['job_name']
has_creation = True
has_modified = True
has_modified_by = True

class SymmetricJob(Document):
	
	def db_insert(self):
		model_insert(self,doctype,table_name,name_field,primary_keys,
    		has_creation,has_modified,has_modified_by)

	def load_from_db(self):
		model_load_from_db(self,doctype,table_name,name_field,primary_keys,has_creation,has_modified,has_modified_by)


	def db_update(self):
		model_db_update(self,doctype,table_name,name_field,primary_keys,has_creation,has_modified,has_modified_by)
	
	def get_list(self, args):
		return model_get_list(self,doctype,table_name,name_field,primary_keys,has_creation,has_modified,has_modified_by, args)
	
	def delete_from_table(self, doctype, name, ignore_doctypes, doc):
		model_delete_from_table(self,doctype,table_name,name_field,primary_keys,has_creation,has_modified,has_modified_by, name, ignore_doctypes, doc)
	 	