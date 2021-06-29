from datetime import datetime

from django.contrib import admin
from django.db import models
from django.utils import timezone
# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Mietobjekt(models.Model):
    name = description = models.CharField(verbose_name="Objektname",max_length=200, default=0)
    # mietzins = models.ManyToManyField(Mietzinse)
    #description = models.CharField(verbose_name="Beschreibung",max_length=1000)
    description = models.TextField(verbose_name="Beschreibung", max_length=1024 * 2)
    # rent = models.DecimalField(max_digits=6, decimal_places=2)
    photo = models.ImageField(verbose_name="Bild", default=0)

    def __str__(self):
        return self.description


class Mietzins(models.Model):
    #mietobjekt = models.ForeignKey(Mietobjekt, on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Beschreibung",max_length=200)
    rent = models.DecimalField(verbose_name="Miete",max_digits=6, decimal_places=2)
    # mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE, default=0)
    mietobject = models.ForeignKey(Mietobjekt, on_delete=models.CASCADE, default=0)
    aktiv = models.BooleanField(default=False)
    def __str__(self):
        return str(self.rent)


class Year(models.Model):
    typ = models.IntegerField(default=2010)

    def __str__(self):
        return str(self.typ)

class Nebenkosten_Typ(models.Model):
    # set headline
    typ = models.CharField(max_length=200)
    # a_conto = models.BooleanField(default=False)
    a_conto =  models.CharField(max_length=10, choices=(('a', 'à conto',),
                                         ('p', 'pauschal')))

    def __str__(self):
        return self.typ + " "+ str(self.a_conto)

class Nebenkosten(models.Model):
    # mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    typ = models.ForeignKey(Nebenkosten_Typ, on_delete=models.CASCADE)
    betrag = models.DecimalField(max_digits=6, decimal_places=2)
    aktiv = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.betrag)+' '+str(self.aktiv)

class Mieter(models.Model):
    company = models.CharField(verbose_name="Firma", max_length=200,blank = True)
    first_name = models.CharField(verbose_name="Vorname",max_length=200)
    last_name = models.CharField(verbose_name="Nachname", max_length=200)
    phone_number = models.CharField(verbose_name="Telefonnummer", max_length=200)
    conto_number = models.CharField(verbose_name="IBAN Nummer", max_length=200, default=0)
    address = models.CharField(verbose_name="Strasse", max_length=200, default=0)
    address_Nr = models.IntegerField(verbose_name="Strassennummer", default=0)
    city = models.CharField(verbose_name="Wohnort", max_length=200, default=0)
    city_code = models.IntegerField(verbose_name="PLZ", default=0)
    first_name_2nd = models.CharField(verbose_name="Zweitmieter Vorname", max_length=200,blank = True)
    last_name_2nd = models.CharField(verbose_name="Zweitmieter Nachname", max_length=200, blank = True)
    activ = models.BooleanField(verbose_name="aktiv", default=False)
    mietzins = models.ManyToManyField(Mietzins)
    nebenkosten = models.ManyToManyField(Nebenkosten)

    def __str__(self):
        """
            used for ForeignKey dropDown
        :return:
        """
        m_zins = ", ".join(str(m) for m in self.mietzins.all())
        return ('{} {} {} {} ').format(
                                                    self.company,
                                                    self.first_name,
                                                    self.last_name,
                                                    m_zins)





class Kosten(models.Model):
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    miete = models.ForeignKey(Mietobjekt, on_delete=models.CASCADE)
    nebenkosten = models.ForeignKey(Nebenkosten, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mieter)+' '+str(self.miete)+' '+str(self.nebenkosten)



class Mietzinseingaenge(models.Model):
    datum = models.DateField(default=datetime.now())
    # ,input_formats=["%Y-%m-%d", ]
    month = models.CharField(max_length=10, choices=(('JA', 'Januar',),
                                         ('FE', 'Februar'),
                                         ('MA', 'März'),
                                         ('AP', 'April'),
                                         ('MA', 'Mai'),
                                         ('JN', 'Juni'),
                                         ('JU', 'Juli'),
                                         ('AU', 'August'),
                                         ('SE', 'September'),
                                         ('OK', 'Oktober'),
                                         ('NO', 'November'),
                                         ('DE', 'Dezember'),))
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    betrag = models.IntegerField(default=0)
    year  = models.ForeignKey(Year, on_delete=models.CASCADE, default=2010)


    def __str__(self):
        return str(self.mieter)+' '+str(self.betrag)+' '+str(self.datum)
