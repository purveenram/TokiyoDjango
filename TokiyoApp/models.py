from typing import Any
from django.db import models
from django.utils import timezone

class CustomerDetail(models.Model):
    customerName = models.CharField('Customer Name', max_length=30)
    customerEmail = models.CharField('Email ID', max_length=40)
    customerPhone = models.IntegerField('Phone No')
    customerPassword = models.CharField('Password', max_length=14)
    customerDateOfBirth = models.DateField(null=True)
    customerGender = models.CharField('Gender', max_length=6)
    
    def __str__(self):
        return f"The Customer : {self.customerName}"

class CustomerAddressDetail(models.Model):
    customerId = models.ForeignKey(CustomerDetail, on_delete=models.CASCADE)
    cutomerHouseNo = models.CharField('Customer House No', max_length=10)
    cutomerAddressLine1  = models.CharField('Address Line 1', max_length=30)
    cutomerAddressLine2  = models.CharField('Address Line 2', max_length=30)
    customerCity = models.CharField('City', max_length=20)
    customerState = models.CharField('State', max_length=20)
    customerPinCode = models.IntegerField('Pin Code')
    customerDeliveryNumber = models.IntegerField('Delivery Phone No')
    
    def __str__(self):
        return f"Address Id {self.customerId.customerName}"


class ProductDetail(models.Model):

    CATEGORY_CHOICES = [
        ('Action Figure', 'Action Figure'),
        ('Accessories', 'Accessories'),
        ('Katana', 'Katana'),
        ('Posters', 'Posters'),
    ]
    SUB_CATEGORY_CHOICES = [
        ('NARUTO', 'NARUTO'),
        ('ONE PIECE', 'ONE PIECE'),
        ('DEMON SLAYER', 'DEMON SLAYER'),
        ('ONE PUNCH MAN', 'ONE PUNCH MAN'),
        ('ATTACK ON TITAN', 'ATTACK ON TITAN'),
        ('TOKYO REVENGER', 'TOKYO REVENGER'),
        ('JUJUTSU KAISEN', 'JUJUTSU KAISEN'),
        ('DEATH NOTE', 'DEATH NOTE'),
        ('GOKU', 'GOKU'),
    ]
    CHARACTER_CHOICES = [
        ('NARUTO', [
            ('Naruto', 'Naruto'),
            ('Kakashi', 'Kakashi'),
            ('Sasuke', 'Sasuke'),
            ('Sakura', 'Sakura'),
            ('Jiraiya', 'Jiraiya'),
            ('Akatsuki', 'Akatsuki'),
            ('Iruka Sensei', 'Iruka Sensei'),
            ('Pain', 'pain'),
            ('Itachi Uchiha', 'Itachi Uchiha'),
            ('Gaara', 'Gaara'),
            ('Tsunade', 'Tsunade'),
            ('Zetsu', 'Zetsu'),
            ('Mighty Guy', 'Mighty Guy'),
            ('Madara Uchiha', 'Madara Uchiha'),
        ]),
        ('ONE PIECE', [
            ('STRAW HAT LUFFY', 'STRAW HAT LUFFY'),
            ('VINSMOKE SANJI', 'VINSMOKE SANJI'),
            ('RORONOA ZORO', 'RORONOA ZORO'),
            ('NAMI', 'NAMI'),
            ('CHOPPER', 'CHOPPER'),
            ('Nico Robin', 'Nico Robin'),
            ('Brook', 'Brook'),
            ('God Usopp', 'God Usopp'),
            ('Franky', 'Franky'),
            ('Jimbe', 'Jimbe'),
            ('White Beard', 'White Beard'),
            ('Donquixote Rosinante', 'Donquixote Rosinante'),
            ('Donquixote Dofamingo', 'Donquixote Dofamingo'),
            ('Boa Hancock', 'Boa Hancock'),
            ('Dracule Mihawk', 'Dracule Mihawk'),
            ('Gol D Roger', 'Gol D Roger'),
            ('Shanks', 'Shanks'),
            ('Monkey D Garp', 'Monkey D Garp'),
            ('Trafalgar D Law', 'Trafalgar D Law'),
            ('Rebecca', 'Rebecca'),
            ('Big Mom', 'Big Mom'),
            ('Portgas D Ace', 'Portgas D Ace'),
        ]),
        ('DEMON SLAYER', [
            ('TANJIRO KAMADO', 'TANJIRO KAMADO'),
            ('INOSUKE HASHIBIRA', 'INOSUKE HASHIBIRA'),
            ('ZENITSU AGATSUMA', 'ZENITSU AGATSUMA'),
            ('NEZUKO KAMADO', 'NEZUKO KAMADO'),
            ('GIYU TOMIOKA', 'GIYU TOMIOKA'),
            ('MUZAN KIBUTSUJI', 'MUZAN KIBUTSUJI'),
            ('RENGOKU', 'RENGOKU'),
            ('GENYA SHINAZUGAWA', 'GENYA SHINAZUGAWA'),
            ('MUICHIRO TOKITO', 'MUICHIRO TOKITO'),
            ('Tengen Uzui', 'Tengen Uzui'),
            ('Mitsuri Kanroji', 'Mitsuri Kanroji'),
        ]),
        ('ONE PUNCH MAN', [
            ('SAITAMA', 'SAITAMA'),
            ('MUMEN RAIDER', 'MUMEN RAIDER'),
            ('GENOS', 'GENOS'),
            ('SILVER FANG', 'SILVER FANG'),
            ('TORNADO OF TERROR', 'TORNADO OF TERROR'),
            ('CHILD EMPEROR', 'CHILD EMPEROR'),
            ('FUBUKI', 'FUBUKI'),
            ('AMAI MASK', 'AMAI MASK'),
        ]),
        ('ATTACK ON TITAN', [
            ('EREN YEAGER', 'EREN YEAGER'),
            ('ERWIN SMITH', 'ERWIN SMITH'),
            ('LEVI ACKERMAN', 'LEVI ACKERMAN'),
            ('JEAN KIRSTEIN', 'JEAN KIRSTEIN'),
        ]),
        ('TOKYO REVENGER', [
            ('Draken', 'Draken'),
            ('Takemichi Hanagaki', 'Takemichi Hanagaki'),
            ('Takashi Mitsuya', 'Takashi Mitsuya'),
        ]),
        ('JUJUTSU KAISEN', [
            ('Yuji Itadori', 'Yuji Itadori'),
            ('Satoru Gojo', 'Satoru Gojo'),
            ('Nanami', 'Nanami'),
            ('Sukuna', 'Sukuna'),
            
        ]),
        ('DEATH NOTE', [
            ('Ryuk', 'Ryuk'),
            ('Light Yagami', 'Light Yagami'),
            ('Teru Mikami', 'Teru Mikami'),
        ]),
        ('GOKU', [
            ('GOKU', 'GOKU'),
        ]),
    ]

    productImage = models.ImageField("Product Image", upload_to='productImages/')
    productName = models.CharField('Product Name', max_length=50)
    productCategory = models.CharField('Product Category', max_length=40, choices=CATEGORY_CHOICES)
    productSubCategory = models.CharField('Product Sub Category', max_length=40, choices=SUB_CATEGORY_CHOICES)
    productCharacterCategory = models.CharField('Product Character Category', max_length=40, choices=CHARACTER_CHOICES)
    productPrice = models.DecimalField('Product Price', max_digits=7, decimal_places=2)
    productSellingPrice = models.DecimalField('Product Selling Price', max_digits=7, decimal_places=2)
    productQuantity = models.DecimalField('Product Quantity', max_digits=5, decimal_places=2)
    productDescription = models.TextField('Product Description')


    def __str__(self):
        return f"The : {self.productName} {self.id}"

