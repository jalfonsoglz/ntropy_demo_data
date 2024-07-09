import random
import time
from datetime import datetime, timedelta
from faker import Faker
from faker.providers import internet
from odoo import models, fields, api


class NtropyDemoDataGenerator(models.Model):
    _name = 'ntropy.demo.data.generator'
    _inherit = ['mail.thread', 'mail.activity.mixin', 'utm.mixin']
    _description = 'Generador de datos'

    name = fields.Char()
    qty_data = fields.Integer(default=1)

    def fake_contacts(self):
        fake = Faker('es_MX')
        fake.add_provider(internet)
        contact = self.env['res.partner']
        contacts_range = self.qty_data
        start_time = time.time()
        msj = ""

        for i in range(contacts_range):
            name = fake.name()
            postcode = fake.postcode()
            street = fake.street_address()
            job = fake.job()
            # bank_account = fake.aba()
            # bank_clabe = fake.clabe()

            contact_vals = {
                'name': name,
                'function': job,
                'state_id': random.randint(485, 516),
                'street': street,
                'phone': '5544332211',
                'mobile': '5544332211',
                'zip': postcode,
                'country_id': self.env.ref('base.mx').id,
                # 'vat': vat,
                'lang': 'es_MX',
                'is_company': False,
                'customer_rank': True,
                'supplier_rank': False,
                # 'category_id': self.env.ref('ntropy_demo_data_generator.user_test_category').id,
                # 'bank_id': random.randint(1, 93),
                # 'acc_number': bank_account,
                # 'acc_holder_name': name,
                # 'l10n_mx_edi_clabe': bank_clabe,
            }

            contact.create(contact_vals)

        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        msj += f"Se crearon {contacts_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Contacts"})

    def generate_sale_orders(self):
        sale_order_obj = self.env['sale.order']
        customers = self.env['res.partner'].search([('category_id.name', 'in', ['Cliente'])
                                                    ])
        sales_order_range = self.qty_data
        products = self.env['product.product'].search([
            ('default_code', 'in', ['CONSUL', 'ALM-NAC', 'ALM-IMP', 'SYSNET'])
        ])
        random_source = self.env['utm.source'].search([])
        # users = self.env['res.users'].search([])
        payment_term_id = self.env.ref('account.account_payment_term_15days').id

        start_time = time.time()
        msj = ""

        for i in range(sales_order_range):
            partner_id = customers[i % len(customers)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(customers)
            # users_id_random = random.choice(users)
            random_source_random = random.choice(random_source)
            if partner_id and product_id:
                sale_order_obj.create({
                    'partner_id': partner_id_random.id,
                    'payment_term_id': payment_term_id,
                    'source_id': random_source_random.id,
                    # 'user_id': users_id_random.id,
                    'order_line': [(0, 0, {
                        'product_id': product_id,
                        'product_uom_qty': random.randint(1, 5),
                    })],
                }).action_confirm()

        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        msj += f"Se crearon {sales_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Sale Orders"})
        return True

    def generate_expenses_orders(self):
        expenses_order_obj = self.env['purchase.order']
        supplier = self.env['res.partner'].search([('category_id.name', 'in', ['Proveedor'])])
        purchase_order_range = self.qty_data
        products = self.env['product.product'].search([
            ('default_code', 'in', ['ADUANA', 'NOMINA', 'CONTA', 'RRHH', 'FLETE'])
        ])
        # users = self.env['res.users'].search([])
        payment_term_id = self.env.ref('account.account_payment_term_45days').id
        msj = ""

        start_time = time.time()

        for i in range(purchase_order_range):
            partner_id = supplier[i % len(supplier)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(supplier)
            # user_id_random = random.choice(users)
            if partner_id and product_id:
                expenses_order_obj.create({
                    'partner_id': partner_id_random.id,
                    'payment_term_id': payment_term_id,
                    # 'user_id': user_id_random.id,
                    'order_line': [(0, 0, {
                        'product_id': product_id,
                        'product_uom_qty': random.randint(1, 5),
                    })],
                }).button_confirm()

        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        msj += f"Se crearon {purchase_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Expenses Orders"})
        return True

    def generate_purchase_orders(self):
        purchase_order_obj = self.env['purchase.order']
        supplier = self.env['res.partner'].search([('category_id.name', 'in', ['Proveedor'])])
        purchase_order_range = self.qty_data
        products = self.env['product.product'].search([
            ('default_code', 'in', ['ALM-NAC', 'ALM-IMP'])
        ])
        # users = self.env['res.users'].search([])
        payment_term_id = self.env.ref('account.account_payment_term_advance_60days').id
        msj = ""

        start_time = time.time()

        for i in range(purchase_order_range):
            partner_id = supplier[i % len(supplier)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(supplier)
            # user_id_random = random.choice(users)
            if partner_id and product_id:
                purchase_order_obj.create({
                    'partner_id': partner_id_random.id,
                    'payment_term_id': payment_term_id,
                    # 'user_id': user_id_random.id,
                    'order_line': [(0, 0, {
                        'product_id': product_id,
                        'product_uom_qty': random.randint(1, 5),
                    })],
                }).button_confirm()

        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)
        msj += f"Se crearon {purchase_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Purchase Orders"})
        return True

    def generate_customer_invoices(self):
        customer_invoice_obj = self.env['account.move']
        invoice_order_range = self.qty_data
        customers = self.env['res.partner'].search([('category_id.name', 'in', ['Cliente'])])
        products = self.env['product.product'].search([
            ('default_code', 'in', ['CONSUL', 'ALM-NAC', 'ALM-IMP', 'SYSNET'])
        ])
        msj = ""
        counter = 0

        start_time = time.time()

        for i in range(invoice_order_range):
            partner_id = customers[i % len(customers)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(customers)
            current_date = fields.Date.today()
            start_date = current_date - timedelta(days=365 * 3)
            end_date = current_date
            random_date_str = f"{random.randint(start_date.year, end_date.year)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_date = datetime.strptime(random_date_str, '%Y-%m-%d').date()
            if partner_id and product_id:
                customer_invoice_obj.create({
                    'journal_id': self.env.ref('account.1_sale').id,
                    'move_type': 'out_invoice',
                    'auto_post': 'at_date',
                    'invoice_date': random_date,
                    'partner_id': partner_id_random.id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': product_id,
                        'quantity': random.randint(1, 5),
                    })],
                })
            counter += 1

        customer_invoice_obj._autopost_draft_entries()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        msj += f"Se crearon y validaron {invoice_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Customer Invoices"})
        return True

    def generate_customer_invoices_40(self):
        customer_invoice_40_obj = self.env['account.move']
        invoice_order_range = self.qty_data
        customers = self.env['res.partner'].search([('category_id.name', 'in', ['Cliente'])])
        products = self.env['product.product'].search([
            ('default_code', 'in', ['CONSUL', 'ALM-NAC', 'ALM-IMP', 'SYSNET'])
        ])
        msj = ""
        counter = 0

        start_time = time.time()

        for i in range(invoice_order_range):
            partner_id = customers[i % len(customers)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(customers)
            current_date = fields.Date.today()
            start_date = current_date - timedelta(days=365 * 3)
            end_date = current_date
            random_date_str = f"{random.randint(start_date.year, end_date.year)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_date = datetime.strptime(random_date_str, '%Y-%m-%d').date()
            if partner_id and product_id:
                customer_invoice_40_obj.create({
                    'journal_id': self.env.ref('ntropy_demo_data_generator.account_journal_mx_sale_invoice').id,
                    'move_type': 'out_invoice',
                    'auto_post': 'at_date',
                    'invoice_date': random_date,
                    'partner_id': partner_id_random.id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': product_id,
                        'quantity': random.randint(1, 5),
                    })],
                })
            counter += 1

        customer_invoice_40_obj._autopost_draft_entries()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        msj += f"Se crearon y validaron {invoice_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Customer Invoices"})
        return True

    def generate_supplier_invoices(self):
        supplier_invoice_obj = self.env['account.move']
        invoice_order_range = self.qty_data
        supplier = self.env['res.partner'].search([('category_id.name', 'in', ['Proveedor'])])
        products = self.env['product.product'].search([
            ('default_code', 'in', ['ADUANA', 'NOMINA', 'CONTA', 'RRHH', 'FLETE'])
        ])
        msj = ""
        counter = 0

        start_time = time.time()

        for i in range(invoice_order_range):
            partner_id = supplier[i % len(supplier)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(supplier)
            current_date = fields.Date.today()
            start_date = current_date - timedelta(days=365 * 3)
            end_date = current_date
            random_date_str = f"{random.randint(start_date.year, end_date.year)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_date = datetime.strptime(random_date_str, '%Y-%m-%d').date()
            if partner_id and product_id:
                supplier_invoice_obj.create({
                    'move_type': 'in_invoice',
                    'auto_post': 'at_date',
                    'invoice_date': random_date,
                    'partner_id': partner_id_random.id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': product_id,
                        'quantity': random.randint(1, 5),
                    })],
                })
            counter += 1

        supplier_invoice_obj._autopost_draft_entries()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        msj += f"Se crearon y validaron {invoice_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Supplier Invoices"})
        return True

    def generate_customer_credit_note(self):
        customer_credit_note_obj = self.env['account.move']
        invoice_order_range = self.qty_data
        customers = self.env['res.partner'].search([('category_id.name', 'in', ['Cliente'])])
        products = self.env['product.product'].search([
            ('default_code', 'in', ['DESC', 'ANT'])
        ])
        payment_term_id = self.env.ref('account.account_payment_term_immediate').id
        msj = ""
        counter = 0

        start_time = time.time()

        for i in range(invoice_order_range):
            partner_id = customers[i % len(customers)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(customers)
            current_date = fields.Date.today()
            start_date = current_date - timedelta(days=365 * 3)
            end_date = current_date
            random_date_str = f"{random.randint(start_date.year, end_date.year)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_date = datetime.strptime(random_date_str, '%Y-%m-%d').date()
            if partner_id and product_id:
                customer_credit_note_obj.create({
                    'journal_id': self.env.ref('ntropy_demo_data_generator.account_journal_mx_sale_credit_note').id,
                    'move_type': 'out_refund',
                    'auto_post': 'at_date',
                    'invoice_date': random_date,
                    'partner_id': partner_id_random.id,
                    'l10n_mx_edi_payment_method_id': 17,
                    'l10n_mx_edi_usage': 'G02',
                    'invoice_payment_term_id': payment_term_id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': product_id,
                        'quantity': random.randint(1, 5),
                        'price_unit': 1000,
                    })],
                })
            counter += 1

        customer_credit_note_obj._autopost_draft_entries()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        msj += f"Se crearon y validaron {invoice_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Customer Credit Note"})
        return True

    def generate_supplier_credit_note(self):
        supplier_credit_note_obj = self.env['account.move']
        invoice_order_range = self.qty_data
        supplier = self.env['res.partner'].search([('category_id.name', 'in', ['Proveedor'])])
        products = self.env['product.product'].search([
            ('default_code', 'in', ['DESC', 'ANT'])
        ])
        payment_term_id = self.env.ref('account.account_payment_term_immediate').id
        msj = ""
        counter = 0

        start_time = time.time()

        for i in range(invoice_order_range):
            partner_id = supplier[i % len(supplier)].id
            product_id = products[i % len(products)].id
            partner_id_random = random.choice(supplier)
            current_date = fields.Date.today()
            start_date = current_date - timedelta(days=365 * 3)
            end_date = current_date
            random_date_str = f"{random.randint(start_date.year, end_date.year)}-{random.randint(1, 12)}-{random.randint(1, 28)}"
            random_date = datetime.strptime(random_date_str, '%Y-%m-%d').date()
            if partner_id and product_id:
                supplier_credit_note_obj.create({
                    'journal_id': self.env.ref('ntropy_demo_data_generator.account_journal_mx_purchase_credit_note').id,
                    'move_type': 'in_refund',
                    'auto_post': 'at_date',
                    'invoice_date': random_date,
                    'partner_id': partner_id_random.id,
                    'invoice_payment_term_id': payment_term_id,
                    'invoice_line_ids': [(0, 0, {
                        'product_id': product_id,
                        'quantity': random.randint(1, 5),
                        'price_unit': 1000,
                    })],
                })
            counter += 1

        supplier_credit_note_obj._autopost_draft_entries()
        end_time = time.time()
        elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

        msj += f"Se crearon y validaron {invoice_order_range} en un tiempo total transcurrido: {minutes} minutos {seconds} segundos"
        self.message_post(body=msj)
        self.write({'name': "Supplier Credit Note"})
        return True
