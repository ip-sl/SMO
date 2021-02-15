from django.db import models

# Create your models here.

PED = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
VT = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
US = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
BS = (
        ('Y', 'Yes'),
        ('N', 'No'),
    )
PW= (
        ('W','Withdrawal of consent'),
        ('S','Significant subject noncompliance'),
        ('n','Investigator Decision'),
        ('o','Other'),
        ('n','No')
    )  
ECG=(
      ('Yes','Yes'),
      ('No','No'),
   )
AV=(
       ('Yes','Yes'),
       ('No','No'),
   )   
DS=(
       ('Yes','Yes'),
       ('No','No'),
   )   
AER=(
       ('Yes','Yes'),
       ('No','No'),
   )  
PD=(
       ('Yes','Yes'),
       ('No','No'),
   )  
PK=(
       ('Yes','Yes'),
       ('No','No'),
   )  
UR=(
       ('Yes','Yes'),
       ('No','No'),
   )           
class sponsor(models.Model):
    name=models.CharField(max_length=200)
    Sposnor_Address=models.CharField(max_length=200)

    class Meta:
        verbose_name = "Sponsor"
        verbose_name_plural = "Sponsor"

    def __str__(self):
        return self.name

class protocol(models.Model):
    add_protocol=models.ForeignKey(sponsor,on_delete=models.CASCADE)
    protocol_no=models.CharField(max_length=200)
    study_details=models.TextField(blank=True)

    class Meta:
        verbose_name = "Protocol"
        verbose_name_plural = "Protocol"

    def __str__(self):
        return self.protocol_no
       

class site(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE)
    site_name=models.CharField(max_length=200)
    site_address=models.CharField(max_length=200)
    PI_Name=models.CharField(max_length=200)
    Sub_I_name=models.CharField(max_length=200)
    SIV_Date=models.DateField(null=True)

    class Meta:
        verbose_name = "Site"
        verbose_name_plural = "Site"    

    def __str__(self):
        return self.site_name

class site_Registration(models.Model):
   The = models.CharField('Therapetic Area',max_length=200)
   PI = models.FileField('PI Data upload',max_length=200)
   sub_I = models.FileField('Sub I Data upload',max_length=200)
   ECdata = models.FileField('EC Data Upload',max_length=100,blank=True)
   lab= models.FileField('Lab Data upload',max_length=100,blank=True)
   

   class Meta:
        verbose_name = "Site Registration"
        verbose_name_plural = "Site Registration"    

   def __str__(self):
        return self.site_name        

class screening(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Screening Date',max_length=100)
    DOB=models.CharField('Date Of Birth',max_length=100)
    icpd=models.CharField('Informed Consent Process Date',max_length=100)
    AV=models.CharField('Audio-Video Consent Taken',choices=AV,max_length=400,null=True)
    avtime=models.CharField('Audio-Video Consent Time',help_text='If <b>Yes</b> please enter time.',max_length=100)
    ped=models.CharField('Physical Exam Done',max_length=10,choices=PED) 
    vital=models.CharField('Vitals Taken',max_length=100,choices=VT)
    ECG_Taken=models.CharField('ECG Taken',max_length=100,choices=ECG,null=True)
    ECG=models.CharField('ECG Time',help_text='If <b>Yes</b> please enter time.',max_length=100)
    us=models.CharField('Urine Sample',max_length=10,choices=US)
    ust=models.CharField('Urine Sample Time',max_length=100)
    BS=models.CharField('Blood Sample',max_length=10,choices=BS)
    BST=models.CharField('Blood Sample Time',max_length=100)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=100)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD=models.CharField('Protocol deviation if any',choices=PD,max_length=100) 
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description')
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)        
     
    class Meta:
        verbose_name = "Screening"
        verbose_name_plural = "Screening" 
     
    def __str__(self):
        return self.patient_number 

