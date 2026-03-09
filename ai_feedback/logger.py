import datetime

def log_event(task, stage, message):

    with open("interaction_log.txt", "a") as f:
        timestamp = datetime.datetime.now()

        f.write(
            f"{timestamp} | {task} | {stage} | {message}\n"
        )

        if(stage == "Review"):
            f.write(f"----------------------------------------------------------------------------------------------------------------------------------------------------------\n")