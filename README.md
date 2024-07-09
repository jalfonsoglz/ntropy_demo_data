# Demo Data Generator [by [Ntropy](https://ntropy.tech/odoo/)]

[Based](https://www.odoo.com/documentation/17.0/applications/finance/fiscal_localizations/mexico.html#introduction)

## 1. Pre-requisites

[//]: # (1. This module needs the Python library Faker, otherwise it create demo data be installed and used. Install Faker through the command: <code>sudo pip install Faker</code>)

1. Install `account` and set México as Company Country.
2. Install `ntropy_demo_data_generator` module.

## 2. Introduction

This module installs base odoo apps for a demonstration

* **Sales**
    * `sale_management`
    * `contacts`

* **Accounting**
    * `account`
    * `account_accountant`
* **Inventory**
    * `stock`
    * `purchase`
    * `stock_barcode`

Another modules for create more data sample as:

* **México EDI Modules:**
    * `l10n_mx`
    * `l10n_mx_edi`
    * `l10n_mx_edi_sale`
    * `l10n_mx_edi_landing`
    * `l10n_mx_reports`
    * `l10n_mx_reports_closing`
    * `l10n_mx_xml_polizas`

Incoming:

* **Customizations**
    * `web_studio`
* **Sales**
    * `crm`
    * `point_of_sale`
* **Services**
    * `project`
    * `timesheet_grid`
    * `helpdesk`
* **Human Resources**
    * `hr`
    * `hr_payroll`
* **Resources**
    * `res.currency.rate` https://www.banxico.org.mx/tipcamb/main.do?page=tip&idioma=sp

## 3. Configuration

## 4. Data Sample

* Create Contacts with RFC to Test EDI Documents with category 'Testing'

### Validez Obligaciones

1. Habilitado para facturar (IVA exento, tasa 0% y 16%)
2. Habilitado para facturar (IVA exento, tasa 0%, 8% y 16%) Zona Fronteriza Norte
3. Habilitado para facturar (IVA exento, tasa 0%, 8% y 16%) Zona Fronteriza Sur
4. Habilitado para facturar (IVA exento, tasa 0%, 8% y 16%) Zona Fronteriza Norte y Sur

| RFC           | Nombre/Razón Social                           | CP    | Regimen                                                              | Retención | Tipo   | Notas                        |
|---------------|-----------------------------------------------|-------|----------------------------------------------------------------------|-----------|--------|------------------------------|
| MASO451221PM4 | MARIA OLIVIA MARTINEZ SAGAZ                   | 80290 | 616 - Sin obligaciones fiscales                                      | 1         | Física | Cliente                      |
| AABF800614HI0 | FELIX MANUEL ANDRADE BALLADO                  | 86400 | 612 - Personas físicas con actividades empresariales y profesionales | 1         | Física | Cliente                      |
| CUSC850516316 | CESAR OSBALDO CRUZ SOLORZANO                  | 45638 | 605 - Sueldos y Salarios e Ingresos Asimilados a Salarios            | 1         | Física | Cliente                      |
| CACX7605101P8 | XOCHILT CASAS CHAVEZ                          | 36257 | 621 - Incorporación fiscal                                           | 2         | Física | Cliente                      |
| FUNK671228PH6 | KARLA FUENTE NOLASCO                          | 01160 | 621 - Incorporación fiscal                                           | 1         | Física | Cliente                      |
| IAÑL750210963 | LUIS IAN ÑUZCO                                | 85256 | 608 - Demás ingresos                                                 | 1         | Física | Cliente                      |
| JUFA7608212V6 | ADRIANA JUAREZ FERNANDEZ                      | 01160 | 614 - Ingresos por intereses                                         | 1         | Física | Cliente                      |
| MISC491214B86 | CECILIA MIRANDA SANCHEZ                       | 01010 | 612 - Personas físicas con actividades empresariales y profesionales | 2         | Física | Cliente                      |
| RAQÑ7701212M3 | ÑEVES RAMIREZ QUEZADA                         | 78905 | 605 - Sueldos y Salarios e Ingresos Asimilados a Salarios            | 1         | Física | Cliente                      |
| WATM640917J45 | MARIA WATEMBER TORRES                         | 43543 | 622 - Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras       | 1         | Física | Cliente                      |
| WERX631016S30 | XAIME WEIR ROJO                               | 01279 | 608 - Demás ingresos                                                 | 1         | Física | Cliente                      |
| XAMA620210DQ5 | ALBA XKARAJAM MENDEZ                          | 01219 | 612 - Personas físicas con actividades empresariales y profesionales | 1         | Física | Cliente                      |
| XOJI740919U48 | INGRID XODAR JIMENEZ                          | 76028 | 612 - Personas físicas con actividades empresariales y profesionales | 1         | Física | Cliente                      |
| KICR630120NX3 | RODRIGO KITIA CASTRO                          | 36246 | 622 - Actividades Agrícolas, Ganaderas, Silvícolas y Pesqueras       | 1         | Física | Cliente                      |
| ABC970528UHA  | ARENA BLANCA                                  | 80290 | 626 - Régimen Simplificado de Confianza - RESICO                     | 1         | Moral  | Cliente                      |
| CTE950627K46  | COMERCIALIZADORA TEODORIKAS                   | 57740 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Cliente                      |
| AMO8905171T1  | ALBERCAS MONTAÑO                              | 22000 | 626 - Régimen Simplificado de Confianza - RESICO                     | 1         | Moral  | Cliente                      |
| GCA000415UX7  | GRUPO DE CONSTRUCCION ARQUITECTONICA NACIONAL | 11830 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Cliente                      |
| HHN0507087N4  | HIDRO HORTICOLA DEL NOROESTE                  | 82198 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Cliente                      |
| XIA190128J61  | XENON INDUSTRIAL ARTICLES                     | 76343 | 624 - Coordinados                                                    | 1         | Moral  | Cliente                      |
| KIJ0906199R1  | KERNEL INDUSTIA JUGUETERA                     | 62661 | 603 - Personas morales con fines no lucrativos                       | 1         | Moral  | Cliente                      |
| XEXX010101000 | Umbrella Corporation                          | 33156 | 616 - Sin obligaciones fiscales                                      | 1         | Moral  | Cliente/Proveedor Extranjero |
| XIQB891116QE4 | BERENICE XIMO QUEZADA                         | 40968 | 606 - Arrendamiento                                                  | 4         | Física | Proveedor                    |
| ICV060329BY0  | INMOBILIARIA CVA                              | 33826 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| IIA040805DZ4  | INDISTRIA ILUMINADORA DE ALMACENES            | 62661 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| H&E951128469  | HERRERIA & ELECTRICOS                         | 06002 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| IVD920810GU2  | INNOVACION VALOR Y DESARROLLO                 | 63901 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| IXS7607092R5  | INTERNACIONAL XIMBO Y SABORES                 | 23004 | 603 - Personas morales con fines no lucrativos                       | 1         | Moral  | Proveedor                    |
| JES900109Q90  | JIMENEZ ESTRADA SALAS                         | 37161 | 616 - Sin obligaciones fiscales                                      | 1         | Moral  | Proveedor                    |
| L&O950913MSA  | LUCES & OBRAS                                 | 60922 | 603 - Personas morales con fines no lucrativos                       | 1         | Moral  | Proveedor                    |
| OÑO120726RX3  | ORGANICOS ÑAVEZ OSORIO                        | 40501 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| S&S051221SE2  | S & SOFTWARE                                  | 76022 | 624 - Coordinados                                                    | 1         | Moral  | Proveedor                    |
| ZUÑ920208KL4  | ZAPATERIA URTADO ÑERI                         | 34541 | 601 - General de Ley de Personas Morales                             | 1         | Moral  | Proveedor                    |
| URE180429TM6  | UNIVERSIDAD ROBOTICA ESPAÑOLA                 | 86991 | 603 - Personas morales con fines no lucrativos                       | 1         | Moral  | Proveedor                    |

## 5. Workflows

1. Customer Invoice
    * Normal Invoice
    * Down Payment Invoice
    * Credit Note
    * CFDI to Public
2. Payment Complements
3. Invoice cancellations
    * Invoices sent with errors with a relation (Type 1)
    * Invoices sent with errors without a relation (Type 2)
4. External Trade
5. Delivery Guide

## 6. Changelog

## 7. To do


