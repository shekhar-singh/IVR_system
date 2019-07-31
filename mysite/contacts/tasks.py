from celery.decorators import task

@task(name="sum_two_numbers")
def add(x, y):
    return x + y

@task(name="call queue")
def call(number):
	if int(number)%2==0:
		return 'Success'
	else:
		return 'Fail'