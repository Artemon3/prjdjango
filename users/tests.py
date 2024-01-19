from django.test import TestCase

# Create your tests here.













































# class ProfileView(UpdateView):
#
#     model = User
#     form_class = UserProfileForm
#     success_url = reverse_lazy('users:profile')
#
#     def get_object(self, queryset=None):
#         return self.request.user
#
#
# def generate_new_password(request):
#     new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
#     send_mail(
#         subject='Вы сменили пароль',
#         message=f'Ваш новый пароль: {new_password}',
#         from_email=settings.EMAIL_HOST_USER,
#         recipient_list=[request.user.email]
#     )
#     request.user.set_password(new_password)
#     request.user.save()
#     return redirect(reverse('catalog:merchandise'))
