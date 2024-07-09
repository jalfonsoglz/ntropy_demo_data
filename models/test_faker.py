# -*- coding: utf-8 -*-
import csv
import random
import time
from faker import Faker
from faker.providers import internet
fake = Faker('es_MX')
fake.add_provider(internet)
for _ in range(1):
    # print(fake.name())
    # # print(fake.state_abbr())
    # print(fake.postcode())
    # print(fake.street_address())
    # print(fake.rfc())
    # print(fake.job())
    start_time = time.time()  # Record the start time


# Cantidad de Filas añadir/crear
num_rows = 100

# Nombre del archivo CSV
csv_filename = 'res_partner_odoo.csv'

# Encabezados del CSV (puedes personalizarlos según tus necesidades)
csv_headers = ['name', 'state_id/.id', 'zip', 'street', 'vat', 'funtion', 'country_id/.id', 'bank_ids/bank_id/.id', 'bank_ids/acc_number', 'bank_ids/l10n_mx_edi_clabe']

# Abre el archivo CSV en modo escritura
with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
    # Crea un objeto escritor CSV
    csv_writer = csv.writer(csvfile)

    # Escribe los encabezados en la primera fila del CSV
    csv_writer.writerow(csv_headers)

    # Genera y escribe las filas de datos falsos en el CSV
    for _ in range(num_rows):
        # Genera datos falsos con Faker
        name = fake.name()
        state_id = random.randint(485, 516)
        postcode = fake.postcode()
        street = fake.street_address()
        vat = fake.rfc()
        funtion = fake.job()
        country_id = random.randint(156, 156)
        bank_id = random.randint(1, 93)
        bank_account = fake.aba()
        bank_clabe = fake.clabe()

        # Escribe los datos en una fila del CSV
        csv_writer.writerow([name, state_id, postcode, street, vat, funtion, country_id, bank_id, bank_account, bank_clabe])
        end_time = time.time()  # Registrar el tiempo de finalización
        elapsed_time = end_time - start_time  # Calcular el tiempo transcurrido

        # Formatear el tiempo en minutos y segundos
        minutes = int(elapsed_time // 60)
        seconds = int(elapsed_time % 60)

print(f'Tiempo total transcurrido: {minutes} minutos {seconds} segundos')
print(f'Se ha creado el archivo CSV: {csv_filename} con {num_rows} lineas')
