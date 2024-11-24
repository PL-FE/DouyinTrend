from datetime import datetime
from tkinter.scrolledtext import example
from typing import Optional

from pydantic import BaseModel, Field


class BaseDyVideo(BaseModel):
    video_id: int
    name: str
    video_url: str = ""
    download_url: str = ""
    title: str = ""
    tags: str = ""
    type: str = ""
    comment_count: int = 0
    share_count: int = 0
    like_count: int = 0
    favorite_count: int = 0
    duration: int = 0
    publish_time: datetime
    text_recognition: str
    remarks: str
    created_at: Optional[datetime]
    updated_at: Optional[datetime]


class claw_video_dy(BaseModel):
    urls: list[str] = Field(..., description="抖音博主主页链接", example=[
        'https://www.douyin.com/user/MS4wLjABAAAA1eKHyNikJZO_COBSzfGAy_s_U4coVcjaYnVmSAkZHnql8J32jnIuPAPbk_sN8tjQ?from_tab_name=main'])
    cookie: str = Field(..., description="抖音cookie",
                        example='ttwid=1%7CxivP0_rKPOGVO2OhbZ2iha8xJBzQS23J5xJleWwSkOU%7C1729660531%7C8785ed640379d9311156383492a93981a6319abe92bbba61fbe6554491428855; UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112bbcbeb4a6e97afffe0093f599fa4730d0aaae1885c72e7ece9994d30b493b2a61621fdb5dba23dbf82c4eb9a4c90c9c1; s_v_web_id=verify_m2lf816j_4xVOCuxM_FNdJ_4xFs_BTdd_711RVF1VSIVD; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX18sHEtDN77GeM3vH48Vt5iMDH0KZVCQKWVeY53EeoqaZQKK4InhlJhSqFdAy72xeaN6tPt7kuHgHQ==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; passport_csrf_token=2e630699d69ead94d5384bc090f9a123; passport_csrf_token_default=2e630699d69ead94d5384bc090f9a123; bd_ticket_guard_client_web_domain=2; is_staff_user=false; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112bbcbeb4a6e97afffe0093f599fa4730d4fdfd272979c31928f4a75551b4c86b4cd5d1d3cb92b558677fb825163f6b6cdb453348055af1b7fc00d5d5bbfb1659451776541e497f0d057f22afd521117b34a93c5cd8652e49dc263ed74360f5f94332ed040bd0ca6ecb22c8402153dfe16e836acb05477f099bddddf19c231d073; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; store-region=cn-cq; store-region-src=uid; my_rd=2; passport_mfa_token=CjdI9QjArm5HgmxgbBx1nrbYfFbP90pbHve7PyVJWeW1MvoAHy%2FnxBsrX%2Fm4sk1v8n9MF6Oj4VjtGkoKPA%2B48e3YaTQvLxI7ofCCK%2BR29d%2B%2BEIWv5xSZbbU%2BUW%2BZ%2FyWC7wNijRxkvmAtj3EtAEXYjUpTsJFcSEa5tRCRwd8NGPax0WwgAiIBA0wSs0E%3D; d_ticket=7ef1e792b5058222c13e95c647acec8eaf28e; passport_assist_user=CkFvdOe-430jLTqRXlsWg1Ho0sxMOg0Eu5nCsuo-03X7nA1psyrEMGst9bScPHAMnTooYzRn7UKaaXukAalwiw9maxpKCjxS1xD_MTq8tNKxNpL9-_4FHcZyyhNcJMevragMwZfj3XviKUGYHdoilC7OMH4g6-J_WKXkeUzaoaMHJzIQhMDfDRiJr9ZUIAEiAQMPOQTC; n_mh=CRGa3Hq4fzcWzlKKCemXV4BMSkA_r348LtwfzN7GRkw; sso_uid_tt=bd8b5c1a9f65559b4fbf3e1312c1fa58; sso_uid_tt_ss=bd8b5c1a9f65559b4fbf3e1312c1fa58; toutiao_sso_user=3d2c3662779018ad72997832f07ca73e; toutiao_sso_user_ss=3d2c3662779018ad72997832f07ca73e; sid_ucp_sso_v1=1.0.0-KDk3ZWExNzIyNjU2NWMzY2VjNzg3N2Y4YmM1MGQ2YmJmZTFlZjg2MGQKIQjk9-DL9My6BhD4z-K4BhjvMSAMMMKv0qsGOAZA9AdIBhoCbGYiIDNkMmMzNjYyNzc5MDE4YWQ3Mjk5NzgzMmYwN2NhNzNl; ssid_ucp_sso_v1=1.0.0-KDk3ZWExNzIyNjU2NWMzY2VjNzg3N2Y4YmM1MGQ2YmJmZTFlZjg2MGQKIQjk9-DL9My6BhD4z-K4BhjvMSAMMMKv0qsGOAZA9AdIBhoCbGYiIDNkMmMzNjYyNzc5MDE4YWQ3Mjk5NzgzMmYwN2NhNzNl; passport_auth_status=47132b70e76d6fa059dd7d7a9fb4a4de%2Cf8bf8588207eeed15a572dc99e02ec42; passport_auth_status_ss=47132b70e76d6fa059dd7d7a9fb4a4de%2Cf8bf8588207eeed15a572dc99e02ec42; uid_tt=4d07d8896036ccbbeb872df8178e22d3; uid_tt_ss=4d07d8896036ccbbeb872df8178e22d3; sid_tt=13a8593494c364c89d2abcb22e76661f; sessionid=13a8593494c364c89d2abcb22e76661f; sessionid_ss=13a8593494c364c89d2abcb22e76661f; _bd_ticket_crypt_cookie=89e9dc5ea3cfe9600905e395d4133d27; sid_guard=13a8593494c364c89d2abcb22e76661f%7C1729669118%7C5183997%7CSun%2C+22-Dec-2024+07%3A38%3A35+GMT; sid_ucp_v1=1.0.0-KDE0YjNmZWY5ZDg3MWU4NmI0Njc3MTQ0OTJiYmQxZWRhMTkxZjI4NmYKGwjk9-DL9My6BhD-z-K4BhjvMSAMOAZA9AdIBBoCbGYiIDEzYTg1OTM0OTRjMzY0Yzg5ZDJhYmNiMjJlNzY2NjFm; ssid_ucp_v1=1.0.0-KDE0YjNmZWY5ZDg3MWU4NmI0Njc3MTQ0OTJiYmQxZWRhMTkxZjI4NmYKGwjk9-DL9My6BhD-z-K4BhjvMSAMOAZA9AdIBBoCbGYiIDEzYTg1OTM0OTRjMzY0Yzg5ZDJhYmNiMjJlNzY2NjFm; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20241030%2F0%22; pwa2=%220%7C0%7C3%7C0%22; WallpaperGuide=%7B%22showTime%22%3A1730279841597%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%7D; publish_badge_show_info=%221%2C0%2C0%2C1730280531272%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=07fdbef5832b08d48db02ab4cf95f6bd; h265ErrorNum=-1; webcast_leading_last_show_time=1730340454476; webcast_leading_total_show_times=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; xg_device_score=7.6233091352684825; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; __ac_signature=_02B4Z6wo00f01Os5i9AAAIDA3B1Pjo5gWozrGY9AAF3wfe; __ac_nonce=067259e2a0084d353989d; strategyABtestKey=%221730518586.742%22; biz_trace_id=6b4d6986; IsDouyinActive=true; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAbD1lkyA4-9NeY4thNBV4ko5_NMXpw6QCRlM9tL8ehng2pfgAjFicTt5-s_6KrJ_r%2F1730563200000%2F0%2F0%2F1730520079629%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAbD1lkyA4-9NeY4thNBV4ko5_NMXpw6QCRlM9tL8ehng2pfgAjFicTt5-s_6KrJ_r%2F1730563200000%2F0%2F1730519479629%2F0%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRjdTTUNjR0xWVnBCdWdvVll2V0RkaWNpZFo5a2pRTGkrdDdoaHZqYTA5RXlXMFdmbHNFQkkzSjVTZ2E1Rm9nSkVzR2EyMG5aRVhiWW9wQ1ZqSkpNUFE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; passport_fe_beating_status=true; odin_tt=228550a0763e76934bdba5c9a64756f288be5ad96de86cb0cdf6a824c0c1e42d95268bf5d4c8dcce8c589d41b621448ffe2f0dfe2187807b911bf3422f1c39d5')


