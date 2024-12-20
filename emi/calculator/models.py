from django.db import models

# Create your models here.

class LoanCalculation(models.Model):
    loan_amount = models.FloatField()
    loan_rate = models.FloatField()
    loan_tenure = models.IntegerField()
    tenure_type = models.CharField(max_length=10, choices=[('Years', 'Years'), ('Months', 'Months')])
    emi = models.FloatField()
    total_interest = models.FloatField()
    total_payment = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Loan EMI: {self.emi} | Total Payment: {self.total_payment}"
