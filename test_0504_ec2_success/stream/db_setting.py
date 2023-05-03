DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'clouddb',
        'USER': 'rdsuser',
        'PASSWORD': 'rdsuser1234',
        'HOST': 'awslecturedb.cfpwksovkphh.ap-northeast-2.rds.amazonaws.com',
        'PORT': '3306',
    }
}
SECRET_KEY = 'django-insecure-zlfyw_ew!a+yzk!_+h&gyi$l6ub1=2w71#s=vube=e8p@ub(ys'