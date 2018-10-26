#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import time
import json
import requests
import re

from src import InstaBot
from src.check_status import check_status
from src.feed_scanner import feed_scanner
from src.follow_protocol import follow_protocol
from src.unfollow_protocol import unfollow_protocol
from src.userinfo import UserInfo
from src.user_info import get_user_info



bot = InstaBot(
    login="testosllab",
    password="testosllab123",
    like_per_day=500,
    comments_per_day=0,
    tag_list=['follow4follow', 'f4f', 'cute', 'l:212999109'],
    tag_blacklist=['rain', 'thunderstorm'],
    user_blacklist={},
    max_like_for_one_tag=50,
    follow_per_day=500,
    follow_time=1 * 60,
    unfollow_per_day=0,
    unfollow_break_min=15,
    unfollow_break_max=30,
    log_mod=0,
    proxy='',)
username="testosllab"
bot.get_userinfo_by_name(username)