class day1(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    DOB=models.CharField('Date Of Birth',max_length=100)
    Randomization=models.CharField('Randomization Number',max_length=200)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    ped=models.CharField('Physical Exam Done',max_length=10,choices=PED) 
    vital=models.CharField('Vitals Taken',max_length=100,choices=VT)
    PK_Blood=models.CharField('PK Blood Sample Taken',choices=PK,max_length=200,null=True)
    PK=models.CharField('First Sample Time',max_length=100,null=True)
    PK_second=models.CharField('Second Sample Time',max_length=100,null=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=500)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD=models.CharField('Protocol deviation if any',choices=PD,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)        
    patient_Withdrawal=models.CharField(choices=PW,max_length=500,null=True)
    other=models.TextField('Other',blank=True)
    
    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 1"

    def __str__(self):
        return self.patient_number

class day2(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Done',choices=PED,max_length=500)
    Vital=models.CharField('vitals',choices=VT,max_length=100)
    Blood_Sample=models.CharField(choices=BS,max_length=500)
    Blood_Sample_Time=models.CharField(max_length=100)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD=models.CharField('Protocol deviation if any',choices=PD,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    patient_Withdrawal=models.CharField(choices=PW,max_length=500,null=True)
    other=models.TextField('Other',blank=True)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 2"

    def __str__(self):
        return self.patient_number

class day3(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Done',choices=PED,max_length=500)
    Vital=models.CharField('vitals',choices=VT,max_length=100)
    DDT=models.CharField('Drugs Dosing Time',max_length=10)
    Blood_Sample=models.CharField(max_length=500)
    Blood_Sample_Time=models.CharField(max_length=100,null=True)
    PK_Blood=models.CharField('PK Blood Sample Taken',choices=PK,max_length=200,null=True)
    PK=models.CharField('First Sample Time',max_length=100,null=True)
    PK_second=models.CharField('Second Sample Time',max_length=100,null=True)
    PK_Third=models.CharField('Third Sample Time',max_length=100,null=True)
    PK_Fourth=models.CharField('Fourth Sample Time',max_length=100,null=True)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)              
    patient_Withdrawal=models.CharField(choices=PW,max_length=500,null=True)
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other',blank=True)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 3"

    def __str__(self):
        return self.patient_number

class day4(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Done',choices=PED,max_length=500)
    Vital=models.CharField('vitals',choices=VT,max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    Blood_Sample=models.CharField(choices=BS,max_length=500)
    Blood_Sample_Time=models.CharField(max_length=100)
    PK=models.CharField('PK Blood Sample',choices=PK,max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 4"

    def __str__(self):
        return self.patient_number

class day5(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Done',choices=PED,max_length=500)
    Vital=models.CharField('vitals',choices=VT,max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    Urine=models.CharField('Urine Sample',choices=UR,max_length=100)
    Urine_Sample_Time=models.TimeField()
    Blood_Sample=models.CharField(choices=BS,max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sample',choices=PK,max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 5"

    def __str__(self):
        return self.patient_number

class day6(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Conducted',max_length=500)
    Vital=models.CharField('vitals',choices=VT,max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    Blood_Sample=models.CharField(choices=BS,max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sampling ',max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "Day"
        verbose_name_plural = "Day 6"

    def __str__(self):
        return self.patient_number

class EOIV(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Conducted',max_length=500)
    Vital=models.CharField('Vitals',max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    ECG=models.CharField(max_length=200)
    Urine=models.CharField('Urine Sample',max_length=100)
    Urine_Sample_Time=models.TimeField()
    Blood_Sample=models.CharField(max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sampling ',max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "EOVI"
        verbose_name_plural = "EOVI"

    def __str__(self):
        return self.patient_number

class EOT(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Conducted',max_length=500)
    Vital=models.CharField('Vitals',max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    ECG=models.CharField(max_length=200)
    Urine=models.CharField('Urine Sample',max_length=100)
    Urine_Sample_Time=models.TimeField()
    Blood_Sample=models.CharField(max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sampling ',max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "EOT"
        verbose_name_plural = "EOT"

    def __str__(self):
        return self.patient_number

class TOC(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Conducted',max_length=500)
    Vital=models.CharField('Vitals',max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    ECG=models.CharField(max_length=200)
    Urine=models.CharField('Urine Sample',max_length=100)
    Urine_Sample_Time=models.TimeField()
    Blood_Sample=models.CharField(max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sampling ',max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "TOC"
        verbose_name_plural = "TOC"

    def __str__(self):
        return self.patient_number


class LFU(models.Model):
    Select_Protocol=models.ForeignKey(protocol,on_delete=models.CASCADE,default=1)
    Select_Site=models.ForeignKey(site,on_delete=models.CASCADE,default=1)
    patient_number=models.CharField(max_length=100)
    Date=models.CharField('Date',max_length=100)
    PEC=models.CharField('Physical Exam Conducted',max_length=500)
    Vital=models.CharField('Vitals',max_length=100)
    DDT=models.CharField('Drug Dosing Time',max_length=100)
    ECG=models.CharField(max_length=200)
    Urine=models.CharField('Urine Sample',max_length=100)
    Urine_Sample_Time=models.TimeField()
    Blood_Sample=models.CharField(max_length=500)
    Blood_Sample_Time=models.CharField('Blood Sample Time',max_length=100)
    PK=models.CharField('PK Blood Sampling ',max_length=200)
    AER=models.CharField('Adverse Event Record',choices=AER,max_length=100)
    AE=models.CharField('Adverse Event Record Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    DSAQ=models.CharField('Daily Symptom Assessment Questionnaire Filled',choices=DS,max_length=500)
    Protocol_Deviation=models.CharField('Protocol deviation Description',max_length=500,null=True,help_text='If <b>Yes</b> Enter Description',blank=True)
    PD_Upload=models.FileField('Protocol Deviation Upload File',null=True,help_text='If <b>Yes</b> Upload file',blank=True)       
    PW=models.CharField('Patient Withdrawal',max_length=100,choices=PW,null=True)
    other=models.TextField('Other Note',blank=True)

    class Meta:
        verbose_name = "LFU"
        verbose_name_plural = "LFU"

    def __str__(self):
        return self.patient_number

    
class Meta:
        verbose_name_plural = 'My images'



     

