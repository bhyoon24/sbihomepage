from django.db import models

class member(models.Model):
    member_name = models.CharField(max_length=100)
    member_cellphone = models.CharField(max_length=20)
    member_email = models.EmailField()
    regdate = models.DateTimeField()

    class Meta:
        ordering = ['-regdate']

    def __str__(self):
        return "이름 : " + self.member_name + "    전화번호 : " + self.member_cellphone+ "    등록일자 : " + self.regdate.strftime("%Y-%m-%d %h:%M:%S")

