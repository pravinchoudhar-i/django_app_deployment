from django.shortcuts import render,redirect
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import *
from django.contrib.auth import authenticate, login
from django.contrib.auth.signals import user_logged_in, user_logged_out, user_login_failed

import logging
user_logger = logging.getLogger("user")
        
# save login activity in MasterLog table
@receiver(user_logged_in)
def log_user_login(sender, user, **kwargs):
    """ log user login to user log """
    activity = 'Login'
    description = 'auth | user'
    master_log = MasterLog.objects.create(
        activity = activity, description = description, user_id = user.id
    )
    user_logger.info('%s login successful', user)
  

# save logout activity in MasterLog table
@receiver(user_logged_out)
def log_user_logout(sender, user, **kwargs):
    """ log user logout to user log """
    try:
        activity = 'Logout'
        description = 'auth | user'
        master_log = MasterLog.objects.create(
            activity = activity, description = description, user_id = user.id
        )
        user_logger.info('%s log out successful', user)
    except:
        return redirect('user-logout')