class DyVideoCreate(BaseModel):
    video_id: int = Field(example='视频id')
    dy_user_id: str = Field(example='抖音用户id')
    name: str = Field(example='博主名称')
    video_url: str = Field(example='视频url')
    download_url: str = Field(example='下载url')
    title: str = Field(example='标题')
    tags: str = Field(example='标签')
    type: str = Field(example='类型')
    comment_count: int = Field(0, example="评论数")
    share_count: int = Field(0, example="分享数")
    like_count: int = Field(0, example="喜欢数")
    favorite_count: int = Field(0, example="收藏数")
    duration: int = Field(0, example="视频时长")
    publish_time: datetime = Field(example='发布时间')
    text_recognition: str = Field(example='文本识别')
    remarks: str = Field(example='备注')


class DyVideoUpdate(BaseModel):
    id: int
    video_id: int = Field(example='视频id')
    name: str = Field(example='博主名称')
    video_url: str = Field(example='视频url')
    download_url: str = Field(example='下载url')
    title: str = Field(example='标题')
    tags: str = Field(example='标签')
    type: str = Field(example='类型')
    comment_count: int = Field(0, example="评论数")
    share_count: int = Field(0, example="分享数")
    like_count: int = Field(0, example="喜欢数")
    favorite_count: int = Field(0, example="收藏数")
    duration: int = Field(0, example="视频时长")
    publish_time: datetime = Field(example='发布时间')
    text_recognition: str = Field(example='文本识别')
    remarks: str = Field(example='备注')

    def update_dict(self):
        return self.model_dump(exclude_unset=True, exclude={"id", "video_id"})


