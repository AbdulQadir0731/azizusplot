from django.contrib import admin
from .models import Plot
from import_export import resources
from import_export.admin import ImportExportModelAdmin


class PlotResource(resources.ModelResource):
    
    class Meta:
        model = Plot

class PlotAdmin(ImportExportModelAdmin):
    resource_class = PlotResource
    list_display = ('name' , 'status')
    search_fields = ('name' , )
    list_filter = ('status' ,)
    fields = ('name' ,
    'initial_feedback' ,
    'seller_photo' ,
    'seller_photo_preview' ,
    'id_or_passport_page_1',
    'id_or_passport_page_1_preview',
    'id_or_passport_page_2',
    'id_or_passport_page_2_preview',
    'id_or_passport_page_3',
    'id_or_passport_page_3_preview',
    'relative_id_or_passport_page_1',
    'relative_id_or_passport_page_1_preview',
    'relative_id_or_passport_page_2',
    'relative_id_or_passport_page_2_preview',
   
   

    'status' ,
    'initial_contact_1' , 
    'initial_contact_2' ,
    'initial_contact_3' ,
    'initial_information' , 
    'initial_information_preview' ,
    'initial_information1' , 
    'initial_information1_preview' ,
    'initial_information_text' ,
    'agreement' ,
    'agreement_preview' ,
    'agreement1' ,
    'agreement1_preview' ,
    'agreement2' ,
    'agreement2_preview' ,
    'agreement3' ,
    'agreement3_preview' ,
    'agreement4' ,
    'agreement4_preview' ,
    'first_payment_cheque' ,
    'first_payment_cheque_preview' ,
    'first_payment_cheque_text' ,
    'second_payment_cheque' ,
    'second_payment_cheque_preview' ,
    'second_payment_cheque_text' ,
    'third_payment_cheque' ,
    'third_payment_cheque_preview' ,
    'third_payment_cheque_text' , 
    'mutuation_text' ,
    'mutuation' ,
    'mutuation_preview' ,
    'mutuation1',
    'mutuation1_preview' ,
    'mutuation2',
    'mutuation2_preview' ,
    'mutuation3',
    'mutuation3_preview' ,
    'mutuation4',
    'mutuation4_preview' ,
    'mutuation5',
    'mutuation5_preview' ,
    'mul_dolil_text' ,
    'mul_dolil' ,
    'mul_dolil_preview' ,
    'mul_dolil1' ,
    'mul_dolil1preview' ,
    'mul_dolil2' ,
    'mul_dolil2preview' ,
    'mul_dolil3' ,
    'mul_dolil3preview' ,
    'mul_dolil4' ,
    'mul_dolil4preview' ,
    'mul_dolil5' ,
    'mul_dolil5preview' ,
    'mul_dolil6' ,
    'mul_dolil6preview' ,
    'mul_dolil7' ,
    'mul_dolil7preview' ,
    'mul_dolil8' ,
    'mul_dolil8preview' ,
    'mul_dolil9' ,
    'mul_dolil9preview' ,
    'mul_dolil10' ,
    'mul_dolil10preview' ,
    'mul_dolil11' ,
    'mul_dolil11preview' ,
    'mul_dolil12' ,
    'mul_dolil12preview' ,
    'mul_dolil13' ,
    'mul_dolil13preview' ,
    'mul_dolil14' ,
    'mul_dolil14preview' ,
    'mul_dolil15' ,
    'mul_dolil15preview' ,
    'mul_dolil16' ,
    'mul_dolil16preview' ,
    'mul_dolil17' ,
    'mul_dolil17preview' ,
    'mul_dolil18' ,
    'mul_dolil18preview' ,
    'mul_dolil19' ,
    'mul_dolil19preview' ,
    'mul_dolil20' ,
    'mul_dolil20preview' ,
  
    )







    readonly_fields = ('seller_photo_preview' ,

    'id_or_passport_page_1_preview',

    'id_or_passport_page_2_preview',

    'id_or_passport_page_3_preview',
  
    'relative_id_or_passport_page_1_preview',
    
    'relative_id_or_passport_page_2_preview',
        'initial_information_preview' , 'initial_information1_preview' , 'agreement_preview' , 'agreement1_preview' , 'agreement2_preview' , 'agreement3_preview' , 'agreement4_preview' ,

        'first_payment_cheque_preview' ,
        'second_payment_cheque_preview' ,
        'third_payment_cheque_preview' ,


        'mutuation_preview' ,
        'mutuation1_preview' ,
        'mutuation2_preview' ,
        'mutuation3_preview' ,  
        'mutuation4_preview' ,
        'mutuation5_preview' ,


        'mul_dolil_preview' ,
        'mul_dolil1preview' ,
        'mul_dolil2preview' ,
        'mul_dolil3preview' ,
        'mul_dolil4preview' ,
        'mul_dolil5preview' ,
        'mul_dolil6preview' ,
        'mul_dolil7preview' ,
        'mul_dolil8preview' ,
        'mul_dolil9preview' ,
        'mul_dolil10preview' ,
        'mul_dolil11preview' ,
        'mul_dolil12preview' ,
        'mul_dolil13preview' ,
        'mul_dolil14preview' ,
        'mul_dolil15preview' ,
        'mul_dolil16preview' ,
        'mul_dolil17preview' ,
        'mul_dolil18preview' ,
        'mul_dolil19preview' ,
        'mul_dolil20preview' ,



    ) 

    
    def seller_photo_preview(self, obj):
        return obj.seller_photo_preview

    def id_or_passport_page_1_preview(self, obj):
        return obj.id_or_passport_page_1_preview

    def id_or_passport_page_2_preview(self, obj):
        return obj.id_or_passport_page_2_preview

    def id_or_passport_page_3_preview(self, obj):
        return obj.id_or_passport_page_3_preview 

    def relative_id_or_passport_page_1_preview(self, obj):
        return obj.relative_id_or_passport_page_1_preview

    def relative_id_or_passport_page_2_preview(self, obj):
        return obj.relative_id_or_passport_page_2_preview

          


    def initial_information_preview(self, obj):
        return obj.initial_information_preview


    def initial_information1_preview(self, obj):
        return obj.initial_information1_preview 

    def agreement_preview(self, obj):
        return obj.agreement_preview  


    def agreement1_preview(self, obj):
        return obj.agreement1_preview  

    def agreement2_preview(self, obj):
        return obj.agreement2_preview  

    def agreement3_preview(self, obj):
        return obj.agreement3_preview 


    def agreement4_preview(self, obj):
        return obj.agreement4_preview 


    def first_payment_cheque_preview(self, obj):
        return obj.first_payment_cheque_preview


    def second_payment_cheque_preview(self, obj):
        return obj.second_payment_cheque_preview  

    def third_payment_cheque_preview(self, obj):
        return obj.third_payment_cheque_preview 

    def mutuation_preview(self, obj):
        return obj.mutuation_preview 

    def mutuation1_preview(self, obj):
        return obj.mutuation1_preview  

    def mutuation2_preview(self, obj):
        return obj.mutuation2_preview 

    def mutuation3_preview(self, obj):
        return obj.mutuation3_preview 

    def mutuation4_preview(self, obj):
        return obj.mutuation4_preview

    def mutuation5_preview(self, obj):
        return obj.mutuation5_preview 

    def mul_dolil_preview(self, obj):
        return obj.mul_dolil_preview 

    def mul_dolil1preview(self, obj):
        return obj.mul_dolil1preview

    def mul_dolil2preview(self, obj):
        return obj.mul_dolil2preview

    def mul_dolil3preview(self, obj):
        return obj.mul_dolil3preview 

    def mul_dolil4preview(self, obj):
        return obj.mul_dolil4preview 

    def mul_dolil5preview(self, obj):
        return obj.mul_dolil5preview 

    def mul_dolil6preview(self, obj):
        return obj.mul_dolil6preview 

    def mul_dolil7preview(self, obj):
        return obj.mul_dolil7preview 

    def mul_dolil8preview(self, obj):
        return obj.mul_dolil8preview 


    def mul_dolil9preview(self, obj):
        return obj.mul_dolil9preview 

    def mul_dolil10preview(self, obj):
        return obj.mul_dolil10preview 

    def mul_dolil11preview(self, obj):
        return obj.mul_dolil11preview 

    def mul_dolil12preview(self, obj):
        return obj.mul_dolil12preview 

    def mul_dolil13preview(self, obj):
        return obj.mul_dolil13preview 

    def mul_dolil14preview(self, obj):
        return obj.mul_dolil14preview 

    def mul_dolil15preview(self, obj):
        return obj.mul_dolil15preview   

    def mul_dolil16preview(self, obj):
        return obj.mul_dolil16preview  

    def mul_dolil17preview(self, obj):
        return obj.mul_dolil17preview    

    def mul_dolil18preview(self, obj):
        return obj.mul_dolil18preview 

    def mul_dolil19preview(self, obj):
        return obj.mul_dolil19preview 

    def mul_dolil20preview(self, obj):
        return obj.mul_dolil20preview                                              


    seller_photo_preview.short_description = 'seller_photo_preview Preview'
    seller_photo_preview.allow_tags = True

    
    id_or_passport_page_1_preview.short_description = 'id_or_passport_page_1_preview Preview'
    id_or_passport_page_1_preview.allow_tags = True

    id_or_passport_page_2_preview.short_description = 'id_or_passport_page_2_preview Preview'
    id_or_passport_page_2_preview.allow_tags = True

    id_or_passport_page_3_preview.short_description = 'id_or_passport_page_3_preview Preview'
    id_or_passport_page_3_preview.allow_tags = True

    

    relative_id_or_passport_page_1_preview.short_description = 'relative_id_or_passport_page_1_preview Preview'
    relative_id_or_passport_page_1_preview.allow_tags = True

    relative_id_or_passport_page_2_preview.short_description = 'relative_id_or_passport_page_2_preview Preview'
    relative_id_or_passport_page_2_preview.allow_tags = True

  



    initial_information_preview.short_description = 'initial_information_preview Preview'
    initial_information_preview.allow_tags = True

    initial_information1_preview.short_description = 'initial_information1_preview Preview'
    initial_information1_preview.allow_tags = True

    agreement_preview.short_description = 'agreement_preview Preview'
    agreement_preview.allow_tags = True


    agreement1_preview.short_description = 'agreement1_preview Preview'
    agreement1_preview.allow_tags = True

    agreement2_preview.short_description = 'agreement2_preview Preview'
    agreement2_preview.allow_tags = True

    agreement3_preview.short_description = 'agreement3_preview Preview'
    agreement3_preview.allow_tags = True

    agreement4_preview.short_description = 'agreement4_preview Preview'
    agreement4_preview.allow_tags = True

    first_payment_cheque_preview.short_description = 'first_payment_cheque_preview Preview'
    first_payment_cheque_preview.allow_tags = True

    second_payment_cheque_preview.short_description = 'second_payment_cheque_preview Preview'
    second_payment_cheque_preview.allow_tags = True

    third_payment_cheque_preview.short_description = 'third_payment_cheque_preview Preview'
    third_payment_cheque_preview.allow_tags = True

    mutuation_preview.short_description = 'mutuation_preview Preview'
    mutuation_preview.allow_tags = True

    mutuation1_preview.short_description = 'mutuation1_preview Preview'
    mutuation1_preview.allow_tags = True
    mutuation2_preview.short_description = 'mutuation2_preview Preview'
    mutuation2_preview.allow_tags = True
    mutuation3_preview.short_description = 'mutuation3_preview Preview'
    mutuation3_preview.allow_tags = True
    mutuation4_preview.short_description = 'mutuation4_preview Preview'
    mutuation4_preview.allow_tags = True
    mutuation5_preview.short_description = 'mutuation5_preview Preview'
    mutuation5_preview.allow_tags = True


    mul_dolil_preview.short_description = 'mul_dolil_preview Preview'
    mul_dolil_preview.allow_tags = True
    mul_dolil1preview.short_description = 'mul_dolil1preview Preview'
    mul_dolil1preview.allow_tags = True
    mul_dolil2preview.short_description = 'mul_dolil2preview Preview'
    mul_dolil2preview.allow_tags = True
    mul_dolil3preview.short_description = 'mul_dolil3preview Preview'
    mul_dolil3preview.allow_tags = True
    mul_dolil4preview.short_description = 'mul_dolil4preview Preview'
    mul_dolil4preview.allow_tags = True
    mul_dolil5preview.short_description = 'mul_dolil5preview Preview'
    mul_dolil5preview.allow_tags = True
    mul_dolil6preview.short_description = 'mul_dolil6preview Preview'
    mul_dolil6preview.allow_tags = True
    mul_dolil7preview.short_description = 'mul_dolil7preview Preview'
    mul_dolil7preview.allow_tags = True
    mul_dolil8preview.short_description = 'mul_dolil8preview Preview'
    mul_dolil8preview.allow_tags = True
    mul_dolil9preview.short_description = 'mul_dolil9preview Preview'
    mul_dolil9preview.allow_tags = True
    mul_dolil10preview.short_description = 'mul_dolil10preview Preview'
    mul_dolil10preview.allow_tags = True
    mul_dolil11preview.short_description = 'mul_dolil11preview Preview'
    mul_dolil11preview.allow_tags = True
    mul_dolil12preview.short_description = 'mul_dolil12preview Preview'
    mul_dolil12preview.allow_tags = True
    mul_dolil13preview.short_description = 'mul_dolil13preview Preview'
    mul_dolil13preview.allow_tags = True
    mul_dolil14preview.short_description = 'mul_dolil14preview Preview'
    mul_dolil14preview.allow_tags = True
    mul_dolil15preview.short_description = 'mul_dolil15preview Preview'
    mul_dolil15preview.allow_tags = True
    mul_dolil16preview.short_description = 'mul_dolil16preview Preview'
    mul_dolil16preview.allow_tags = True
    mul_dolil17preview.short_description = 'mul_dolil17preview Preview'
    mul_dolil17preview.allow_tags = True
    mul_dolil18preview.short_description = 'mul_dolil18preview Preview'
    mul_dolil18preview.allow_tags = True
    mul_dolil19preview.short_description = 'mul_dolil19preview Preview'
    mul_dolil19preview.allow_tags = True
    mul_dolil20preview.short_description = 'mul_dolil20preview Preview'
    mul_dolil20preview.allow_tags = True




# Register your models here.

admin.site.register(Plot , PlotAdmin)

