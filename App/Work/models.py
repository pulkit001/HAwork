from django.db import models

# Create your models here.
STATUS_CHOICES = (
  ('Pending','Pending'),
  ('Approved','Approved'),
  ('Cancelled','Cancelled') ,
  ('Solved' ,  'Solved')
)



class Lost(models.Model):
    LDAP = models.EmailField()
    HostelN = models.CharField(max_length=100)
    Article = models.CharField(max_length=100)
    Date = models.DateTimeField()
    PlaceLost = models.TextField()
    Details  = models.TextField()
    Name = models.CharField(max_length=100)
    Contact = models.CharField(max_length=100)
    AddressItem = models.CharField(max_length=300)
    ImageLost = models.ImageField(upload_to='Lost')
    Status = models.CharField(choices=STATUS_CHOICES,default='Pending' , max_length=200)

    def __str__(self):
        return f"{self.Article}"


class Found(models.Model):
    HostelN = models.CharField(max_length=100)
    Article = models.CharField(max_length=100)
    Date = models.DateTimeField()
    PlaceFound = models.TextField()
    Details  = models.TextField()
    Name = models.CharField(max_length=100)
    LDAP = models.EmailField()
    Contact = models.CharField(max_length=100)
    AddressItem = models.CharField(max_length=300)
    ImageFound = models.ImageField(upload_to='Found')
    Status = models.CharField(choices=STATUS_CHOICES,default='Pending' , max_length=200)
    def __str__(self):
        return f"{self.Article}"

class ContactOffice(models.Model):
    Name = models.CharField(max_length=300)
    Position = models.CharField(max_length=400)
    Contact = models.CharField(max_length=100)
    Email = models.EmailField()

    def __str__(self):
        return f"{self.Name}"
