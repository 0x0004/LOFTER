#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, datetime
reload(sys)
sys.setdefaultencoding('utf-8')
LOFTERSettings = {
    'post_types': ('post', 'page'), # deprecated
    'allow_registration': os.environ.get('allow_registration', 'false').lower() == 'true',
    'allow_su_creation': os.environ.get('allow_su_creation', 'false').lower() == 'true',
    'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
    'auto_role': os.environ.get('auto_role', 'reader').lower(),
    'blog_meta': {
        'name': os.environ.get('name').decode('utf8') if os.environ.get('name') else 'LOFTER',
        'subtitle': os.environ.get('subtitle').decode('utf8') if os.environ.get('subtitle') else '记录生活  发现美好',
        'description': os.environ.get('description').decode('utf8') if os.environ.get('description') else '轻巧  随性',
        'wechat_name': os.environ.get('wechat_name').decode('utf8') if os.environ.get('wechat_name') else 'LOFT ER Wechat Root',
        'wechat_subtitle': os.environ.get('wechat_subtitle').decode('utf8') if os.environ.get('wechat_subtitle') else 'LOFT ER Wechat Subtitle',
        'owner': os.environ.get('owner').decode('utf8') if os.environ.get('owner') else '0x0004',
        'keywords': os.environ.get('keywords').decode('utf8') if os.environ.get('keywords') else 'Python,Django,Flask,Docker,MongoDB',
        'google_site_verification': os.environ.get('google_site_verification') or '12345678',
        'baidu_site_verification': os.environ.get('baidu_site_verification') or '87654321',
        'sogou_site_verification': os.environ.get('sogou_site_verification') or '87654321',
    },
    'search_engine_submit_urls':{
        'baidu': os.environ.get('baidu_submit_url')
    },
    'pagination':{
        'per_page': int(os.environ.get('per_page', 5)),
        'admin_per_page': int(os.environ.get('admin_per_page', 10)),
        'archive_per_page': int(os.environ.get('admin_per_page', 20)),
    },
    'blog_comment':{
        'allow_comment': os.environ.get('allow_comment', 'true').lower() == 'true',
        'comment_type': os.environ.get('comment_type', 'lofter').lower(), # currently, LOFTER only supports duoshuo comment
        'comment_opt':{
            'lofter': 'loft-er', # shotname of lofter
            'duoshuo': 'loft-er', # shotname of duoshuo
            }
    },
    'donation': {
        'allow_donate': os.environ.get('allow_donate', 'true').lower() == 'true',
        'donation_msg': os.environ.get('donation_msg', 'You can donate to me if the article makes sense to you ;)').decode('utf8')
    },
    'wechat': {
        'display_wechat': os.environ.get('display_wechat', 'true').lower() == 'true',
        'wechat_msg': os.environ.get('wechat_msg', ' ').decode('utf8')
    },
    'copyright': {
        'display_copyright': os.environ.get('allow_donate', 'true').lower() == 'true',
        'copyright_msg': os.environ.get('copyright_msg', 'The article is not allowed to repost unless author authorized').decode('utf8')
    },
    'only_abstract_in_feed': os.environ.get('only_abstract_in_feed', 'false').lower() == 'true',
    'allow_share_article': os.environ.get('allow_share_article', 'true').lower() == 'true',
    'gavatar_cdn_base': os.environ.get('gavatar_cdn_base', '//cdn.v2ex.com/gravatar/'),
    'gavatar_default_image': os.environ.get('gavatar_default_image', 'http://7tsygu.com1.z0.glb.clouddn.com/user-avatar.jpg'),

}

class Config(object):
    DEBUG = False
    TESTING = False

    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fjdljLJDL08_80jflKzcznv*c'
    MONGODB_SETTINGS = {'DB': 'LOFTER'}

    TEMPLATE_PATH = os.path.join(BASE_DIR, 'templates').replace('\\', '/')
    STATIC_PATH = os.path.join(BASE_DIR, 'static').replace('\\', '/')
    EXPORT_PATH = os.path.join(BASE_DIR, 'exports').replace('\\', '/')

    if not os.path.exists(EXPORT_PATH):
        os.makedirs(EXPORT_PATH)

    REMEMBER_COOKIE_DURATION = datetime.timedelta(hours=3)


    @staticmethod
    def init_app(app):
        pass

class DevConfig(Config):
    DEBUG = True

class PrdConfig(Config):
    # DEBUG = False
    DEBUG = os.environ.get('DEBUG', 'false').lower() == 'true'
    MONGODB_SETTINGS = {
            'db': 'LOFTER',
            'host': os.environ.get('MONGO_HOST') or 'localhost',
            # 'port': 12345
        }

class TestingConfig(Config):
    TESTING = True
    DEBUG = True
    MONGODB_SETTINGS = {'DB': 'LOFTERTest'}
    WTF_CSRF_ENABLED = False

config = {
    'dev': DevConfig,
    'prd': PrdConfig,
    'testing': TestingConfig,
    'default': DevConfig,
}
