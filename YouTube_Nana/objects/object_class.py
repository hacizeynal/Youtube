class User:

    def __init__(self, user_mail, user_name, user_password, user_current_job_title):
        self.email = user_mail
        self.name = user_name
        self.password = user_password
        self.current_job_title = user_current_job_title

    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.current_job_title} .You can contact them at {self.email} ")
