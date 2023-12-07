from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from .models import Service
from .forms import ServiceForm


@login_required(login_url="accounts:login")
def board_write(request):
    if request.method == 'POST':
        form = ServiceForm(request.POST)
        if form.is_valid():
            services = Service()  # 모델 클래스 변수 생성
            services.title = form.cleaned_data['title']  # form의 제목을 가져옴
            services.contents = form.cleaned_data['contents']
            services.writer = request.user  # 현재 로그인한 사용자의 id
            services.save()
            return HttpResponseRedirect('/service/board_list/')  # 작성 후 글목록으로 이동
        else:
            return render(request, 'service/board_write.html')
    else:
        form = ServiceForm()
    return render(request, 'service/board_write.html', {'form': form})

@login_required(login_url="accounts:login")
def board_list(request):
    boards = Service.objects.all().order_by('-id')

    return render(request, 'service/board_list.html', {'boards': boards})


@login_required(login_url="accounts:login")
def board_detail(request,pk):
    board = Service.objects.get(id=pk)

    return render(request, 'service/board_detail.html', {'board': board},)


@login_required(login_url="accounts:login")
def board_delete(request, pk):
    board = get_object_or_404(Service, id=pk)
    if request.user == board.writer:
        board.delete()
    return redirect('service:board_list')


@login_required(login_url="accounts:login")
def board_update(request, pk):
    board = Service.objects.get(id=pk)
    if request.method == 'POST':
        board.title = request.POST.get('title')
        board.contents = request.POST.get('contents')
        board.writer = request.user
        board.save()
        return redirect('service:board_list')
    return render(request, 'service/board_update.html',{'board':board})
#
# @login_required(login_url="accounts:login")
# def notice(request):
#     return render(request, 'board/notice.html')
