from celery.schedules import crontab

prod_beats = {
    "update_ipv6": {
        "task": "tasks.ip_task.update_ipv6",
        "schedule": 300,
    },
    "schedule_ipv6": {
        "task": "tasks.ip_task.schedule_ipv6",
        "schedule": crontab(minute="00", hour="09"),
    },
}