class ProductImage(models.Model):
    product = models.ForeignKey(ProductDetail, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField("Product Image", upload_to='productImages/')
    
    def __str__(self):
        return f"Image for {self.product.productName}"

class CartDetail(models.Model):
    customerIdInCart = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE)
    productIdInCart = models.ForeignKey(ProductDetail,to_field='id', on_delete=models.CASCADE)
    productQuantityInCart = models.DecimalField("Quantity", max_digits=3, decimal_places=0)
    productPrizingInCart = models.DecimalField("Sum of products", max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return f"Card {self.id}"
    
class OrderDetail(models.Model):
    customerIdInOrder = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE)
    tokiyoOrderId = models.DecimalField('Tokiyo Order Id',  max_digits=9, decimal_places=0) # 369000001
    deliverAddressInOrder = models.CharField('Delivery Address', max_length=140)
    deliveryNumberInOrder = models.IntegerField('Delivery Phone No')
    totalItemCostInOrder = models.DecimalField('Total cost', max_digits=9, decimal_places=2)
    discountInOrder = models.DecimalField('Discount', max_digits=9, decimal_places=2)
    totalAmountPaidInOrder = models.DecimalField('Total amount paid', max_digits=9, decimal_places=2)
    orderPlacedTimeDate = models.CharField('order Placed Time & Date', max_length=30,default=None)
    orderPlacedDate = models.DateField(null=True,default=timezone.now)
    orderDeliveredDate = models.DateField(null=True,default=timezone.now)
    orderStatusInOrder = models.CharField('Delivery Status', max_length=1,default='N')

    def __str__(self):
        return f"Order :{self.tokiyoOrderId}"
    
class OrderDetailsProduct(models.Model):
    customerIdInODP = models.ForeignKey(CustomerDetail, to_field='id', on_delete=models.CASCADE,default=None)
    orderDetailSId = models.ForeignKey(OrderDetail, to_field='id', on_delete=models.CASCADE)
    productIdInODP = models.ForeignKey(ProductDetail,to_field='id', on_delete=models.CASCADE)
    productQuantityInODP = models.DecimalField("Quantity", max_digits=3, decimal_places=0)
    productPrizingInODP = models.DecimalField("Sum of products", max_digits=10, decimal_places=2,default=0.0)

    def __str__(self):
        return f"order details {self.id}_{self.productIdInODP.productName}"
