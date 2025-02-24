from django.contrib import admin

from api.models import User, University, Student, Sponsor, StudentSponsor, PaymentSummary

admin.site.register(User)
admin.site.register(University)
admin.site.register(Student)
admin.site.register(Sponsor)
admin.site.register(StudentSponsor)
admin.site.register(PaymentSummary)
