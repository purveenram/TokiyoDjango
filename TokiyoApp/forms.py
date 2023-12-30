from django import forms
from .models import *

class CustomerDetailsForm(forms.ModelForm):
    class Meta:
        model = CustomerDetail
        fields =  ['customerName', 'customerEmail','customerPhone','customerPassword','customerDateOfBirth','customerGender']

class CustomerAddressForm(forms.ModelForm):
    class Meta:
        model = CustomerAddressDetail
        fields =  ['customerId', 'cutomerHouseNo','cutomerAddressLine1','cutomerAddressLine2','customerCity','customerState','customerPinCode','customerDeliveryNumber']

class CartDeatilsForm(forms.ModelForm):
    class Meta:
        model = CartDetail
        fields =  ['customerIdInCart','productIdInCart','productQuantityInCart']

class OrderDeatilsForm(forms.ModelForm):
    class Meta:
        model = OrderDetail
        fields =  ['customerIdInOrder','tokiyoOrderId','deliverAddressInOrder','deliveryNumberInOrder','totalItemCostInOrder','discountInOrder','totalAmountPaidInOrder','orderPlacedTimeDate','orderPlacedDate','orderDeliveredDate','orderStatusInOrder']

class OrderDetailsProductsForm(forms.ModelForm):
    class Meta:
        model = OrderDetailsProduct
        fields =  ['customerIdInODP','orderDetailSId','productIdInODP','productQuantityInODP','productPrizingInODP']
