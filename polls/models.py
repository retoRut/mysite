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


class Mieter(models.Model):
    company = models.CharField(verbose_name="Firma", max_length=200,blank = True)
    first_name = models.CharField(verbose_name="Vorname",max_length=200)
    last_name = models.CharField(verbose_name="Nachname", max_length=200)
    phone_number = models.CharField(verbose_name="Telefonnummer", max_length=200)
    conto_number = models.CharField(verbose_name="IBAN Nummer", max_length=200, default=0)
    address = models.CharField(verbose_name="Strasse", max_length=200, default=0)
    address_Nr = models.CharField(verbose_name="Strassennummer",max_length=200, default=0)
    city = models.CharField(verbose_name="Wohnort", max_length=200, default=0)
    city_code = models.IntegerField(verbose_name="PLZ", default=0)
    first_name_2nd = models.CharField(verbose_name="Zweitmieter Vorname", max_length=200,blank = True)
    last_name_2nd = models.CharField(verbose_name="Zweitmieter Nachname", max_length=200, blank = True)
    activ = models.BooleanField(verbose_name="aktiv", default=False)

    def __str__(self):
        """
            used for headlines
        :return:
        """
        return ('{} {} {} {} {} {} {} {} {}').format(
                                                    self.company,
                                                    self.first_name,
                                                    self.last_name,
                                                    self.first_name_2nd,
                                                    self.first_name_2nd,
                                                    self.phone_number,
                                                    self.address,
                                                    self.address_Nr,
                                                    self.city,
                                                    self.city_code)

class Mietzinse(models.Model):
    #mietobjekt = models.ForeignKey(Mietobjekt, on_delete=models.CASCADE)
    description = models.CharField(verbose_name="Beschreibung",max_length=200)
    rent = models.IntegerField(default=0)

    def __str__(self):
        return self.description

class Mietobjekt(models.Model):
    name = description = models.CharField(verbose_name="Objektname",max_length=200, default=0)
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    mietzins = models.ForeignKey(Mietzinse, on_delete=models.CASCADE, default=0)
    # mietzins = models.ManyToManyField(Mietzinse)
    description = models.CharField(verbose_name="Beschreibung",max_length=200)
    rent = models.IntegerField(default=0)
    a_conto = models.IntegerField(default=0)

    def __str__(self):
        return self.description



class ZahlungsTyp(models.Model):
    typ = models.CharField(max_length=50, default = '1' )

    def __str__(self):
        return str(self.typ)

class Nebenkosten_Typ(models.Model):
    # set headline
    typ = models.CharField(max_length=200)
    # a_conto = models.BooleanField(default=False)
    a_conto = models.ForeignKey(ZahlungsTyp, on_delete=models.CASCADE)

    def __str__(self):
        return self.typ + " "+ str(self.a_conto)


class Nebenkosten(models.Model):
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    typ = models.ForeignKey(Nebenkosten_Typ, on_delete=models.CASCADE)
    betrag = models.DecimalField(max_digits=6, decimal_places=2)
    aktiv = models.BooleanField(default=False)
    start_date = models.DateField(default=datetime.now())
    end_date = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.betrag)+' '+str(self.aktiv)


class Kosten(models.Model):
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    miete = models.ForeignKey(Mietobjekt, on_delete=models.CASCADE)
    nebenkosten = models.ForeignKey(Nebenkosten, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.mieter)+' '+str(self.miete)+' '+str(self.nebenkosten)


class Month(models.Model):
    month = models.CharField(max_length=50)

    def __str__(self):
        return str(self.month)


class Year(models.Model):
    year = models.CharField(max_length=50)

    def __str__(self):
        return str(self.year)



class Mietzinseingaenge(models.Model):
    datum = models.DateField(default=datetime.now())
    # ,input_formats=["%Y-%m-%d", ]
    month = models.ForeignKey(Month, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    mieter = models.ForeignKey(Mieter, on_delete=models.CASCADE)
    betrag = models.IntegerField(default=0)


    def __str__(self):
        return str(self.mieter)+' '+str(self.betrag)+' '+str(self.datum)
