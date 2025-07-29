# from apscheduler.schedulers.blocking import BlockingScheduler
# from datetime import datetime, timedelta
# from poster import post_random_image

# scheduler = BlockingScheduler()

# # Define end time (1 month from now)
# end_date = datetime.now() + timedelta(days=30)

# def scheduled_task():
#     now = datetime.now()
#     if now > end_date:
#         print("[INFO] Scheduler finished (1 month completed). Shutting down.")
#         scheduler.shutdown()
#         return
    
#     print(f"[SCHEDULED TASK] Running at {now.strftime('%Y-%m-%d %H:%M:%S')}")
#     try:
#         for i in range(4):  # 4 images every 3 hours
#             print(f"Posting image {i+1}...")
#             post_random_image()
#     except Exception as e:
#         print(f"[ERROR] Scheduled post failed: {str(e)}")

# # Schedule the task every 3 hours
# scheduler.add_job(scheduled_task, 'interval', hours=3, next_run_time=datetime.now())

# print("[INFO] Scheduler started... Posting every 3 hours.")
# scheduler.start()


from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime, timedelta
from poster import post_random_image

scheduler = BlockingScheduler()

# Define end time (1 month from now)
end_date = datetime.now() + timedelta(days=30)

def scheduled_task():
    now = datetime.now()
    if now > end_date:
        print("[INFO] Scheduler finished (1 month completed). Shutting down.")
        scheduler.shutdown()
        return
    
    print(f"[SCHEDULED TASK] Running at {now.strftime('%Y-%m-%d %H:%M:%S')}")
    try:
        post_random_image()  # Just 1 image every 10 minutes
    except Exception as e:
        print(f"[ERROR] Scheduled post failed: {str(e)}")

# Schedule the task every 10 minutes
scheduler.add_job(scheduled_task, 'interval', minutes=10, next_run_time=datetime.now())

print("[INFO] Scheduler started... Posting every 10 minutes.")
scheduler.start()
