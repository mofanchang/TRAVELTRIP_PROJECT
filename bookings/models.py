from django.db import models
from django.conf import settings

class Booking(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    
    # 訂單狀態（例如 Pending, Completed, Cancelled）
    status = models.CharField(max_length=20, default='Pending')

    # PayPal 交易ID，用來對應 PayPal 的付款訂單
    paypal_transaction_id = models.CharField(max_length=100, null=True, blank=True)

    # 付款完成時間（可以選擇性加）
    payment_completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Booking {self.id} by {self.user.username}"
