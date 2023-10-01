class SMTPConfig(object):
    """配置 SMTP 服务器参数"""

    # SMTP 服务器主机地址
    host = ""

    # SMTP 服务器端口号
    port = "25"

    # 用户名
    user = ""

    # 用户密码(口令)
    password = ""

    # 收件人地址列表
    receivers = [
        ""
    ]
