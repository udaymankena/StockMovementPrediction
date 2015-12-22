from django import forms

class StockForm(forms.Form):
     company_list = (
                    ('Apple Inc','Apple Inc'),
                    ('Cisco Systems Inc','Cisco Systems Inc'),
                    ('Microsoft Corporation','Microsoft Corporation'),
                    ('Honeywell International Inc','Honeywell International Inc'),
                    ('Harris Corporation','Harris Corporation'),
                    ('Cummins','Cummins'),
                    ('Applied Materials','Applied Materials'),
                    ('Marriott International','Marriott International'),
                    ('Expedia','Expedia'),
                    ('Red Hat','Red Hat'),
                    ('Robert Half International Inc','Robert Half International Inc'),
                    ('QUALCOMM','QUALCOMM'),
                    ('Oracle Corporation','Oracle Corporation'),
                    ('Phillips','Phillips'),
                    ('NetApp Inc','NetApp Inc'),
                    ('Skyworks Solutions','Skyworks Solutions'),
                    ('Goldman Sachs Group','Goldman Sachs Group'),
                    ('Google Inc','Google Inc'),
                    ('General Motors Company','General Motors Company'),
                    ('Marvell Technology Group Ltd','Marvell Technology Group Ltd'),
                    ('Nokia Corporation','Nokia Corporation'),
                    ('Akamai Technologies','Akamai Technologies'),
                    ('Teradata','Teradata')
                    )
     stock_name = forms.ChoiceField(choices= company_list)