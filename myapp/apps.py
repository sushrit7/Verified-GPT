from django.apps import AppConfig
from django.db.models.signals import post_migrate
from threading import Thread
import time
import logging
from django.dispatch import receiver

# Set up logging
logger = logging.getLogger(__name__)

class MyappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myapp'

    def ready(self):
        self.start_background_task()

    @receiver(post_migrate)
    def start_background_task(self, **kwargs):
        print("Starting background task.")
        
        # Start the background task after the app is fully loaded
        def check_and_run_tasks():
            print("Starting background task.")
            while True:
                time.sleep(180)  # Check every 6 seconds (adjust as needed)
                print("Checking answers...")
                self.run_scheduled_tasks()

        # Start the background thread to check tasks
        thread = Thread(target=check_and_run_tasks, daemon=True)
        thread.start()  

    def run_scheduled_tasks(self):
        # This method can be called periodically or when needed
        self.execute_task()

    def execute_task(self):
        print("Executing scheduled task.")
        self.check_answers_for_upvotes_and_comments(min_upvotes=4, min_comments=2)

    def check_answers_for_upvotes_and_comments(self, min_upvotes, min_comments):
        from .models import Question  # Import models here to avoid AppRegistryNotReady

        print(f"Checking answers for upvotes >= {min_upvotes} and comments >= {min_comments}")
        
        questions = Question.objects.all()  # Get all questions
        for question in questions:
            # Loop through all answers related to the question
            for answer in question.answers.all():
                # Get the number of comments for the current answer
                comment_count = answer.comments.count()

                # Check if the answer meets the criteria for upvotes and comments
                if answer.upvotes >= min_upvotes and comment_count >= min_comments:
                    print(f"Answer with {answer.upvotes} upvotes and {comment_count} comments meets the criteria.")
                    # Trigger the specific code
                    self.trigger_specific_code(question.id)
                else:
                    print(f"Answer for question '{question.text[:50]}' does not meet criteria.")

    def trigger_specific_code(self, answer):
        from .views import updates_thread
        # This is where your custom logic for the triggered code goes
        updates_thread(answer)