import random
from random import randint

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from config import settings
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')
    template_name = 'users/register.html'

    def form_valid(self, form):
        verified_password = ''
        for i in range(8):
            i = randint(0, 9)
            verified_password += str(i)

        form.verified_password = verified_password
        user = form.save()
        user.verified_password = verified_password
        send_mail(
            subject='Верификация почты',
            message=f'Если вы регистрировались: нажмите на ссылку: http://127.0.0.1:8000/users/verifying?code={user.verified_password}\n Так вы подтвердите почту',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[user.email]
        )

        return super().form_valid(form)


@login_required
def verify_view(request):
    code = int(request.GET.get('code'))
    user = User.objects.get(verified_password=code)
    user.verified = True
    user.save()
    return render(request, 'users/verifying.html')


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def reset_password(request):
    if request.method == 'POST':
        # получение почты из формы
        user_email = request.POST.get('email')
        # генерация пароля
        new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
        send_mail(
            subject='восстановить пароль',
            message=f'пароль {new_password}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[request.user.email]
        )
        # поиск пользователя с указанной почтой
        user_reset_pass = User.objects.get(email=user_email)
        # обновление пароля этому пользователю
        user_reset_pass.set_password(new_password)
        user_reset_pass.save()
    return render(request, 'users/reset.html')
