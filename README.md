Home Work 51

Home Work 52

1)
works = Work.objects.all() 
 Work.objects.filter(updated_at__range=("2022-06-10", "2022-07-20"))
 
 2)
 Work.objects.filter(status__status = 'New').filter(types__type = 'Task')

3)
w = Work.objects.filter(summary__icontains = 'bug') 
t = Work.objects.filter(types__type__icontains = 'bug') 
w | t
