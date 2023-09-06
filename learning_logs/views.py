#coding:utf-8
from django.shortcuts import render

from .models import Topic,Entry
from django.http import HttpResponseRedirect,Http404
#from django.core.urlresolvers import reverse
from django.urls import reverse
from .forms import TopicForm, EntryForm
from django.contrib.auth.decorators import login_required
#用于对链接申请做出回应
# Create your views here.
def index(request): 
    return render(request, 'learning_logs\index.html')

@login_required
def topics(request): 
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
  # #topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

@login_required
def topic(request, topic_ids): 
    topic = Topic.objects.get(id=topic_ids)
    if topic.owner != request.user: 
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

@login_required
def new_topic(request): 
    """娣诲姞鏂颁富棰�""" 
    if request.method != 'POST': 
        # 鏈彁浜ゆ暟鎹細鍒涘缓涓�涓柊琛ㄥ崟
        form = TopicForm() 
    else: 
        # POST鎻愪氦鐨勬暟鎹�,瀵规暟鎹繘琛屽鐞�
        form = TopicForm(request.POST) 
        if form.is_valid(): 
            new_topic = form.save(commit=False) 
            new_topic.owner = request.user 
            new_topic.save()
            return HttpResponseRedirect(reverse('learning_logs:topics')) 
    context = {'form':form}
    return render(request, 'learning_logs/new_topic.html', context)

@login_required
def new_entry(request, topic_id): 
    """新增加内容""" 
    topic = Topic.objects.get(id=topic_id) 
    if request.method != 'POST':
        # 鏈彁浜ゆ暟鎹�,鍒涘缓涓�涓┖琛ㄥ崟
        form = EntryForm()
    else: 
        # POST鎻愪氦鐨勬暟鎹�,瀵规暟鎹繘琛屽鐞�
        form = EntryForm(data=request.POST) 
    if form.is_valid(): 
        new_entry = form.save(commit=False) 
        new_entry.topic = topic 
        new_entry.save() 
        return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id])) 
 
    context = {'topic': topic, 'form': form} 
    return render(request, 'learning_logs/new_entry.html', context)

@login_required
def edit_entry(request, entry_id): 
    """缂栬緫鏃㈡湁鏉＄洰""" 
    entry = Entry.objects.get(id=entry_id) 
    topic = entry.topic 
    if topic.owner != request.user: 
        raise Http404
    if request.method != 'POST': 
        # 鍒濇璇锋眰锛屼娇鐢ㄥ綋鍓嶆潯鐩～鍏呰〃鍗�
        form = EntryForm(instance=entry) 
    else: 
        # POST鎻愪氦鐨勬暟鎹紝瀵规暟鎹繘琛屽鐞�
        form = EntryForm(instance=entry, data=request.POST) 
        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic.id])) 
 
    context = {'entry': entry, 'topic': topic, 'form': form} 
    return render(request, 'learning_logs/edit_entry.html', context)