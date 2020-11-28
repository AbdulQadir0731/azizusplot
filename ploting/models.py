from django.db import models
from django.contrib import admin
from django.utils.html import mark_safe
from sorl.thumbnail import get_thumbnail
from django.utils.html import format_html
# Create your models here.


class Plot(models.Model):
    name = models.CharField(max_length=30)

    
       
    INITIAL_FEEDBACK = (
        ('INTERESTED', 'interested'),
        ('NOT INTERESTED', 'not interested'),
    )
    initial_feedback = models.CharField(max_length=60, choices=INITIAL_FEEDBACK)
    initial_contact_1 =  models.CharField(max_length=256 , blank=True)
    initial_contact_2 =  models.CharField(max_length=256 , blank=True)
    initial_contact_3 =  models.CharField(max_length=256 , blank=True)
    
    
    


    

    

    initial_information = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def initial_information_preview(self):
        if self.initial_information:
            _initial_information = get_thumbnail(self.initial_information,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_initial_information.url, _initial_information.width, _initial_information.height))
        return "" 


    initial_information1 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def initial_information1_preview(self):
        if self.initial_information1:
            _initial_information1 = get_thumbnail(self.initial_information1,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_initial_information1.url, _initial_information1.width, _initial_information1.height))
        return ""     

    

    agreement = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def agreement_preview(self):
        if self.agreement:
            _agreement = get_thumbnail(self.agreement,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_agreement.url, _agreement.width, _agreement.height))
        return "" 

    agreement1 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def agreement1_preview(self):
        if self.agreement1:
            _agreement1 = get_thumbnail(self.agreement1,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_agreement1.url, _agreement1.width, _agreement1.height))
        return ""    


    agreement2 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def agreement2_preview(self):
        if self.agreement2:
            _agreement2 = get_thumbnail(self.agreement2,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_agreement2.url, _agreement2.width, _agreement2.height))
        return ""    


    agreement3 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def agreement3_preview(self):
        if self.agreement3:
            _agreement3 = get_thumbnail(self.agreement3,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_agreement3.url, _agreement3.width, _agreement3.height))
        return ""

    agreement4 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def agreement4_preview(self):
        if self.agreement4:
            _agreement4 = get_thumbnail(self.agreement4,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_agreement4.url, _agreement4.width, _agreement4.height))
        return ""     
    
    
  

    first_payment_cheque = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def first_payment_cheque_preview(self):
        if self.first_payment_cheque:
            _first_payment_cheque = get_thumbnail(self.first_payment_cheque,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_first_payment_cheque.url, _first_payment_cheque.width, _first_payment_cheque.height))
        return "" 

    second_payment_cheque = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def second_payment_cheque_preview(self):
        if self.second_payment_cheque:
            _second_payment_cheque = get_thumbnail(self.second_payment_cheque,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_second_payment_cheque.url, _second_payment_cheque.width, _second_payment_cheque.height))
        return ""     

    third_payment_cheque = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def third_payment_cheque_preview(self):
        if self.third_payment_cheque:
            _third_payment_cheque = get_thumbnail(self.third_payment_cheque,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_third_payment_cheque.url, _third_payment_cheque.width, _third_payment_cheque.height))
        return ""


    mutuation_text = models.TextField(null=True, blank=True)


    mutuation = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation_preview(self):
        if self.mutuation:
            _mutuation = get_thumbnail(self.mutuation,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation.url, _mutuation.width, _mutuation.height))
        return ""

    mutuation1 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation1_preview(self):
        if self.mutuation1:
            _mutuation1 = get_thumbnail(self.mutuation1,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation1.url, _mutuation1.width, _mutuation1.height))
        return ""    



    mutuation2 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation2_preview(self):
        if self.mutuation2:
            _mutuation2 = get_thumbnail(self.mutuation2,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation2.url, _mutuation2.width, _mutuation2.height))
        return ""   


    mutuation3 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation3_preview(self):
        if self.mutuation3:
            _mutuation3 = get_thumbnail(self.mutuation3,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation3.url, _mutuation3.width, _mutuation3.height))
        return ""       
    

    mutuation4 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation4_preview(self):
        if self.mutuation4:
            _mutuation4 = get_thumbnail(self.mutuation4,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation4.url, _mutuation4.width, _mutuation4.height))
        return "" 


    mutuation5 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mutuation5_preview(self):
        if self.mutuation5:
            _mutuation5 = get_thumbnail(self.mutuation5,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mutuation5.url, _mutuation5.width, _mutuation5.height))
        return ""  


    
    mul_dolil_text = models.TextField(null=True, blank=True)


    mul_dolil = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil_preview(self):
        if self.mul_dolil:
            _mul_dolil = get_thumbnail(self.mul_dolil,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil.url, _mul_dolil.width, _mul_dolil.height))
        return ""        


    
    mul_dolil1 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil1preview(self):
        if self.mul_dolil1:
            _mul_dolil1 = get_thumbnail(self.mul_dolil1,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil1.url, _mul_dolil1.width, _mul_dolil1.height))
        return ""

    mul_dolil2 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil2preview(self):
        if self.mul_dolil2:
            _mul_dolil2 = get_thumbnail(self.mul_dolil2,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil2.url, _mul_dolil2.width, _mul_dolil2.height))
        return ""


    mul_dolil3 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil3preview(self):
        if self.mul_dolil3:
            _mul_dolil3 = get_thumbnail(self.mul_dolil3,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil3.url, _mul_dolil3.width, _mul_dolil3.height))
        return ""

    mul_dolil4 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil4preview(self):
        if self.mul_dolil4:
            _mul_dolil4 = get_thumbnail(self.mul_dolil4,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil4.url, _mul_dolil4.width, _mul_dolil4.height))
        return ""


    mul_dolil5 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil5preview(self):
        if self.mul_dolil5:
            _mul_dolil5 = get_thumbnail(self.mul_dolil5,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil5.url, _mul_dolil5.width, _mul_dolil5.height))
        return ""

    mul_dolil6 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil6preview(self):
        if self.mul_dolil6:
            _mul_dolil6 = get_thumbnail(self.mul_dolil6,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil6.url, _mul_dolil6.width, _mul_dolil6.height))
        return ""

    mul_dolil7 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil7preview(self):
        if self.mul_dolil7:
            _mul_dolil7 = get_thumbnail(self.mul_dolil7,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil7.url, _mul_dolil7.width, _mul_dolil7.height))
        return "" 


    mul_dolil8 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil8preview(self):
        if self.mul_dolil8:
            _mul_dolil8 = get_thumbnail(self.mul_dolil8,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil8.url, _mul_dolil8.width, _mul_dolil8.height))
        return ""                      


    mul_dolil9 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil9preview(self):
        if self.mul_dolil9:
            _mul_dolil9 = get_thumbnail(self.mul_dolil9,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil9.url, _mul_dolil9.width, _mul_dolil9.height))
        return "" 

    mul_dolil10 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil10preview(self):
        if self.mul_dolil10:
            _mul_dolil10 = get_thumbnail(self.mul_dolil10,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil10.url, _mul_dolil10.width, _mul_dolil10.height))
        return ""


    mul_dolil11 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil11preview(self):
        if self.mul_dolil11:
            _mul_dolil11 = get_thumbnail(self.mul_dolil11,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil11.url, _mul_dolil11.width, _mul_dolil11.height))
        return ""    

    mul_dolil12 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil12preview(self):
        if self.mul_dolil12:
            _mul_dolil12 = get_thumbnail(self.mul_dolil12,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil12.url, _mul_dolil12.width, _mul_dolil12.height))
        return ""

    mul_dolil13 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil13preview(self):
        if self.mul_dolil13:
            _mul_dolil13 = get_thumbnail(self.mul_dolil13,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil13.url, _mul_dolil13.width, _mul_dolil13.height))
        return ""   

    mul_dolil14 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil14preview(self):
        if self.mul_dolil14:
            _mul_dolil14 = get_thumbnail(self.mul_dolil14,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil14.url, _mul_dolil14.width, _mul_dolil14.height))
        return ""    

    mul_dolil15 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil15preview(self):
        if self.mul_dolil15:
            _mul_dolil15 = get_thumbnail(self.mul_dolil15,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil15.url, _mul_dolil15.width, _mul_dolil15.height))
        return ""


    mul_dolil16 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil16preview(self):
        if self.mul_dolil16:
            _mul_dolil16 = get_thumbnail(self.mul_dolil16,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil16.url, _mul_dolil16.width, _mul_dolil16.height))
        return ""

    mul_dolil17 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil17preview(self):
        if self.mul_dolil17:
            _mul_dolil17 = get_thumbnail(self.mul_dolil17,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil17.url, _mul_dolil17.width, _mul_dolil17.height))
        return ""            


    mul_dolil18 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil18preview(self):
        if self.mul_dolil18:
            _mul_dolil18 = get_thumbnail(self.mul_dolil18,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil18.url, _mul_dolil18.width, _mul_dolil18.height))
        return ""    


    mul_dolil19 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil19preview(self):
        if self.mul_dolil19:
            _mul_dolil19 = get_thumbnail(self.mul_dolil19,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil19.url, _mul_dolil19.width, _mul_dolil19.height))
        return ""    

    mul_dolil20 = models.ImageField(upload_to='post/thumbnail/%Y/%m/%d/', null=True, blank=True)
    
    @property
    def mul_dolil20preview(self):
        if self.mul_dolil20:
            _mul_dolil20 = get_thumbnail(self.mul_dolil20,
                                   '300x300',
                                   upscale=False,
                                   crop=False,
                                   quality=100)
            return format_html('<img src="{}" width="{}" height="{}">'.format(_mul_dolil20.url, _mul_dolil20.width, _mul_dolil20.height))
        return ""    