class ClawCommentsDySchemas(BaseModel):
    video_ids: list[int] = Field(..., description="视频id", example=[7439138051776924978])
    cookie: str = Field(..., description="抖音cookie",
                        example='ttwid=1%7CxivP0_rKPOGVO2OhbZ2iha8xJBzQS23J5xJleWwSkOU%7C1729660531%7C8785ed640379d9311156383492a93981a6319abe92bbba61fbe6554491428855; UIFID_TEMP=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112bbcbeb4a6e97afffe0093f599fa4730d0aaae1885c72e7ece9994d30b493b2a61621fdb5dba23dbf82c4eb9a4c90c9c1; s_v_web_id=verify_m2lf816j_4xVOCuxM_FNdJ_4xFs_BTdd_711RVF1VSIVD; hevc_supported=true; dy_swidth=1920; dy_sheight=1080; fpk1=U2FsdGVkX18sHEtDN77GeM3vH48Vt5iMDH0KZVCQKWVeY53EeoqaZQKK4InhlJhSqFdAy72xeaN6tPt7kuHgHQ==; fpk2=7675d59b5e84e0a878ee6f0a97f9056f; passport_csrf_token=2e630699d69ead94d5384bc090f9a123; passport_csrf_token_default=2e630699d69ead94d5384bc090f9a123; bd_ticket_guard_client_web_domain=2; is_staff_user=false; UIFID=63bdc4b4b456901f349a081bfd3a24da10a1c6623f0a2d5eadd83f51c9f4d112bbcbeb4a6e97afffe0093f599fa4730d4fdfd272979c31928f4a75551b4c86b4cd5d1d3cb92b558677fb825163f6b6cdb453348055af1b7fc00d5d5bbfb1659451776541e497f0d057f22afd521117b34a93c5cd8652e49dc263ed74360f5f94332ed040bd0ca6ecb22c8402153dfe16e836acb05477f099bddddf19c231d073; SelfTabRedDotControl=%5B%5D; _bd_ticket_crypt_doamin=2; __security_server_data_status=1; store-region=cn-cq; store-region-src=uid; my_rd=2; passport_mfa_token=CjdI9QjArm5HgmxgbBx1nrbYfFbP90pbHve7PyVJWeW1MvoAHy%2FnxBsrX%2Fm4sk1v8n9MF6Oj4VjtGkoKPA%2B48e3YaTQvLxI7ofCCK%2BR29d%2B%2BEIWv5xSZbbU%2BUW%2BZ%2FyWC7wNijRxkvmAtj3EtAEXYjUpTsJFcSEa5tRCRwd8NGPax0WwgAiIBA0wSs0E%3D; d_ticket=7ef1e792b5058222c13e95c647acec8eaf28e; passport_assist_user=CkFvdOe-430jLTqRXlsWg1Ho0sxMOg0Eu5nCsuo-03X7nA1psyrEMGst9bScPHAMnTooYzRn7UKaaXukAalwiw9maxpKCjxS1xD_MTq8tNKxNpL9-_4FHcZyyhNcJMevragMwZfj3XviKUGYHdoilC7OMH4g6-J_WKXkeUzaoaMHJzIQhMDfDRiJr9ZUIAEiAQMPOQTC; n_mh=CRGa3Hq4fzcWzlKKCemXV4BMSkA_r348LtwfzN7GRkw; sso_uid_tt=bd8b5c1a9f65559b4fbf3e1312c1fa58; sso_uid_tt_ss=bd8b5c1a9f65559b4fbf3e1312c1fa58; toutiao_sso_user=3d2c3662779018ad72997832f07ca73e; toutiao_sso_user_ss=3d2c3662779018ad72997832f07ca73e; sid_ucp_sso_v1=1.0.0-KDk3ZWExNzIyNjU2NWMzY2VjNzg3N2Y4YmM1MGQ2YmJmZTFlZjg2MGQKIQjk9-DL9My6BhD4z-K4BhjvMSAMMMKv0qsGOAZA9AdIBhoCbGYiIDNkMmMzNjYyNzc5MDE4YWQ3Mjk5NzgzMmYwN2NhNzNl; ssid_ucp_sso_v1=1.0.0-KDk3ZWExNzIyNjU2NWMzY2VjNzg3N2Y4YmM1MGQ2YmJmZTFlZjg2MGQKIQjk9-DL9My6BhD4z-K4BhjvMSAMMMKv0qsGOAZA9AdIBhoCbGYiIDNkMmMzNjYyNzc5MDE4YWQ3Mjk5NzgzMmYwN2NhNzNl; passport_auth_status=47132b70e76d6fa059dd7d7a9fb4a4de%2Cf8bf8588207eeed15a572dc99e02ec42; passport_auth_status_ss=47132b70e76d6fa059dd7d7a9fb4a4de%2Cf8bf8588207eeed15a572dc99e02ec42; uid_tt=4d07d8896036ccbbeb872df8178e22d3; uid_tt_ss=4d07d8896036ccbbeb872df8178e22d3; sid_tt=13a8593494c364c89d2abcb22e76661f; sessionid=13a8593494c364c89d2abcb22e76661f; sessionid_ss=13a8593494c364c89d2abcb22e76661f; _bd_ticket_crypt_cookie=89e9dc5ea3cfe9600905e395d4133d27; sid_guard=13a8593494c364c89d2abcb22e76661f%7C1729669118%7C5183997%7CSun%2C+22-Dec-2024+07%3A38%3A35+GMT; sid_ucp_v1=1.0.0-KDE0YjNmZWY5ZDg3MWU4NmI0Njc3MTQ0OTJiYmQxZWRhMTkxZjI4NmYKGwjk9-DL9My6BhD-z-K4BhjvMSAMOAZA9AdIBBoCbGYiIDEzYTg1OTM0OTRjMzY0Yzg5ZDJhYmNiMjJlNzY2NjFm; ssid_ucp_v1=1.0.0-KDE0YjNmZWY5ZDg3MWU4NmI0Njc3MTQ0OTJiYmQxZWRhMTkxZjI4NmYKGwjk9-DL9My6BhD-z-K4BhjvMSAMOAZA9AdIBBoCbGYiIDEzYTg1OTM0OTRjMzY0Yzg5ZDJhYmNiMjJlNzY2NjFm; SEARCH_RESULT_LIST_TYPE=%22single%22; download_guide=%223%2F20241030%2F0%22; pwa2=%220%7C0%7C3%7C0%22; WallpaperGuide=%7B%22showTime%22%3A1730279841597%2C%22closeTime%22%3A0%2C%22showCount%22%3A1%2C%22cursor1%22%3A16%2C%22cursor2%22%3A4%7D; publish_badge_show_info=%221%2C0%2C0%2C1730280531272%22; douyin.com; device_web_cpu_core=16; device_web_memory_size=8; architecture=amd64; csrf_session_id=07fdbef5832b08d48db02ab4cf95f6bd; h265ErrorNum=-1; webcast_leading_last_show_time=1730340454476; webcast_leading_total_show_times=1; volume_info=%7B%22isUserMute%22%3Afalse%2C%22isMute%22%3Afalse%2C%22volume%22%3A0.5%7D; xg_device_score=7.6233091352684825; stream_player_status_params=%22%7B%5C%22is_auto_play%5C%22%3A0%2C%5C%22is_full_screen%5C%22%3A0%2C%5C%22is_full_webscreen%5C%22%3A0%2C%5C%22is_mute%5C%22%3A0%2C%5C%22is_speed%5C%22%3A1%2C%5C%22is_visible%5C%22%3A0%7D%22; stream_recommend_feed_params=%22%7B%5C%22cookie_enabled%5C%22%3Atrue%2C%5C%22screen_width%5C%22%3A1920%2C%5C%22screen_height%5C%22%3A1080%2C%5C%22browser_online%5C%22%3Atrue%2C%5C%22cpu_core_num%5C%22%3A16%2C%5C%22device_memory%5C%22%3A8%2C%5C%22downlink%5C%22%3A10%2C%5C%22effective_type%5C%22%3A%5C%224g%5C%22%2C%5C%22round_trip_time%5C%22%3A0%7D%22; __ac_signature=_02B4Z6wo00f01Os5i9AAAIDA3B1Pjo5gWozrGY9AAF3wfe; __ac_nonce=067259e2a0084d353989d; strategyABtestKey=%221730518586.742%22; biz_trace_id=6b4d6986; IsDouyinActive=true; FOLLOW_LIVE_POINT_INFO=%22MS4wLjABAAAAbD1lkyA4-9NeY4thNBV4ko5_NMXpw6QCRlM9tL8ehng2pfgAjFicTt5-s_6KrJ_r%2F1730563200000%2F0%2F0%2F1730520079629%22; FOLLOW_NUMBER_YELLOW_POINT_INFO=%22MS4wLjABAAAAbD1lkyA4-9NeY4thNBV4ko5_NMXpw6QCRlM9tL8ehng2pfgAjFicTt5-s_6KrJ_r%2F1730563200000%2F0%2F1730519479629%2F0%22; home_can_add_dy_2_desktop=%221%22; bd_ticket_guard_client_data=eyJiZC10aWNrZXQtZ3VhcmQtdmVyc2lvbiI6MiwiYmQtdGlja2V0LWd1YXJkLWl0ZXJhdGlvbi12ZXJzaW9uIjoxLCJiZC10aWNrZXQtZ3VhcmQtcmVlLXB1YmxpYy1rZXkiOiJCRjdTTUNjR0xWVnBCdWdvVll2V0RkaWNpZFo5a2pRTGkrdDdoaHZqYTA5RXlXMFdmbHNFQkkzSjVTZ2E1Rm9nSkVzR2EyMG5aRVhiWW9wQ1ZqSkpNUFE9IiwiYmQtdGlja2V0LWd1YXJkLXdlYi12ZXJzaW9uIjoyfQ%3D%3D; passport_fe_beating_status=true; odin_tt=228550a0763e76934bdba5c9a64756f288be5ad96de86cb0cdf6a824c0c1e42d95268bf5d4c8dcce8c589d41b621448ffe2f0dfe2187807b911bf3422f1c39d5')
